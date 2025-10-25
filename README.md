# Sistema de Calificación Automatizada con NBGrader

Sistema automatizado para calificar notebooks de Jupyter usando NBGrader en Google Colab.

## 📋 Tabla de Contenidos

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

## 📖 Descripción General

Este sistema permite automatizar la calificación de tareas (assignments) de Jupyter Notebook usando **NBGrader**, con las siguientes características:

✅ Carga de estudiantes desde archivo CSV
✅ Calificación masiva automatizada
✅ Generación automática de feedback en HTML
✅ Exportación de calificaciones a CSV
✅ Validación de nombres (sin acentos)
✅ Reportes de errores y estadísticas
✅ Utilidades de mantenimiento integradas

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

### Paso 2: Estructura de directorios

El sistema creará automáticamente la siguiente estructura en Google Drive:

```
/content/drive/MyDrive/nbgrader_PAGD1_14123/
├── source/              # Notebooks maestros del instructor
│   └── S01_D02_A02/
│       └── S01_D02_A02.ipynb
├── release/             # Versión para estudiantes (auto-generada)
│   └── S01_D02_A02/
│       └── S01_D02_A02.ipynb
├── submitted/           # Submissions de estudiantes
│   ├── Estudiante1/
│   │   └── S01_D02_A02/
│   │       └── S01_D02_A02.ipynb
│   └── Estudiante2/
│       └── S01_D02_A02/
│           └── S01_D02_A02.ipynb
├── autograded/          # Notebooks calificados (auto-generado)
│   ├── Estudiante1/
│   └── Estudiante2/
└── feedback/            # Feedback en HTML (auto-generado)
    ├── Estudiante1/
    └── Estudiante2/
```

### Paso 3: Configurar `nbgrader_config.py`

El archivo de configuración debe estar en `/content/` con:

```python
c.CourseDirectory.root = '/content/drive/MyDrive/nbgrader_PAGD1_14123'
c.CourseDirectory.course_id = 'Python_AP'
```

> ✅ Este archivo ya está incluido en el repositorio

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

4. Guarda el notebook como: `source/S01_D02_A02/S01_D02_A02.ipynb`

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

**Solución:**
1. Verifica que `nbgrader_config.py` esté en `/content/`
2. Copia el archivo de configuración a la ubicación correcta:

```python
!cp /content/drive/MyDrive/tu_carpeta/nbgrader_config.py /content/
```

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
