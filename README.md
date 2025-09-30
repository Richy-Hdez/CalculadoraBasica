# 👤 Integrantes
- Contreras Mosco Cristobal  
- Díaz Pérez Diego  
- Hernández Aguirre Ricardo  
- Monroy Muñoz Angel Yael  
- Salazar Rocha Any Jennifer  

---

# 🧮 Calculadora v3.0 con Funciones Avanzadas

Esta es una **calculadora de escritorio** creada en **Python** utilizando la librería **Tkinter**.  
La versión **3.0** es una **evolución completa** que añade **cálculo de porcentajes**, mejora las **funciones de memoria** y presenta una **interfaz rediseñada**, manteniendo un uso **intuitivo** y en **español**.

---

## ✨ Características Principales

### 🔢 Operaciones Avanzadas
- **Operaciones básicas:** Suma (`+`), resta (`-`), multiplicación (`x`) y división (`÷`).  
- **Cálculo de porcentaje (`%`):** Permite realizar cálculos complejos directamente en una operación.  
  - Ejemplo: `200 + 15%` → Presionar `=` → **Resultado automático**.

---

### 🧠 Funciones de Memoria Mejoradas
- **M+** → Suma el número en pantalla a la memoria.  
- **M-** → Resta el número en pantalla de la memoria.  
- **MR** → Recupera (muestra) el valor guardado en la memoria.  
- **MC** → Limpia (borra) el valor guardado en la memoria.  

**Extras:**
- El botón `MR` se ilumina en **verde** cuando hay un valor almacenado.  
- La memoria **no se borra** al usar los botones `C` o `CA`.

---

### 📝 Historial de Operaciones
- Guarda un registro de **todos los cálculos realizados**.  
- El panel del historial se puede **ocultar y mostrar** con el botón `H`.

---

### ⚙️ Soporte para Números Decimales
- Botón de decimal con símbolo **•** para una estética limpia.  
  - Internamente inserta el **`.` estándar** en la operación.  
- Los resultados se redondean a un **máximo de 4 decimales** cuando es necesario.

---

### 🧹 Botones de Control Rápido
- **CA** → Borrar **todo** (pantalla e historial).  
- **C** → Borrar la **operación actual** en pantalla.  
- **B** → Borrar el **último dígito** escrito.

---

### 🛡️ Manejo de Errores Robusto
- Previene la **división entre cero**.  
- No permite **múltiples puntos decimales** en un mismo número.  
- Evita calcular **operaciones incompletas** (ejemplo: `4 + ❌`).  
- Muestra **error genérico** para operaciones mal formadas.  
- Muestra **"Error: Sin número"** si se intenta usar `M+` o `M-` con la pantalla vacía.

---

### 🖥️ Interfaz Limpia y Funcional
- Longitud máxima en pantalla: **15 caracteres**.  
- Los resultados solo muestran decimales cuando es necesario.  
  - Ejemplo: `10` en lugar de `10.0`.

---

## 🖼️ Interfaz y Distribución de Botones

La distribución de botones fue rediseñada en una cuadrícula **6x5** para ofrecer un acceso **más directo y lógico** a todas las funcionalidades:


0 . = +

