# 🧮 Calculadora con Interfaz Gráfica

Esta es una calculadora creada en **Python** utilizando la librería **Tkinter**.  
Incluye las **cuatro operaciones básicas** y varias funciones extra como historial y manejo de errores, diseñada con una **interfaz clara y en español**.

---

## ✨ Características

- Operaciones básicas: **suma (+), resta (-), multiplicación (*), división (/)**  
- Soporte para **números decimales** (máximo 2 decimales)
- **Historial de operaciones** con panel lateral
- Botones para control rápido:
  - `H` → Mostrar/ocultar historial
  - `CA` → Borrar todo (pantalla e historial)
  - `C` → Borrar pantalla actual
  - `B` → Borrar **último dígito** escrito
- Previene errores como:
  - División entre cero → muestra mensaje de error
  - No permite más de un punto decimal en un mismo número
  - No se puede presionar `=` con una operación incompleta (`4 +` ❌)
  - Longitud máxima en pantalla: **12 caracteres**
- Los resultados **solo muestran punto decimal cuando es necesario**:
  - `10` → ✅
  - `10.25` → ✅

---

## 🖼️ Interfaz

Distribución estándar para una calculadora física:

