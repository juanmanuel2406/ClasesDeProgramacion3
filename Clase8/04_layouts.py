"""
Programación 3 - Clase 8: Layouts - organizar los widgets
=========================================================
Crear un widget no le dice a Qt dónde queremos ponerlo. Para eso están
los layouts, que además redistribuyen los controles cuando el usuario
cambia el tamaño de la ventana.

    QVBoxLayout  -> organiza verticalmente (uno debajo del otro)
    QHBoxLayout  -> organiza horizontalmente (uno al lado del otro)
    QGridLayout  -> organiza mediante filas y columnas

En este ejemplo las tres variantes conviven en la misma ventana: un
layout raíz vertical que contiene tres secciones.

Correr: .\\.venv\\Scripts\\python.exe 04_layouts.py
"""

import sys

from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


app = QApplication(sys.argv)

window = QMainWindow()

# Layout raíz: contiene las tres secciones, una debajo de la otra.
central_widget = QWidget()
layout = QVBoxLayout(central_widget)

# ----------------------------------------------------------------------
# 1) SECCIÓN QVBoxLayout - elementos apilados verticalmente
# ----------------------------------------------------------------------
layout.addWidget(QLabel("QVBoxLayout - vertical"))

vertical = QVBoxLayout()
vertical.addWidget(QLabel("Primer widget"))
vertical.addWidget(QLineEdit())
vertical.addWidget(QPushButton("Tercer widget"))
layout.addLayout(vertical)

# ----------------------------------------------------------------------
# 2) SECCIÓN QHBoxLayout - elementos uno al lado del otro
# ----------------------------------------------------------------------
layout.addWidget(QLabel("QHBoxLayout - horizontal"))

horizontal = QHBoxLayout()
horizontal.addWidget(QPushButton("Botón 1"))
horizontal.addWidget(QPushButton("Botón 2"))
horizontal.addWidget(QPushButton("Botón 3"))
layout.addLayout(horizontal)

# ----------------------------------------------------------------------
# 3) SECCIÓN QGridLayout - filas y columnas (ideal para formularios)
# ----------------------------------------------------------------------
layout.addWidget(QLabel("QGridLayout - filas y columnas"))

# addWidget(widget, fila, columna)
# La etiqueta va en la columna 0 y el campo de texto en la columna 1.
rejilla = QGridLayout()
rejilla.addWidget(QLabel("Nombre:"), 0, 0)
rejilla.addWidget(QLineEdit(), 0, 1)
rejilla.addWidget(QLabel("Email:"), 1, 0)
rejilla.addWidget(QLineEdit(), 1, 1)
layout.addLayout(rejilla)

# ----------------------------------------------------------------------
# JERARQUÍA DE WIDGETS
# ----------------------------------------------------------------------
# QMainWindow
#     └── central_widget
#             └── layout (QVBoxLayout raíz)
#                     ├── QLabel
#                     ├── vertical (QVBoxLayout)
#                     │       ├── QLabel
#                     │       ├── QLineEdit
#                     │       └── QPushButton
#                     ├── QLabel
#                     ├── horizontal (QHBoxLayout)
#                     │       └── 3 x QPushButton
#                     ├── QLabel
#                     └── rejilla (QGridLayout)
#
# Un layout puede contener widgets y también otros layouts: por eso
# usamos addLayout() para los sub-layouts y addWidget() para los controles.

window.setCentralWidget(central_widget)

window.setWindowTitle("Layouts: vertical, horizontal y rejilla")

window.resize(500, 600)

window.show()

sys.exit(app.exec())
