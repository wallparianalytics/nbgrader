#!/usr/bin/env python3
"""
Script para corregir automáticamente el metadata de celdas de test
en notebooks de nbgrader, para que los tests NO aparezcan en el feedback
de los estudiantes.

Uso:
    python script_corregir_metadata_tests.py <notebook.ipynb>

El script:
1. Lee el notebook
2. Encuentra todas las celdas de test (nbgrader.grade = true)
3. Establece locked = true en todas las celdas de test
4. Guarda una copia del notebook original como backup
5. Guarda el notebook corregido
"""

import json
import sys
import os
import shutil
from datetime import datetime
import nbformat

def corregir_metadata_tests(notebook_path):
    """
    Corrige el metadata de las celdas de test para ocultar el código.

    Args:
        notebook_path: Ruta al notebook a corregir

    Returns:
        dict con estadísticas de corrección
    """
    if not os.path.exists(notebook_path):
        return {
            'error': f'El archivo no existe: {notebook_path}',
            'success': False
        }

    # Crear backup
    backup_path = notebook_path + f'.backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    shutil.copy2(notebook_path, backup_path)

    # Leer notebook
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
    except Exception as e:
        return {
            'error': f'Error leyendo notebook: {e}',
            'success': False
        }

    # Estadísticas
    stats = {
        'total_cells': len(nb.cells),
        'test_cells_found': 0,
        'test_cells_corrected': 0,
        'test_cells_already_locked': 0,
        'changes': [],
        'success': False
    }

    # Procesar cada celda
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != 'code':
            continue

        metadata = cell.get('metadata', {})
        nbgrader_meta = metadata.get('nbgrader', {})

        # ¿Es una celda de test?
        is_test = nbgrader_meta.get('grade', False) and not nbgrader_meta.get('solution', False)

        if is_test:
            stats['test_cells_found'] += 1
            grade_id = nbgrader_meta.get('grade_id', f'cell-{i}')
            locked = nbgrader_meta.get('locked', False)

            if not locked:
                # CORRECCIÓN: Establecer locked = true
                nbgrader_meta['locked'] = True
                cell['metadata']['nbgrader'] = nbgrader_meta

                stats['test_cells_corrected'] += 1
                stats['changes'].append({
                    'cell_index': i,
                    'grade_id': grade_id,
                    'action': 'set locked=true'
                })
            else:
                stats['test_cells_already_locked'] += 1

    # Guardar notebook corregido
    if stats['test_cells_corrected'] > 0:
        try:
            with open(notebook_path, 'w', encoding='utf-8') as f:
                nbformat.write(nb, f)
            stats['success'] = True
            stats['backup_path'] = backup_path
        except Exception as e:
            stats['error'] = f'Error guardando notebook: {e}'
            stats['success'] = False
    elif stats['test_cells_found'] == 0:
        stats['success'] = False
        stats['error'] = 'No se encontraron celdas de test en el notebook'
        # Eliminar backup si no hubo cambios
        if os.path.exists(backup_path):
            os.remove(backup_path)
    else:
        stats['success'] = True
        stats['info'] = 'Todas las celdas de test ya tenían locked=true. No se hicieron cambios.'
        # Eliminar backup si no hubo cambios
        if os.path.exists(backup_path):
            os.remove(backup_path)

    return stats


def main():
    if len(sys.argv) < 2:
        print("="*70)
        print("Script para corregir metadata de tests en notebooks de nbgrader")
        print("="*70)
        print("\nUso:")
        print(f"  python {sys.argv[0]} <notebook.ipynb>")
        print("\nEjemplo:")
        print(f"  python {sys.argv[0]} source/Assignment1/Assignment1.ipynb")
        print("\n" + "="*70)
        sys.exit(1)

    notebook_path = sys.argv[1]

    print("="*70)
    print("🔧 CORRECCIÓN AUTOMÁTICA DE METADATA DE TESTS")
    print("="*70)
    print(f"\nNotebook: {notebook_path}\n")

    stats = corregir_metadata_tests(notebook_path)

    if stats.get('error'):
        print(f"❌ ERROR: {stats['error']}")
        sys.exit(1)

    print("📊 RESULTADOS:")
    print("="*70)
    print(f"Total de celdas:                {stats['total_cells']}")
    print(f"Celdas de test encontradas:     {stats['test_cells_found']}")
    print(f"Celdas corregidas:              {stats['test_cells_corrected']}")
    print(f"Celdas ya correctas:            {stats['test_cells_already_locked']}")

    if stats['test_cells_corrected'] > 0:
        print("\n✅ CAMBIOS REALIZADOS:")
        print("="*70)
        for change in stats['changes']:
            print(f"  Celda {change['cell_index']}: {change['grade_id']}")
            print(f"    → {change['action']}")

        print("\n" + "="*70)
        print("✅ ¡Notebook corregido exitosamente!")
        print("="*70)
        print(f"Backup guardado en: {stats['backup_path']}")
        print(f"\n💡 SIGUIENTE PASO:")
        print(f"   1. Ejecuta: nbgrader generate_assignment '{os.path.basename(os.path.dirname(notebook_path))}'")
        print(f"   2. Los tests ya NO aparecerán en el feedback de los estudiantes")
        print("="*70)
    elif stats.get('info'):
        print("\n✅ " + stats['info'])
    else:
        print("\n⚠️  No se encontraron celdas de test para corregir")

    print()


if __name__ == '__main__':
    main()
