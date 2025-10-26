# Sistema de Calificación Automatizada con NBGrader

Sistema **completamente dinámico y configurable** para calificar notebooks de Jupyter usando NBGrader en Google Colab.

## ⭐ Características Principales

🎯 **100% Dinámico** - Configura cualquier curso, assignment y estudiantes
📊 **Carga desde CSV** - Lista de estudiantes desde archivo editable
⚡ **Configuración automática** - Genera `nbgrader_config.py` automáticamente
✅ **Validación inteligente** - Detecta errores en nombres y configuración
📈 **Reportes completos** - Estadísticas y resúmenes detallados
🛠️ **Utilidades integradas** - Mantenimiento y limpieza de archivos

## 📋 Tabla de Contenidos

- [Inicio Rápido](#inicio-rápido)
- [Configuración Dinámica](#configuración-dinámica)
- [Descripción General](#descripción-general)
- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Guía de Uso Paso a Paso](#guía-de-uso-paso-a-paso)
- [Workflow Completo](#workflow-completo)
- [Archivos Importantes](#archivos-importantes)
- [Troubleshooting](#troubleshooting)
- [Preguntas Frecuentes](#preguntas-frecuentes)

---

## 🚀 Inicio Rápido

1. Abre `nbgrader_optimizado.ipynb` en Google Colab
2. Ejecuta las celdas en orden
3. Ingresa cuando se pida:
   - **Base Path** - Carpeta principal (ej: `/content/drive/MyDrive/nbgrader`)
   - **Course ID** - Nombre del curso (ej: `Python_2024`)
   - **Assignment ID** - ID de la tarea (ej: `Tarea1`)
   - **Timeout** - Presiona ENTER para usar 180s
4. Sube el CSV con estudiantes
5. ¡Listo! El sistema está configurado

> Se creará automáticamente: `{BASE_PATH}/{COURSE_ID}/`

---

## ⚙️ Configuración Dinámica

### El sistema te pedirá:

| Parámetro | Ejemplo | Descripción |
|-----------|---------|-------------|
| **Base Path** | `/content/drive/MyDrive/nbgrader` | Carpeta principal para **TODOS** tus cursos |
| **Course ID** | `Python_AP` | Identificador del curso (se crea como subcarpeta) |
| **Assignment ID** | `S01_D02_A02` | Identificador de la tarea |
| **Timeout** | `180` | Segundos máximo de ejecución |
| **CSV Estudiantes** | `estudiantes.csv` | Archivo con lista de estudiantes |

### Estructura resultante:

```
BASE_PATH/                           # ej: /content/drive/MyDrive/nbgrader
└── COURSE_ID/                       # ej: Python_AP
    ├── source/                      # Notebooks maestros
    ├── release/                     # Para estudiantes
    ├── submitted/                   # Entregas
    ├── autograded/                  # Calificados
    └── feedback/                    # Feedback HTML
```

### Ventajas:

✅ **Sin hardcodeo** - No hay valores fijos en el código
✅ **Reutilizable** - Mismo notebook para todos tus cursos
✅ **Múltiples cursos** - Todos organizados en un solo lugar
✅ **Flexible** - Cambia parámetros en cada ejecución
✅ **Validado** - Verifica que los valores sean correctos

---

## 📖 Descripción General

Este sistema permite automatizar la calificación de tareas (assignments) de Jupyter Notebook usando **NBGrader**, con las siguientes características:

✅ **Configuración dinámica** - Cualquier curso, assignment y estudiantes
✅ **Carga desde CSV** - Lista de estudiantes desde archivo editable
✅ **Generación automática de config** - Crea `nbgrader_config.py` con tus valores
✅ **Calificación masiva** - Califica todos los estudiantes automáticamente
✅ **Feedback en HTML** - Genera feedback personalizado para cada estudiante
✅ **Export a CSV** - Exporta calificaciones listas para importar
✅ **Validación inteligente** - Detecta nombres con acentos y errores
✅ **Reportes detallados** - Estadísticas y resúmenes de calificación
✅ **Utilidades de mantenimiento** - Limpieza y gestión de archivos

---

## 🔧 Requisitos Previos

### Software
- Google Colab (recomendado) o Jupyter Notebook
- Google Drive (para almacenamiento persistente)
- Python 3.8+

### Dependencias
- `nbgrader==0.8.1`
- `nbclient==0.6.1`
- `pandas`
- `jupyter`

> ⚠️ **Importante:** Las versiones específicas de nbgrader y nbclient son necesarias para evitar incompatibilidades.

---

## 🚀 Instalación y Configuración

### Paso 1: Configurar el entorno

1. Abre `nbgrader_optimizado.ipynb` en Google Colab
2. Las celdas iniciales instalarán automáticamente:
   - `nbclient==0.6.1`
   - `nbgrader==0.8.1`

### Paso 2: Configuración dinámica

El notebook te pedirá los siguientes valores **en este orden**:

1. **Base Path** - Carpeta principal para TODOS tus cursos
   - Ej: `/content/drive/MyDrive/nbgrader`
   - Ej: `/content/drive/MyDrive/Cursos`

2. **Course ID** - Nombre del curso (se crea dentro de Base Path)
   - Ej: `Python_2024`, `DataScience_101`
   - Se creará: `{BASE_PATH}/Python_2024/`

3. **Assignment ID** - Nombre de la tarea
   - Ej: `Tarea1`, `Parcial_Final`, `S01_D02_A02`

4. **Timeout** - Segundos máximos de ejecución (default: 180)

**El sistema automáticamente:**
- Construye la ruta completa: `{BASE_PATH}/{COURSE_ID}/`
- Genera `nbgrader_config.py` con tu configuración
- Crea la estructura de directorios
- Valida que los valores sean correctos

### Paso 3: Estructura de directorios (generada automáticamente)

El sistema creará automáticamente esta estructura:

```
{BASE_PATH}/                       # Ej: /content/drive/MyDrive/nbgrader
└── {COURSE_ID}/                   # Ej: Python_2024
    ├── source/                    # Notebooks maestros del instructor
    │   └── {ASSIGNMENT_ID}/
    │       └── {ASSIGNMENT_ID}.ipynb
    ├── release/                   # Versión para estudiantes (auto-generada)
    │   └── {ASSIGNMENT_ID}/
    │       └── {ASSIGNMENT_ID}.ipynb
    ├── submitted/                 # Submissions de estudiantes
    │   ├── {Estudiante1}/
    │   │   └── {ASSIGNMENT_ID}/
    │   │       └── {ASSIGNMENT_ID}.ipynb
    │   └── {Estudiante2}/
    │       └── {ASSIGNMENT_ID}/
    │           └── {ASSIGNMENT_ID}.ipynb
    ├── autograded/                # Notebooks calificados (auto-generado)
    │   ├── {Estudiante1}/
    │   └── {Estudiante2}/
    └── feedback/                  # Feedback en HTML (auto-generado)
        ├── {Estudiante1}/
        └── {Estudiante2}/
```

**Ejemplo concreto:**
```
/content/drive/MyDrive/nbgrader/
├── Python_2024/
│   ├── source/
│   ├── release/
│   └── ...
├── DataScience_2024/
│   ├── source/
│   ├── release/
│   └── ...
└── MachineLearning_2024/
    ├── source/
    ├── release/
    └── ...
```

> ✅ **Ventaja:** Todos tus cursos organizados en un solo lugar

### Paso 4: Configurar `nbgrader_config.py`

**No necesitas editarlo manualmente.** El notebook genera automáticamente este archivo con tus valores:

```python
c.CourseDirectory.root = '{TU_BASE_PATH}'
c.Execute.timeout = {TU_TIMEOUT}
# ... y todas las demás configuraciones
```

> ✅ El archivo `nbgrader_config.py` incluido en el repo es solo un template de referencia

---

## 📁 Estructura del Proyecto

### Archivos Principales

| Archivo | Descripción |
|---------|-------------|
| `nbgrader_optimizado.ipynb` | **Notebook principal optimizado** - Úsalo para todo el workflow |
| `estudiantes.csv` | Template del CSV con lista de estudiantes |
| `nbgrader_config.py` | Configuración de NBGrader |
| `README.md` | Esta documentación |
| `nbgrader_ap_001.ipynb` | Notebook original (mantenido por compatibilidad) |

### Formato del CSV de Estudiantes

El archivo `estudiantes.csv` debe tener el siguiente formato:

```csv
nombre_estudiante
Acosta_Zavaleta_Jose_Manuel
Alza_Guzman_Andrea_Coral
Asencios_Clavijo_Gabriela_Shumey
```

⚠️ **Reglas importantes:**
- Primera línea debe ser el header: `nombre_estudiante`
- **NO usar acentos** (ej: `Martinez` en lugar de `Martínez`)
- **NO usar caracteres especiales** (solo letras, números y guiones bajos)
- Formato recomendado: `Apellido1_Apellido2_Nombre1_Nombre2`

---

## 📘 Guía de Uso Paso a Paso

### 1️⃣ Preparar el Assignment (Instructor)

1. Crea tu notebook con ejercicios en Jupyter
2. Marca las celdas con los metadatos de NBGrader:
   - **Grade cells:** Celdas con tests que se califican automáticamente
   - **Solution cells:** Celdas donde los estudiantes escriben código
   - **Read-only cells:** Celdas que no pueden modificar

3. Ejemplo de metadatos para una celda de test:

```json
{
  "nbgrader": {
    "grade": true,
    "grade_id": "test_cell_1",
    "locked": true,
    "points": 10,
    "schema_version": 3,
    "solution": false,
    "task": false
  }
}
```

4. Guarda el notebook como: `source/{ASSIGNMENT_ID}/{ASSIGNMENT_ID}.ipynb`

#### 🔒 Ocultar Tests a los Estudiantes

**⚠️ CRÍTICO:** Para que los estudiantes NO vean el código de los tests en el feedback HTML, debes configurar CORRECTAMENTE los metadatos ANTES de generar el assignment.

**❌ Problema común:** Las celdas de test aparecen visibles en el feedback y los estudiantes pueden copiar las respuestas.

**✅ Solución:** Marcar las celdas de test con `"locked": true` en los metadatos.

---

**MÉTODO RECOMENDADO: Marcar toda la celda como Grade Cell bloqueada**

**1. En el notebook fuente, cada celda de test debe tener estos metadatos:**

```json
{
  "nbgrader": {
    "grade": true,
    "grade_id": "test_suma",
    "locked": true,         ← CRÍTICO: Debe ser true
    "points": 10,
    "schema_version": 3,
    "solution": false,
    "task": false
  }
}
```

**2. Cómo editar metadatos en Jupyter:**

1. Abre el notebook fuente en Jupyter Notebook (NO en Colab)
2. Selecciona la celda de test
3. Click: `View` → `Cell Toolbar` → `Edit Metadata`
4. Click en `Edit Metadata` en la celda
5. Edita el JSON y asegúrate de tener `"locked": true`
6. Guarda los cambios

**3. Verificar ANTES de generar el assignment:**

El notebook optimizado incluye una **celda de verificación (Celda 8.1)** que revisa automáticamente si las celdas están correctamente configuradas:

```python
# Ejecuta la celda 8.1 para verificar
# Te mostrará:
# ✅ Celdas correctamente bloqueadas
# ❌ Celdas con problemas (te dirá cuáles arreglar)
```

**4. Resultado esperado:**

**Con `locked: true`:**
- ✅ Los estudiantes NO verán el código del test
- ✅ Solo verán: "Test test_suma: PASSED (10/10 points)" o "FAILED (0/10 points)"
- ✅ Verán los puntos obtenidos pero no cómo se calculan

**Sin `locked: true`:**
- ❌ Los estudiantes VERÁN todo el código: `assert suma(2,3) == 5`
- ❌ Pueden copiar las respuestas directamente
- ❌ La evaluación no tiene sentido

---

**MÉTODO ALTERNATIVO: Usar delimitadores para tests parcialmente ocultos**

Si quieres mostrar ALGUNOS tests pero ocultar otros:

```python
# Tests visibles (los estudiantes verán estos)
assert resultado > 0, "El resultado debe ser positivo"

# BEGIN HIDDEN TESTS
# Tests ocultos - SOLO estos se ocultan
assert resultado == 42, "Valor específico incorrecto"
assert type(resultado) == int, "Tipo de dato incorrecto"
# END HIDDEN TESTS
```

**IMPORTANTE:** Aún así la celda debe tener `"locked": true` para que funcione correctamente.

---

**⚠️ Advertencias:**

1. **Google Colab no permite editar metadatos fácilmente** - Usa Jupyter local para crear el assignment
2. **Verifica SIEMPRE con la celda 8.1** antes de generar el assignment
3. **Si ya generaste el assignment sin `locked: true`**, debes:
   - Corregir los metadatos en el notebook fuente
   - Re-ejecutar la celda 19 (Generar Assignment)
   - Re-distribuir el notebook a los estudiantes

**⚠️ Importante:**
- Los delimitadores `BEGIN HIDDEN TESTS` y `END HIDDEN TESTS` deben estar en **comentarios**
- Todo el código entre estos delimitadores se elimina antes de generar el feedback
- Usa la Opción 1 si quieres ocultar TODO el test (más simple)

### 2️⃣ Preparar Lista de Estudiantes

**Opción A: Usar CSV (Recomendado)**

1. Edita `estudiantes.csv` con tus estudiantes
2. Asegúrate de que no haya acentos
3. El notebook cargará automáticamente este archivo

**Opción B: Lista manual**

Descomenta la celda en el notebook y edita:

```python
estudiantes = [
    'Estudiante_Uno',
    'Estudiante_Dos',
    'Estudiante_Tres'
]
```

### 3️⃣ Generar Assignment para Estudiantes

Ejecuta la celda de "Generar Assignment" en el notebook:

```python
!nbgrader generate_assignment --assignment_id='S01_D02_A02' --debug
```

Esto creará el archivo para estudiantes en: `release/S01_D02_A02/S01_D02_A02.ipynb`

**El sistema automáticamente:**
- Elimina las soluciones
- Bloquea las celdas de test
- Agrega stubs de código (ej: `# YOUR CODE HERE`)
- Calcula checksums para prevenir modificaciones

### 4️⃣ Distribuir a Estudiantes

1. Descarga el archivo de: `release/S01_D02_A02/S01_D02_A02.ipynb`
2. Compártelo con tus estudiantes (ej: Google Drive, Moodle, email)
3. Los estudiantes completan el assignment

### 5️⃣ Recolectar Submissions

Los estudiantes deben subir sus notebooks completados a:

```
submitted/{nombre_estudiante}/S01_D02_A02/S01_D02_A02.ipynb
```

> 💡 **Tip:** Puedes compartir un link de carpeta de Google Drive donde cada estudiante tenga su subcarpeta

### 6️⃣ Calificar Automáticamente

Ejecuta la celda de "Autograding Masivo":

```python
# El notebook tiene un loop que califica a todos
for estudiante in estudiantes:
    !nbgrader autograde --student {estudiante} S01_D02_A02 --debug
```

**El sistema:**
- Ejecuta todos los notebooks
- Corre los tests automáticos
- Calcula las calificaciones
- Guarda resultados en la base de datos
- Genera un reporte de éxitos y errores

### 7️⃣ Generar Feedback

Ejecuta la celda de "Generar Feedback":

```python
!nbgrader feedback --assignment S01_D02_A02 --debug
```

Esto crea archivos HTML en: `feedback/{estudiante}/S01_D02_A02/`

### 8️⃣ Exportar Calificaciones

Ejecuta la celda de "Exportar Notas":

```python
!nbgrader export --to notas_S01_D02_A02.csv
```

El CSV contendrá todas las calificaciones listas para importar a tu sistema de gestión.

---

## 🔄 Workflow Completo

```
┌─────────────────────────────────────────┐
│  1. Crear Assignment Maestro            │
│     (source/S01_D02_A02/)               │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│  2. Cargar Lista de Estudiantes         │
│     (desde CSV o manual)                │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│  3. Generar Assignment                  │
│     nbgrader generate_assignment        │
│     → release/S01_D02_A02/              │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│  4. Distribuir a Estudiantes            │
│     (Google Drive, Moodle, etc)         │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│  5. Estudiantes Completan Tareas        │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│  6. Recolectar Submissions              │
│     submitted/{estudiante}/S01_D02_A02/ │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│  7. Autograding Masivo                  │
│     nbgrader autograde (loop)           │
│     → autograded/                       │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│  8. Generar Feedback                    │
│     nbgrader feedback                   │
│     → feedback/ (HTML)                  │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│  9. Exportar Calificaciones             │
│     nbgrader export → CSV               │
└─────────────────────────────────────────┘
```

---

## 📄 Archivos Importantes

### `nbgrader_config.py`

Configuración principal del sistema. Ajusta según tu entorno:

```python
# Directorio raíz del curso
c.CourseDirectory.root = '/content/drive/MyDrive/nbgrader_PAGD1_14123'

# ID del curso
c.CourseDirectory.course_id = 'Python_AP'

# Opciones recomendadas para Google Colab
c.Execute.timeout = 180  # Timeout de ejecución (segundos)
c.ClearHiddenTests.enforce_metadata = False  # Permitir tests ocultos
```

### `estudiantes.csv`

Template para la lista de estudiantes:

```csv
nombre_estudiante
Estudiante_Uno
Estudiante_Dos
```

### `nbgrader_optimizado.ipynb`

Notebook principal con todas las funcionalidades integradas.

---

## 🛠️ Troubleshooting

### Problema: "No nbgrader_config.py file found"

**Síntoma:** Warning al ejecutar comandos de nbgrader: `[WARNING] No nbgrader_config.py file found`

**⚠️ IMPORTANTE:** Este warning es **INFORMATIVO** y generalmente **NO impide** que nbgrader funcione.

---

**¿Por qué aparece?**

NBGrader busca `nbgrader_config.py` en múltiples ubicaciones. Cuando no lo encuentra en todas, muestra el warning, **PERO** sigue usando la configuración definida en el código.

**¿Es realmente un problema?**

**❌ SÍ es problema si:**
- Los comandos de nbgrader **fallan** después del warning
- No se crean archivos en los directorios esperados

**✅ NO es problema si:**
- Los comandos de nbgrader **completan exitosamente**
- Se crean archivos correctamente
- El sistema funciona como se espera

**En la mayoría de casos, puedes IGNORAR este warning con seguridad.**

---

**Verificación rápida:**

Ejecuta la **celda 4.1** (Diagnóstico de nbgrader_config.py) para ver si el archivo existe:

```
✅ EXISTE - /content/nbgrader_config.py
✅ EXISTE - {BASE_PATH}/nbgrader_config.py
```

**Si ambos dicen "✅ EXISTE":**
- 👍 Todo está correcto
- 👍 El warning es solo informativo
- 👍 Puedes ignorarlo con seguridad

**Si dice "❌ NO EXISTE":**
- ⚠️ Re-ejecuta la **celda 4** para regenerar el archivo

---

**Solución automática (YA IMPLEMENTADA):**

El notebook **ya maneja esto automáticamente**:
1. La celda 4 genera el archivo en dos ubicaciones
2. Todas las celdas cambian al directorio correcto antes de ejecutar
3. La celda 4.1 te permite verificar si todo está bien

**Resumen:**
| Situación | Acción |
|-----------|--------|
| Warning + comando funciona | Ignorar |
| Warning + comando falla | Re-ejecutar celda 4 |
| Archivo existe en BASE_PATH | Todo bien |

### Problema: "El feedback no se genera para algunos estudiantes"

**Causa común:** Nombres con acentos o caracteres especiales

**Solución:**
1. Revisa `estudiantes.csv`
2. Elimina todos los acentos: `Martínez` → `Martinez`
3. Usa solo letras, números y guiones bajos
4. Ejecuta la validación en el notebook (celda de carga de CSV)

### Problema: "Error al calificar: NotebookClient timeout"

**Causa:** El código del estudiante toma mucho tiempo o tiene un loop infinito

**Solución:**
1. Aumenta el timeout en `nbgrader_config.py`:

```python
c.Execute.timeout = 300  # 5 minutos
```

2. Revisa manualmente el notebook del estudiante

### Problema: "Carpeta 'submitted' vacía"

**Solución:**
1. Verifica que ejecutaste la celda "Crear Carpetas de Estudiantes"
2. Confirma que los estudiantes subieron sus notebooks a la ubicación correcta
3. Usa la celda "Ver Estadísticas" para verificar el estado

### Problema: "Se tiene que reiniciar sesión"

**Causa:** Cambios en los archivos de Google Drive no se reflejan

**Solución:**
1. En Google Colab: Runtime → Restart Runtime
2. Re-ejecuta las celdas necesarias

### Problema: "AttributeError: module has no attribute"

**Causa:** Incompatibilidad de versiones de nbgrader/nbclient

**Solución:**
1. Reinstala las versiones exactas:

```python
!pip install --force-reinstall nbclient==0.6.1
!pip install --force-reinstall nbgrader==0.8.1
```

2. Reinicia el runtime

### Problema: "Los puntajes exportados muestran 0 aunque los estudiantes hicieron bien el assignment"

**Síntoma:** El CSV exportado muestra `score=0` para todos o algunos estudiantes, pero tú sabes que completaron el assignment correctamente.

**Causas comunes:**
1. El autograding no se ejecutó correctamente
2. La base de datos de nbgrader no se actualizó
3. Las celdas de test no tienen puntos asignados
4. El comando export leyó una base de datos antigua

**Soluciones:**

1. **Verificar la base de datos:**
   ```python
   !nbgrader db assignment list
   ```
   Si no ves tu assignment o muestra puntajes 0, hay un problema con el autograding.

2. **Re-ejecutar el autograding con --force:**

   Usa la **celda 11.1 "Diagnóstico y Corrección de Puntajes"** del notebook optimizado, que incluye:
   - Verificación de la base de datos
   - Re-autograding con debug para detectar errores
   - Herramientas para diagnosticar problemas específicos

   O manualmente:
   ```python
   !nbgrader autograde '{ASSIGNMENT_ID}' --student '{estudiante}' --force --debug
   ```

3. **Verificar que las celdas de test tienen puntos:**

   Abre el notebook source y verifica que cada celda de test tenga:
   ```json
   {
     "nbgrader": {
       "grade": true,
       "points": 10,  // ← ESTO DEBE ESTAR CONFIGURADO
       "locked": true
     }
   }
   ```

4. **Limpiar y empezar de nuevo:**

   Si nada funciona, limpia la base de datos y re-autograde:
   ```python
   # Eliminar base de datos
   import os
   db_path = os.path.join(BASE_PATH, 'gradebook.db')
   if os.path.exists(db_path):
       os.remove(db_path)

   # Re-ejecutar celda 22 (Autograding Masivo)
   # Re-ejecutar celda 26 (Exportar Notas)
   ```

5. **Verificar archivos autograded:**

   Asegúrate de que existen notebooks en `autograded/{estudiante}/{ASSIGNMENT_ID}/`:
   ```python
   !ls -la {DIRS['autograded']}/{estudiante}/{ASSIGNMENT_ID}/
   ```

**Prevención:**
- Siempre verifica la salida de la celda 22 (Autograding) para confirmar que no hubo errores
- Usa la verificación de base de datos integrada en la celda 26 (Export)
- Ejecuta la celda 11.1 de diagnóstico si ves advertencias de puntajes en 0

---

## ❓ Preguntas Frecuentes

### ¿Puedo usar esto en Jupyter local en lugar de Google Colab?

Sí, pero necesitas:
1. Ajustar las rutas en `nbgrader_config.py`
2. Cambiar la lógica de montaje de Google Drive
3. Asegurar que tienes las dependencias instaladas

### ¿Cómo agrego calificación manual?

Después del autograding:
1. Abre los notebooks en `autograded/{estudiante}/`
2. Usa la interfaz de NBGrader para calificar manualmente
3. O edita directamente la base de datos SQLite (`gradebook.db`)

### ¿Puedo tener múltiples assignments?

Sí, solo cambia la variable `ASSIGNMENT_ID` en el notebook:

```python
ASSIGNMENT_ID = 'S01_D02_A03'  # Nuevo assignment
```

Cada assignment tiene su propia carpeta en `source/`, `release/`, etc.

### ¿Cómo elimino un estudiante de la base de datos?

Usa la celda de utilidades:

```python
!nbgrader db student remove {nombre_estudiante} --assignment {ASSIGNMENT_ID} --force
```

### ¿Dónde está la base de datos de calificaciones?

En: `{BASE_PATH}/gradebook.db` (archivo SQLite)

### ¿Puedo personalizar el mensaje "YOUR CODE HERE"?

Sí, en `nbgrader_config.py`:

```python
c.ClearSolutions.code_stub = {
    'python': '# ESCRIBE TU CÓDIGO AQUÍ\nraise NotImplementedError()'
}
```

### ¿Cómo evito que los estudiantes modifiquen las celdas de test?

Las celdas de test deben tener `"locked": true` en los metadatos. Esto se hace automáticamente con `nbgrader generate_assignment`.

### ¿El sistema funciona con otros lenguajes además de Python?

Sí, NBGrader soporta:
- Python
- R
- Julia
- Matlab/Octave
- Java
- SAS

Ajusta `code_stub` en la configuración para cada lenguaje.

---

## 📚 Recursos Adicionales

- [Documentación oficial de NBGrader](https://nbgrader.readthedocs.io/)
- [Tutorial de NBGrader](https://nbgrader.readthedocs.io/en/stable/user_guide/creating_and_grading_assignments.html)
- [Metadatos de celdas](https://nbgrader.readthedocs.io/en/stable/user_guide/creating_and_grading_assignments.html#autograded-answer-cells)

---

## 🤝 Contribuciones

Para reportar problemas o sugerir mejoras:
1. Abre un issue en GitHub
2. Describe el problema detalladamente
3. Incluye logs y versiones de dependencias

---

## 📝 Licencia

Este proyecto está bajo la licencia especificada por el curso Python_AP.

---

## 📞 Contacto

Para soporte técnico, contacta al equipo de instructores del curso.

---

**Última actualización:** Octubre 2025
**Versión:** 2.0 (Optimizada con carga CSV)
