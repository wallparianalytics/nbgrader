# ============================================================================
# NBGrader Configuration File
# ============================================================================
# Este archivo configura el comportamiento de NBGrader para el curso.
# Debe estar ubicado en: /content/ (para Google Colab)
#
# Curso: Python_AP
# Assignment: S01_D02_A02
# Instructor: [Tu Nombre]
# Última actualización: Octubre 2025
# ============================================================================

# ----------------------------------------------------------------------------
# CONFIGURACIÓN PRINCIPAL DEL CURSO
# ----------------------------------------------------------------------------

## Directorio raíz donde se encuentran todas las carpetas del curso
## (source, release, submitted, autograded, feedback)
c.CourseDirectory.root = '/content/drive/MyDrive/nbgrader_PAGD1_14123'

## Identificador del curso (aparece en la base de datos)
## IMPORTANTE: Cambiar según tu curso
# c.CourseDirectory.course_id = 'Python_AP'

## ID del assignment - puede dejarse vacío y especificarse por línea de comandos
## Ejemplo: nbgrader generate_assignment --assignment_id='S01_D02_A02'
# c.CourseDirectory.assignment_id = 'S01_D02_A02'

# ----------------------------------------------------------------------------
# ESTRUCTURA DE DIRECTORIOS
# ----------------------------------------------------------------------------

## Nombre del directorio que contiene los notebooks maestros del instructor
## Default: 'source'
# c.CourseDirectory.source_directory = 'source'

## Nombre del directorio que contiene los assignments para estudiantes
## Default: 'release'
# c.CourseDirectory.release_directory = 'release'

## Nombre del directorio que contiene las submissions de estudiantes
## Default: 'submitted'
# c.CourseDirectory.submitted_directory = 'submitted'

## Nombre del directorio que contiene los notebooks autocalificados
## Default: 'autograded'
# c.CourseDirectory.autograded_directory = 'autograded'

## Nombre del directorio que contiene el feedback en HTML
## Default: 'feedback'
# c.CourseDirectory.feedback_directory = 'feedback'

# ----------------------------------------------------------------------------
# EJECUCIÓN Y TIMEOUT
# ----------------------------------------------------------------------------

## Tiempo máximo (en segundos) para ejecutar una celda
## Útil para prevenir loops infinitos o código muy lento
## Default: None (sin límite)
## Recomendado para Google Colab: 180 segundos (3 minutos)
c.Execute.timeout = 180

## Número de reintentos si la ejecución falla
## Default: 0
# c.Execute.execute_retries = 0

## Si interrumpir el kernel en caso de timeout
## Default: False
# c.Execute.interrupt_on_timeout = False

## Si permitir errores durante la ejecución
## Default: False (detener al primer error)
# c.Execute.allow_errors = False

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
    'octave': "% YOUR CODE HERE\nerror('No Answer Given!')",
    'java': '// YOUR CODE HERE',
    'r': '# YOUR CODE HERE\nstop("No Answer Given!")'
}

## Texto que reemplaza respuestas escritas (markdown)
c.ClearSolutions.text_stub = 'YOUR ANSWER HERE'

## Delimitadores para tests ocultos (no visibles para estudiantes)
c.ClearHiddenTests.begin_test_delimeter = 'BEGIN HIDDEN TESTS'
c.ClearHiddenTests.end_test_delimeter = 'END HIDDEN TESTS'

## Si NO validar metadatos de celdas con tests ocultos
## IMPORTANTE: Poner en False para mayor flexibilidad
## Default: True (validar metadatos)
c.ClearHiddenTests.enforce_metadata = False

## Delimitadores para esquema de calificación (rúbricas)
c.ClearMarkScheme.begin_mark_scheme_delimeter = 'BEGIN MARK SCHEME'
c.ClearMarkScheme.end_mark_scheme_delimeter = 'END MARK SCHEME'

# ----------------------------------------------------------------------------
# BLOQUEO DE CELDAS
# ----------------------------------------------------------------------------

## Si bloquear (hacer no-editables y no-eliminables) todas las celdas
## Default: False (solo bloquear según metadatos)
# c.LockCells.lock_all_cells = False

## Si bloquear celdas de calificación (con metadatos grade=True)
## Default: True
c.LockCells.lock_grade_cells = True

## Si bloquear celdas de solo lectura (readonly=True)
## Default: True
c.LockCells.lock_readonly_cells = True

## Si bloquear celdas de solución (solution=True)
## Default: True
c.LockCells.lock_solution_cells = True

# ----------------------------------------------------------------------------
# LÍMITE DE OUTPUT
# ----------------------------------------------------------------------------

## Número máximo de líneas de output por celda
## Previene que notebooks muy verbosos generen archivos enormes
## Default: 1000
## Usar -1 para sin límite
c.LimitOutput.max_lines = 1000

## Número máximo de líneas de traceback en caso de errores
## Default: 100
c.LimitOutput.max_traceback = 100

