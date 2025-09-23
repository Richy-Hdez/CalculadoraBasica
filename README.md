# 👤Integrantes
●	Contreras Mosco Cristobal

●	Díaz Pérez Diego

●	Hernández Aguirre Ricardo

●	Monroy Muñoz Angel Yael

●	Salazar Rocha Any Jennifer



# 🧮 Calculadora v2.0 con Memoria e Interfaz Gráfica

Esta es una calculadora de escritorio creada en **Python** utilizando la librería **Tkinter**.  
La versión **2.0** expande las funcionalidades básicas para incluir **operaciones de memoria** (`M+`, `M-`, `MR`), manteniendo una interfaz clara, intuitiva y en **español**.

---

## ✨ Características Principales

### 🔢 Operaciones básicas
- Suma (`+`), resta (`-`), multiplicación (`*`) y división (`/`).

### 🧠 Funciones de Memoria Independientes
- **M+** → Suma el número en pantalla a la memoria.  
- **M-** → Resta el número en pantalla de la memoria.  
- **MR** → Recupera (muestra) el valor de la memoria en pantalla.  
- **M** → Limpia (borra) el valor guardado en la memoria.

**Extras:**
- El botón `MR` se ilumina en **verde** cuando hay un valor almacenado.  
- La memoria **no se borra** al usar los botones `C` o `CA`.

### 📝 Historial de Operaciones
- Guarda un registro de **todos los cálculos realizados**.
- El panel del historial se puede **ocultar y mostrar** con el botón `H`.

### ⚙️ Soporte para Números Decimales
- Permite la entrada de **números decimales**.
- Los resultados se redondean a un **máximo de 2 decimales**, solo cuando es necesario.

### 🧹 Botones de Control Rápido
- **CA** → Borrar **todo** (pantalla e historial).  
- **C** → Borrar la **operación actual** en pantalla.  
- **B** → Borrar el **último dígito** escrito.

### 🛡️ Manejo de Errores Mejorado
- Previene la **división entre cero**.  
- No permite **más de un punto decimal** en el mismo número.  
- Impide calcular **operaciones incompletas** (ejemplo: `4 + ❌`).  
- Muestra **"Error: Sin número"** si se intenta usar `M+` o `M-` con la pantalla vacía.

### 🖥️ Interfaz Limpia y Funcional
- Longitud máxima en pantalla: **12 caracteres**.  
- Los resultados solo muestran decimales cuando es necesario (ejemplo: `10` en lugar de `10.0`).

---

## 🖼️ Interfaz y Distribución de Botones

La distribución de botones fue actualizada para dar prioridad a las **funciones de memoria**, quedando organizada de la siguiente manera:
M+ M- M MR 
H CA C B 
7 8 9 / 
4 5 6 * 
1 2 3 - 
0 . = +

