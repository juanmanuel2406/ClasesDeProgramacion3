"""
Programación 3 - Clase 8: Nuestra primera aplicación
===================================================
Una aplicación gráfica NO termina después de mostrar un resultado:
queda ejecutándose y esperando que el usuario interactúe con ella
(el event loop).

Solo necesitamos tres cosas:
    1) QApplication  -> administra la aplicación y el ciclo de eventos
    2) QMainWindow   -> la ventana principal (aún no visible)
    3) app.exec()    -> inicia el event loop y espera eventos

Correr: .\\.venv\\Scripts\\python.exe 01_primera_aplicacion.py
"""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow


# ----------------------------------------------------------------------
# 1) CREAR LA APLICACIÓN (debe existir una sola, y antes que cualquier ventana)
# ----------------------------------------------------------------------
app = QApplication(sys.argv)

# ----------------------------------------------------------------------
# 2) CREAR LA VENTANA
# ----------------------------------------------------------------------
# Ojo: aquí el objeto ventana existe, pero todavía NO se ve nada en pantalla.
window = QMainWindow()

# El título que aparece en la barra de la ventana.
window.setWindowTitle("Mi primera aplicación")

# Tamaño inicial: primero el ancho (600), después el alto (400).
window.resize(600, 400)

# ----------------------------------------------------------------------
# 3) MOSTRAR LA VENTANA
# ----------------------------------------------------------------------
# show() la hace visible. Sin esta llamada la ventana no aparecería.
window.show()

# ----------------------------------------------------------------------
# 4) EJECUTAR LA APLICACIÓN
# ----------------------------------------------------------------------
# app.exec() inicia el event loop: el programa queda esperando eventos
# (clics, teclas, cerrar la ventana) hasta que el usuario termine.
sys.exit(app.exec())