# ----------------------------------------------------------------------------
# ARCHIVOS E IGNORADOS
# ----------------------------------------------------------------------------

## Lista de archivos/carpetas a ignorar al copiar directorios
## Default: ['.ipynb_checkpoints', '*.pyc', '__pycache__', 'feedback']
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

## Patrón de archivos a incluir (solo copiar archivos que coincidan)
## Default: ['*'] (todos los archivos)
# c.CourseDirectory.include = ['*']

## Tamaño máximo de archivos en KB (archivos más grandes serán ignorados)
## Default: 100000 (100 MB)
c.CourseDirectory.max_file_size = 100000

# ----------------------------------------------------------------------------
# PERMISOS Y SEGURIDAD
# ----------------------------------------------------------------------------

## Permisos de archivos generados
## Default: 0 (usa permisos por defecto)
## 444 = solo lectura, 644 = lectura/escritura para dueño
# c.BaseConverter.permissions = 0

## Si hacer archivos compartibles por grupo
## Default: False
## Solo usar si entiendes el modelo de permisos Unix
# c.CourseDirectory.groupshared = False

# ----------------------------------------------------------------------------
# BASE DE DATOS
# ----------------------------------------------------------------------------

## URL de la base de datos de calificaciones
## Default: '' (usa sqlite:///<root>/gradebook.db)
## Ejemplos:
##   SQLite: 'sqlite:////ruta/absoluta/gradebook.db'
##   MySQL: 'mysql://usuario:contraseña@localhost/nbgrader'
##   PostgreSQL: 'postgresql://usuario:contraseña@localhost/nbgrader'
# c.CourseDirectory.db_url = ''

# ----------------------------------------------------------------------------
# CALIFICACIÓN MANUAL
# ----------------------------------------------------------------------------

## Plugin para asignar penalizaciones por entrega tardía
## Opciones: 'none', 'zero'
## Default: 'none'
c.LateSubmissionPlugin.penalty_method = 'none'

# ----------------------------------------------------------------------------
# EXPORTACIÓN
# ----------------------------------------------------------------------------

## Formato de timestamps en exports
## Default: '%Y-%m-%d %H:%M:%S.%f %Z'
c.Exchange.timestamp_format = '%Y-%m-%d %H:%M:%S %Z'

## Zona horaria para timestamps
## Default: 'UTC'
## Ejemplos: 'America/Lima', 'America/Mexico_City', 'Europe/Madrid'
c.Exchange.timezone = 'UTC'

# ----------------------------------------------------------------------------
# FEEDBACK
# ----------------------------------------------------------------------------

## Prioridad de tipos de datos para mostrar en feedback
## El primero disponible será usado
c.GetGrades.display_data_priority = [
    'text/html',
    'application/pdf',
    'text/latex',
    'image/svg+xml',
    'image/png',
    'image/jpeg',
    'text/plain'
]

# ----------------------------------------------------------------------------
# NOTEBOOK CLIENT
# ----------------------------------------------------------------------------

## Archivo de historial de IPython para el kernel
## Usar ':memory:' para evitar crear archivos de historial
## Recomendado para ejecuciones en paralelo
c.Execute.ipython_hist_file = ':memory:'

## Si grabar timing de ejecución en los metadatos del notebook
## Default: True
c.Execute.record_timing = True

## Si almacenar el estado de widgets de Jupyter
## Default: True
# c.Execute.store_widget_state = True

# ----------------------------------------------------------------------------
# LOGGING Y DEBUG
# ----------------------------------------------------------------------------

## Nivel de logging
## Opciones: 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'
## Default: 30 (WARNING)
## Usar 'DEBUG' para troubleshooting
# c.Application.log_level = 'INFO'

## Archivo donde guardar logs
## Default: '' (no guardar en archivo, solo mostrar en pantalla)
# c.NbGrader.logfile = ''

# ============================================================================
# NOTAS IMPORTANTES
# ============================================================================
#
# 1. NOMBRES SIN ACENTOS:
#    - Los nombres de estudiantes NO deben tener acentos
#    - Usar: Martinez (correcto) vs Martínez (incorrecto)
#    - El feedback no funciona correctamente con acentos
#
# 2. ESTRUCTURA DE ARCHIVOS:
#    - Assignment ID debe coincidir con el nombre de carpeta
#    - Ejemplo: source/S01_D02_A02/S01_D02_A02.ipynb
#
# 3. GOOGLE COLAB:
#    - Copiar este archivo a /content/ antes de ejecutar nbgrader
#    - Reiniciar runtime si se cambia la configuración
#
# 4. TIMEOUT:
#    - Ajustar c.Execute.timeout según la complejidad del assignment
#    - 180s (3 min) es suficiente para la mayoría de casos
#    - Aumentar si los estudiantes tienen código que toma más tiempo
#
# 5. VALIDACIÓN:
#    - c.ClearHiddenTests.enforce_metadata = False permite mayor flexibilidad
#    - Cambiar a True si quieres validación estricta de metadatos
#
# ============================================================================
