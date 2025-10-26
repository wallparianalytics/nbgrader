# Solución: Tests Aparecen en el Feedback de Estudiantes

## Problema

Los estudiantes ven el código completo de los tests en el feedback HTML, incluyendo:

```python
### BEGIN HIDDEN TESTS
assert array1.shape[1] == 1, "Los arrays deben ser verticales (n×1)"
assert np.array_equal(concatenacion_horizontal, esperado_horizontal), \
    "La concatenación horizontal no es correcta"
### END HIDDEN TESTS
```

**Esto NO debería pasar.** Los estudiantes deberían ver solo:
- ✓ Test pasado / ✗ Test fallado
- Mensaje de error (si falló)
- Puntaje obtenido
- **NO** el código de los asserts

---

## Causa del Problema

Las celdas de test en tu notebook **NO tienen el metadata correcto**.

Específicamente, falta: `"locked": true` en el metadata de nbgrader.

---

## Solución Rápida (Opción 1): Corrección Automática

### Paso 1: Ejecuta la celda 8.2 en `nbgrader_optimizado.ipynb`

Esta celda automáticamente:
1. Lee tu notebook fuente
2. Encuentra todas las celdas de test
3. Establece `locked = true` en todas
4. Guarda el notebook corregido
5. Crea un backup del original

### Paso 2: Re-genera el assignment

Ejecuta la celda 9 del notebook optimizado:

```python
nbgrader generate_assignment '{ASSIGNMENT_ID}'
```

### Paso 3: Re-ejecuta autograding y feedback

1. Celda 25: Autograding masivo
2. Celda 26: Generar feedback masivo
3. Verifica el HTML del feedback - los tests ya NO deberían aparecer

---

## Solución Manual (Opción 2): Editar Metadata en Jupyter

Si prefieres editar manualmente o no tienes el notebook optimizado:

### Paso 1: Abre el notebook fuente en Jupyter

```bash
jupyter notebook source/{ASSIGNMENT_ID}/{ASSIGNMENT_ID}.ipynb
```

### Paso 2: Habilita la toolbar de nbgrader

En Jupyter:
- Menu: `View` → `Cell Toolbar` → `Edit Metadata`

### Paso 3: Para CADA celda de test

1. **Selecciona la celda de test**

2. **Click en "Edit Metadata"** (botón en la parte superior de la celda)

3. **Busca la sección `"nbgrader"`** en el JSON

4. **Verifica/agrega `"locked": true`**

   El metadata debe verse así:

   ```json
   {
     "nbgrader": {
       "grade": true,
       "grade_id": "test_ejercicio1",
       "locked": true,          ← ESTE ES EL CRÍTICO
       "points": 2,
       "schema_version": 3,
       "solution": false,
       "task": false
     }
   }
   ```

5. **Click "Edit"** para guardar

6. **Repite para TODAS las celdas de test**

### Paso 4: Guarda el notebook

`File` → `Save`

### Paso 5: Re-genera el assignment

```bash
cd /ruta/a/tu/curso
nbgrader generate_assignment 'ASSIGNMENT_ID'
```

---

## Verificación

### Opción A: Usar el script de verificación (recomendado)

Ejecuta la celda 8.1 en `nbgrader_optimizado.ipynb`:

```python
# Verifica el metadata de las celdas de test
```

Deberías ver:

```
✅ Celda 5: test_ejercicio1
   - Locked: True
   - Points: 2
   - Tiene código: True
```

Si ves `❌` o `Locked: False`, hay un problema.

### Opción B: Verificar manualmente el release

Después de generar el assignment, verifica el notebook en `release/`:

```python
import nbformat

nb_path = 'release/{ASSIGNMENT_ID}/{ASSIGNMENT_ID}.ipynb'
nb = nbformat.read(nb_path, as_version=4)

for i, cell in enumerate(nb.cells):
    nbg = cell.get('metadata', {}).get('nbgrader', {})
    if nbg.get('grade', False):
        locked = nbg.get('locked', False)
        print(f"Celda {i}: {nbg.get('grade_id')} - locked={locked}")
```

Todas las celdas de test deben tener `locked=True`.

### Opción C: Verificar el feedback HTML

Después de generar el feedback:

1. Abre el archivo HTML de un estudiante:
   ```
   feedback/{estudiante}/{ASSIGNMENT_ID}/{ASSIGNMENT_ID}.html
   ```

2. Busca las secciones de tests

3. **NO** deberías ver código como:
   ```python
   assert array1.shape[1] == 1
   ```

