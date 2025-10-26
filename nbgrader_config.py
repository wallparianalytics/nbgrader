# ============================================================================
# NBGrader Configuration File - TEMPLATE
# ============================================================================
# NOTA: Este archivo es un TEMPLATE de referencia.
# El notebook 'nbgrader_optimizado.ipynb' genera automáticamente
# la configuración con tus valores específicos.
#
# Si prefieres usar este archivo manualmente, descomenta y edita
# las líneas según tus necesidades.
# ============================================================================

# ----------------------------------------------------------------------------
# CONFIGURACIÓN PRINCIPAL DEL CURSO
# ----------------------------------------------------------------------------

## Directorio raíz donde se encuentran todas las carpetas del curso
## IMPORTANTE: Cambiar según tu configuración
# c.CourseDirectory.root = '/content/drive/MyDrive/nbgrader_TuCurso'

## Identificador del curso (opcional, se puede especificar por línea de comandos)
# c.CourseDirectory.course_id = 'TuCurso'

## ID del assignment (opcional, se puede especificar por línea de comandos)
# c.CourseDirectory.assignment_id = 'Assignment1'

# ----------------------------------------------------------------------------
# EJECUCIÓN Y TIMEOUT
# ----------------------------------------------------------------------------

## Tiempo máximo (en segundos) para ejecutar una celda
## Recomendado: 180 segundos (3 minutos)
## Aumentar si los ejercicios requieren más tiempo de ejecución
c.Execute.timeout = 180

## Archivo de historial de IPython
## ':memory:' es recomendado para Google Colab
c.Execute.ipython_hist_file = ':memory:'

## Grabar timing de ejecución en metadatos
c.Execute.record_timing = True

# ----------------------------------------------------------------------------
# CONFIGURACIÓN DE SOLUCIONES Y TESTS
# ----------------------------------------------------------------------------

## Delimitadores para soluciones en el código
c.ClearSolutions.begin_solution_delimeter = 'BEGIN SOLUTION'
c.ClearSolutions.end_solution_delimeter = 'END SOLUTION'

## Código que reemplaza las soluciones en diferentes lenguajes
c.ClearSolutions.code_stub = {
    'python': '# YOUR CODE HERE\nraise NotImplementedError()',
    'matlab': "% YOUR CODE HERE\nerror('No Answer Given!')",
    'r': '# YOUR CODE HERE\nstop("No Answer Given!")',
    'java': '// YOUR CODE HERE'
}

## Texto para respuestas escritas (markdown)
c.ClearSolutions.text_stub = 'YOUR ANSWER HERE'

## Delimitadores para tests ocultos
c.ClearHiddenTests.begin_test_delimeter = 'BEGIN HIDDEN TESTS'
c.ClearHiddenTests.end_test_delimeter = 'END HIDDEN TESTS'

## NO validar metadatos estrictamente (más flexibilidad)
c.ClearHiddenTests.enforce_metadata = False

# ----------------------------------------------------------------------------
# BLOQUEO DE CELDAS
# ----------------------------------------------------------------------------

## Bloquear celdas de calificación (no editables/eliminables)
c.LockCells.lock_grade_cells = True

## Bloquear celdas de solo lectura
c.LockCells.lock_readonly_cells = True

## Bloquear celdas de solución
c.LockCells.lock_solution_cells = True

# ----------------------------------------------------------------------------
# LÍMITE DE OUTPUT
# ----------------------------------------------------------------------------

## Número máximo de líneas de output por celda
## Previene notebooks muy verbosos
c.LimitOutput.max_lines = 1000

## Número máximo de líneas de traceback
c.LimitOutput.max_traceback = 100

# ----------------------------------------------------------------------------
# ARCHIVOS E IGNORADOS
# ----------------------------------------------------------------------------

## Lista de archivos/carpetas a ignorar
c.CourseDirectory.ignore = [
    '.ipynb_checkpoints',
    '*.pyc',
    '__pycache__',
    'feedback',
    '.DS_Store',
    '*.swp',
    '*.swo',
    '*~'
]

## Tamaño máximo de archivos en KB (100 MB)
c.CourseDirectory.max_file_size = 100000

# ----------------------------------------------------------------------------
# CALIFICACIÓN Y PENALIZACIONES
# ----------------------------------------------------------------------------

## Método de penalización por entrega tardía
## Opciones: 'none', 'zero'
c.LateSubmissionPlugin.penalty_method = 'none'

# ----------------------------------------------------------------------------
# EXPORTACIÓN Y TIMESTAMPS
# ----------------------------------------------------------------------------

## Formato de timestamps
c.Exchange.timestamp_format = '%Y-%m-%d %H:%M:%S %Z'

## Zona horaria para timestamps
## Ejemplos: 'UTC', 'America/Lima', 'America/Mexico_City'
c.Exchange.timezone = 'UTC'

# ----------------------------------------------------------------------------
# FEEDBACK
# ----------------------------------------------------------------------------

## Prioridad de tipos de datos para mostrar en feedback
c.GetGrades.display_data_priority = [
    'text/html',
    'application/pdf',
    'text/latex',
    'image/svg+xml',
    'image/png',
    'image/jpeg',
    'text/plain'
]

# ============================================================================
# NOTAS IMPORTANTES
# ============================================================================
#
# 1. CONFIGURACIÓN DINÁMICA:
#    El notebook 'nbgrader_optimizado.ipynb' genera automáticamente
#    este archivo con tus valores específicos. No necesitas editarlo manualmente.
#
# 2. NOMBRES SIN ACENTOS:
#    Los nombres de estudiantes NO deben tener acentos.
#    Usar: Martinez (✓) vs Martínez (✗)
#
# 3. ESTRUCTURA DE ARCHIVOS:
#    - source/{ASSIGNMENT_ID}/{ASSIGNMENT_ID}.ipynb
#    - submitted/{ESTUDIANTE}/{ASSIGNMENT_ID}/{ASSIGNMENT_ID}.ipynb
#
# 4. GOOGLE COLAB:
#    Este archivo debe estar en /content/ al ejecutar nbgrader
#
# 5. PERSONALIZACIÓN:
#    Si usas este archivo manualmente, descomenta y edita las líneas
#    comentadas (las que empiezan con '#') según tus necesidades.
#
# ============================================================================
