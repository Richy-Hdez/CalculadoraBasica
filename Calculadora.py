import tkinter as tk

class Calculadora:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Calculadora")
        self.raiz.resizable(False, False)

        # ================= VARIABLES =================
        self.operacion_actual = ""
        self.historial_visible = False  # Oculto al iniciar
        self.resultado_mostrado = False

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

        # ================= BOTONES =================
        botones = [
            ("H", 1, 0), ("CA", 1, 1), ("C", 1, 2), ("B", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3)
        ]

        for (texto, fila, columna) in botones:
            tk.Button(marco_principal, text=texto, width=6, height=2, font=("Arial", 14),
                      command=lambda t=texto: self.boton_presionado(t)).grid(row=fila, column=columna, padx=2, pady=2)

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
        else:
            self.agregar_a_operacion(valor)

    # ================= MANEJO DE OPERACION =================
    def agregar_a_operacion(self, valor):
        if self.resultado_mostrado:
            if valor in "+-*/":
                self.operacion_actual = self.pantalla.get() + valor
            else:
                self.operacion_actual = valor
            self.resultado_mostrado = False
        else:
            # Limite de caracteres en pantalla
            if len(self.operacion_actual) >= 12:
                return

            # Evitar dos puntos decimales en el mismo numero
            if valor == ".":
                partes = self.operacion_actual.split(" ")[-1] if self.operacion_actual else self.operacion_actual
                if "." in partes:
                    return

            # Evitar operadores consecutivos, reemplazando el anterior
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
            
            # Mostrar sin decimales si es entero
            if resultado == int(resultado):
                resultado = int(resultado)

            # Actualizar historial
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
    raiz = tk.Tk()
    app = Calculadora(raiz)
    raiz.mainloop()
