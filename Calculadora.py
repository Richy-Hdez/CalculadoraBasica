import tkinter as tk

class Calculadora:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Calculadora 2.0")
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
        self.pantalla.grid(row=0, column=0, columnspan=4, pady=5)

        # ================= HISTORIAL =================
        self.marco_historial = tk.Frame(self.raiz, bg="#f0f0f0", width=200)
        self.etiqueta_historial = tk.Label(self.marco_historial, text="Historial", font=("Arial", 14, "bold"), bg="#f0f0f0")
        self.etiqueta_historial.pack(pady=5)
        self.lista_historial = tk.Listbox(self.marco_historial, font=("Arial", 12), height=15, width=25)
        self.lista_historial.pack(padx=5, pady=5, fill=tk.BOTH)

        # ================= BOTONES (Nueva distribución) =================
        botones = [
            ("M+", 1, 0), ("M-", 1, 1), ("M", 1, 2), ("MR", 1, 3),
            ("H", 2, 0), ("CA", 2, 1), ("C", 2, 2), ("B", 2, 3),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("/", 3, 3),
            ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("*", 4, 3),
            ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("-", 5, 3),
            ("0", 6, 0), (".", 6, 1), ("=", 6, 2), ("+", 6, 3)
        ]

        for (texto, fila, columna) in botones:
            boton = tk.Button(marco_principal, text=texto, width=6, height=2, font=("Arial", 14),
                              command=lambda t=texto: self.boton_presionado(t))
            boton.grid(row=fila, column=columna, padx=2, pady=2)
            
            
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
        elif valor == "M":
            self.memoria_limpiar()
        else:
            self.agregar_a_operacion(valor)

    # ================= MANEJO DE MEMORIA (Nuevas funciones) =================
    def memoria_operar(self, sumar):
        try:
            valor_en_pantalla = float(self.pantalla.get())
            if sumar:
                self.memoria += valor_en_pantalla
            else:
                self.memoria -= valor_en_pantalla
            
            self.operacion_actual = "" 
            self.actualizar_pantalla()
            self.actualizar_indicador_memoria()
        except (ValueError, TclError):
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

    # ================= MANEJO DE OPERACION =================
    def agregar_a_operacion(self, valor):
        if "Error" in self.pantalla.get():
            self.operacion_actual = ""
            
        if self.resultado_mostrado:
            if valor in "+-*/":
                self.operacion_actual = self.pantalla.get() + valor
            else:
                self.operacion_actual = valor
            self.resultado_mostrado = False
        else:
            if len(self.operacion_actual) >= 12:
                return

            if valor == ".":
                partes = self.operacion_actual.split(" ")[-1] if self.operacion_actual else self.operacion_actual
                if "." in partes:
                    return

            if valor in "+-*/":
                if self.operacion_actual and self.operacion_actual[-1] in "+-*/":
                    self.operacion_actual = self.operacion_actual[:-1] + valor
                    self.actualizar_pantalla()
                    return

            self.operacion_actual += valor
        self.actualizar_pantalla()

    # ================= CALCULO =================
    def realizar_calculo(self):
        if not self.operacion_actual or self.operacion_actual[-1] in "+-*/":
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, "ERROR: Incompleta")
            self.operacion_actual = ""
            return

        try:
            resultado = eval(self.operacion_actual)
            if isinstance(resultado, float):
                resultado = round(resultado, 2)
            
            if resultado == int(resultado):
                resultado = int(resultado)

            self.lista_historial.insert(tk.END, f"{self.operacion_actual} = {resultado}")
            self.lista_historial.yview(tk.END)

            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, resultado)

            self.operacion_actual = str(resultado)
            self.resultado_mostrado = True

        except ZeroDivisionError:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, "ERROR: ÷0")
            self.operacion_actual = ""
        except:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, "ERROR")
            self.operacion_actual = ""

    # ================= BORRAR ULTIMO CARACTER =================
    def borrar_ultimo_caracter(self):
        if self.operacion_actual:
            self.operacion_actual = self.operacion_actual[:-1]
            self.actualizar_pantalla()

    # ================= PANTALLA =================
    def actualizar_pantalla(self):
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(tk.END, self.operacion_actual)

    # ================= MOSTRAR/OCULTAR HISTORIAL =================
    def mostrar_ocultar_historial(self):
        if self.historial_visible:
            self.marco_historial.pack_forget()
            self.historial_visible = False
        else:
            self.marco_historial.pack(side=tk.RIGHT, fill=tk.Y)
            self.historial_visible = True

# ================= MAIN =================
if __name__ == "__main__":
    from tkinter import TclError
    raiz = tk.Tk()
    app = Calculadora(raiz)
    raiz.mainloop()
