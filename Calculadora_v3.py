import tkinter as tk
class Calculadora:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Calculadora 4.1")
        self.raiz.resizable(False, False)

        # ================= VARIABLES =================
        self.operacion_actual = ""
        self.historial_visible = False
        self.resultado_mostrado = False
        self.memoria = 0.0
        self.boton_mr = None
        self.color_boton_defecto = ""

        # ================= FRAME PRINCIPAL =================
        marco_principal = tk.Frame(self.raiz, bg="#d9d9d9")
        marco_principal.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)

        # ================= PANTALLA =================
        self.pantalla = tk.Entry(marco_principal, font=("Arial", 24), justify="right", bd=10, relief="sunken")
        self.pantalla.grid(row=0, column=0, columnspan=5, pady=5, sticky="nsew")

        # ================= HISTORIAL =================
        self.marco_historial = tk.Frame(self.raiz, bg="#f0f0f0", width=200)
        self.etiqueta_historial = tk.Label(self.marco_historial, text="Historial", font=("Arial", 14, "bold"), bg="#f0f0f0")
        self.etiqueta_historial.pack(pady=5)
        self.lista_historial = tk.Listbox(self.marco_historial, font=("Arial", 12), height=15, width=25)
        self.lista_historial.pack(padx=5, pady=5, fill=tk.BOTH)

        # ================= BOTONES  =================
        botones = [
            ("M+", 1, 0), ("M-", 1, 1), ("MR", 1, 2), ("MC", 1, 3), ("B", 1, 4),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("CA", 2, 3), ("C", 2, 4),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("x", 3, 3), ("÷", 3, 4),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3), ("-", 4, 4),
            ("0", 5, 0), ("•", 5, 1), ("%", 5, 2), ("=", 5, 3), ("H", 5, 4)
        ]

        for (texto, fila, columna) in botones:
            boton = tk.Button(marco_principal, text=texto, width=6, height=2, font=("Arial", 14),
                              command=lambda t=texto: self.boton_presionado(t))
            boton.grid(row=fila, column=columna, padx=2, pady=2, sticky="nsew")
            
            if texto == "MR":
                self.boton_mr = boton
                self.color_boton_defecto = self.boton_mr.cget("background")

    # ================= EVENTOS DE BOTONES =================
    def boton_presionado(self, valor):
        if valor == "C":
            self.operacion_actual = ""
            self.actualizar_pantalla()
        elif valor == "CA":
            self.operacion_actual = ""
            self.lista_historial.delete(0, tk.END)
            self.actualizar_pantalla()
        elif valor == "H":
            self.mostrar_ocultar_historial()
        elif valor == "=":
            self.realizar_calculo()
        elif valor == "B":
            self.borrar_ultimo_caracter()
        elif valor == "M+":
            self.memoria_operar(sumar=True)
        elif valor == "M-":
            self.memoria_operar(sumar=False)
        elif valor == "MR":
            self.memoria_recuperar()
        elif valor == "MC":
            self.memoria_limpiar()
        # --- CAMBIO PRINCIPAL ---
        elif valor == "•":
            self.agregar_a_operacion('.')
        else: 
            self.agregar_a_operacion(valor)

    # ================= MANEJO DE OPERACION =================
    def agregar_a_operacion(self, valor):
        if "Error" in self.pantalla.get():
            self.operacion_actual = ""
            
        if self.resultado_mostrado:
            if valor in "+-x÷%":
                self.operacion_actual = self.pantalla.get() + valor
            else:
                self.operacion_actual = valor
            self.resultado_mostrado = False
        else:
            if len(self.operacion_actual) >= 15:
                return

            if valor == "%":
                if not self.operacion_actual or not self.operacion_actual[-1].isdigit():
                    return
            if valor == ".":
                partes = self.operacion_actual.replace('+', ' ').replace('-', ' ').replace('x', ' ').replace('÷', ' ').split()
                if partes and '.' in partes[-1]:
                    return

            if valor in "+-x÷":
                if self.operacion_actual and self.operacion_actual[-1] in "+-x÷":
                    self.operacion_actual = self.operacion_actual[:-1] + valor
                    self.actualizar_pantalla()
                    return

            self.operacion_actual += valor
        self.actualizar_pantalla()

    # ================= CALCULO =================
    def realizar_calculo(self):
        if not self.operacion_actual or self.operacion_actual[-1] in "+-x÷":
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, "ERROR: Incompleta")
            return

        try:
            expresion = self.operacion_actual
            resultado = 0

            if '%' in expresion:
                ultimo_operador_pos = -1
                ultimo_operador = None
                for op in ['+', '-', 'x', '÷']:
                    pos = expresion.rfind(op)
                    if pos > ultimo_operador_pos:
                        ultimo_operador_pos = pos
                        ultimo_operador = op
                
                if ultimo_operador and ultimo_operador_pos > 0:
                    base_str = expresion[:ultimo_operador_pos]
                    porcentaje_str = expresion[ultimo_operador_pos+1:-1]
                    
                    base_num = eval(base_str.replace('x', '*').replace('÷', '/'))
                    porcentaje_num = float(porcentaje_str)
                    
                    if ultimo_operador in ['+', '-']:
                        calculo_porcentaje = base_num * (porcentaje_num / 100)
                        resultado = base_num + calculo_porcentaje if ultimo_operador == '+' else base_num - calculo_porcentaje
                    else:
                        resultado = base_num * (porcentaje_num / 100) if ultimo_operador == 'x' else base_num / (porcentaje_num / 100)
                else:
                    numero_str = expresion[:-1]
                    resultado = float(numero_str) / 100
            else:
                operacion_a_evaluar = expresion.replace('x', '*').replace('÷', '/')
                resultado = eval(operacion_a_evaluar)
            
            if isinstance(resultado, float):
                resultado = round(resultado, 4)
            if resultado == int(resultado):
                resultado = int(resultado)

            self.lista_historial.insert(tk.END, f"{self.operacion_actual} = {resultado}")
            self.lista_historial.yview(tk.END)
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, str(resultado))
            self.operacion_actual = str(resultado)
            self.resultado_mostrado = True

        except (ZeroDivisionError, SyntaxError, ValueError):
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, "ERROR")
            self.operacion_actual = ""

    # ================= MANEJO DE MEMORIA =================
    def memoria_operar(self, sumar):
        try:
            valor_en_pantalla = float(self.pantalla.get())
            self.memoria += valor_en_pantalla if sumar else -valor_en_pantalla
            self.operacion_actual = ""
            self.actualizar_pantalla()
            self.actualizar_indicador_memoria()
        except (ValueError, tk.TclError):
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, "Error: Sin número")
            self.operacion_actual = ""

    def memoria_recuperar(self):
        resultado = self.memoria
        if resultado == int(resultado):
            resultado = int(resultado)
        self.operacion_actual = str(resultado)
        self.actualizar_pantalla()

    def memoria_limpiar(self):
        self.memoria = 0.0
        self.actualizar_indicador_memoria()

    def actualizar_indicador_memoria(self):
        if self.memoria != 0:
            self.boton_mr.config(bg="lightgreen")
        else:
            self.boton_mr.config(bg=self.color_boton_defecto)

    # ================= FUNCIONES AUXILIARES =================
    def borrar_ultimo_caracter(self):
        if self.operacion_actual:
            self.operacion_actual = self.operacion_actual[:-1]
            self.actualizar_pantalla()

    def actualizar_pantalla(self):
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(tk.END, self.operacion_actual)

    def mostrar_ocultar_historial(self):
        if self.historial_visible:
            self.marco_historial.pack_forget()
        else:
            self.marco_historial.pack(side=tk.RIGHT, fill=tk.Y)
        self.historial_visible = not self.historial_visible

# ================= MAIN =================
if __name__ == "__main__":
    raiz = tk.Tk()
    app = Calculadora(raiz)
    raiz.mainloop()