4. **SÍ** deberías ver:
   - ✓ Test {nombre}: PASSED (X pts)
   - ✗ Test {nombre}: FAILED (0 pts) - {mensaje de error}

---

## Ejemplo Completo

### Antes (INCORRECTO - tests visibles):

**Metadata de la celda:**
```json
{
  "nbgrader": {
    "grade": true,
    "grade_id": "test_suma",
    "locked": false,        ← PROBLEMA: false
    "points": 2
  }
}
```

**Lo que ve el estudiante en feedback.html:**
```python
# Test Cell
assert suma(2, 3) == 5, "La suma debe ser correcta"
assert suma(0, 0) == 0, "La suma de ceros debe ser cero"
### BEGIN HIDDEN TESTS
assert suma(100, 200) == 300
### END HIDDEN TESTS
```

### Después (CORRECTO - tests ocultos):

**Metadata de la celda:**
```json
{
  "nbgrader": {
    "grade": true,
    "grade_id": "test_suma",
    "locked": true,         ← CORRECTO: true
    "points": 2
  }
}
```

**Lo que ve el estudiante en feedback.html:**
```
✓ Test test_suma: PASSED (2.0 / 2.0 points)
```

O si falló:
```
✗ Test test_suma: FAILED (0.0 / 2.0 points)
   AssertionError: La suma debe ser correcta
```

**El código de los asserts NO se muestra.**

---

## Archivos de Ayuda

1. **`nbgrader_optimizado.ipynb`** - Celda 8.2: Corrección automática
2. **`ejemplo_assignment_con_tests_ocultos.ipynb`** - Ejemplo completo con metadata correcto
3. **`script_corregir_metadata_tests.py`** - Script standalone para corregir notebooks

---

## Script Standalone (Opción 3)

Si no estás usando el notebook optimizado, puedes usar el script directamente:

```bash
python script_corregir_metadata_tests.py source/{ASSIGNMENT_ID}/{ASSIGNMENT_ID}.ipynb
```

El script:
- Automáticamente corrige el metadata
- Crea un backup del original
- Muestra un resumen de cambios

---

## FAQ

### ¿Por qué `### BEGIN HIDDEN TESTS` no funciona?

Los delimitadores `### BEGIN HIDDEN TESTS` / `### END HIDDEN TESTS` solo funcionan si:

1. La celda tiene `"locked": true`
2. El `nbgrader_config.py` tiene configurados los delimitadores

**Ambos** son necesarios. No basta con solo usar los delimitadores en el código.

### ¿Puedo ocultar solo PARTE del código de la celda?

Sí, usa los delimitadores:

```python
# Este código SÍ se muestra en el feedback (tests básicos)
assert x > 0, "x debe ser positivo"

### BEGIN HIDDEN TESTS
# Este código NO se muestra (tests avanzados)
assert x == 42, "x debe ser exactamente 42"
assert y == 100, "y debe ser exactamente 100"
### END HIDDEN TESTS
```

Pero la celda DEBE tener `"locked": true`.

### ¿Afecta esto a las celdas de solución?

No. Solo afecta a las celdas de test (celdas con `"grade": true` y `"solution": false`).

Las celdas de solución (celdas con `"solution": true`) funcionan de manera diferente.

### ¿Puedo verificar esto antes de generar el assignment?

Sí. Ejecuta la celda 8.1 del notebook optimizado para verificar el metadata antes de generar.

---

## Resumen de Flujo Correcto

```
1. Crear notebook fuente con celdas de test
   ↓
2. Configurar metadata: locked=true en TODAS las celdas de test
   (Usar celda 8.2 para corrección automática)
   ↓
3. Verificar metadata (celda 8.1)
   ↓
4. Generar assignment (nbgrader generate_assignment)
   ↓
5. Estudiantes completan y entregan
   ↓
6. Autograding (nbgrader autograde)
   ↓
7. Generar feedback (nbgrader feedback)
   ↓
8. Verificar HTML - tests NO deben aparecer
   ↓
9. Distribuir feedback a estudiantes
```

---

## Contacto / Soporte

Si después de seguir todos estos pasos los tests siguen apareciendo:

1. Verifica que ejecutaste la celda 8.2 (corrección automática)
2. Verifica que re-generaste el assignment (celda 9)
3. Verifica que re-ejecutaste autograding y feedback (celdas 25-26)
4. Revisa el archivo release/{ASSIGNMENT_ID}/{ASSIGNMENT_ID}.ipynb y verifica manualmente el metadata

---

**Última actualización:** 2025-10-26
