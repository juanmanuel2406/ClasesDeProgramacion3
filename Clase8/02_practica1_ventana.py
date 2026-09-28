"""
Programación 3 - Clase 8: Práctica 1 - Experimentando con la ventana
====================================================================
Partimos de 01_primera_aplicacion.py y cumplimos la actividad:

    - Cambiar el título de la ventana a "Sistema de alumnos".
    - Establecer un tamaño inicial de 800 x 500.
    - Probar otros dos tamaños diferentes.
    - Cambiar nuevamente el título de la ventana.
    - Agregar un comentario explicando para qué sirve app.exec().

Los tamaños y títulos alternativos quedan comentados: probalos
descomentando uno por vez, mirando el resultado y volviendo a comentarlo.

Correr: .\\.venv\\Scripts\\python.exe 02_practica1_ventana.py
"""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow


app = QApplication(sys.argv)

window = QMainWindow()

# ----------------------------------------------------------------------
# 1) TÍTULO DE LA VENTANA
# ----------------------------------------------------------------------
window.setWindowTitle("Sistema de alumnos")

# ----------------------------------------------------------------------
# 2) TAMAÑO INICIAL: ancho x alto
# ----------------------------------------------------------------------
window.resize(800, 500)

# Otros dos tamaños para experimentar (dejá activo uno a la vez):
# window.resize(400, 300)   # más chica
# window.resize(1024, 768)  # más grande

# ----------------------------------------------------------------------
# 3) CAMBIAR NUEVAMENTE EL TÍTULO
# ----------------------------------------------------------------------
# Podemos reemplazarlo en cualquier momento, incluso con la ventana visible.
window.setWindowTitle("Sistema de alumnos - mi primera ventana con Qt")

# Si quisiéramos volver al título anterior:
# window.setWindowTitle("Sistema de alumnos")

window.show()

# ----------------------------------------------------------------------
# 4) PARA QUÉ SIRVE app.exec()
# ----------------------------------------------------------------------
# app.exec() inicia el EVENT LOOP (ciclo de eventos).
#
# Es el mecanismo que mantiene la aplicación ejecutándose: en lugar de
# terminar como un script normal, el programa queda esperando infinitamente
# los eventos que ocurren mientras el usuario interactúa (presionar un botón,
# escribir, mover el mouse, cerrar la ventana) y responde a cada uno.
#
# Sin esta línea el programa se cerraría apenas termina la ejecución del
# código, por más que la ventana ya haya sido creada y mostrada.
sys.exit(app.exec())
