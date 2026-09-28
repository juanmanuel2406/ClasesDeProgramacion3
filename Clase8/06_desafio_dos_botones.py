"""
Programación 3 - Clase 8: Desafío - Agregar un segundo botón
===========================================================
Partimos del formulario anterior y sumamos un botón "Limpiar", de forma
que ambos queden alineados uno al lado del otro:

    [ Guardar ]    [ Limpiar ]

Todavía no programamos el comportamiento de los botones. Para alinear
los dos en la misma fila pedimos un QHBoxLayout que los contenga y luego
agregamos ese layout al layout principal.

Correr: .\\.venv\\Scripts\\python.exe 06_desafio_dos_botones.py
"""

import sys

from PySide6.QtWidgets import (
    QApplication,
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

central_widget = QWidget()
layout = QVBoxLayout(central_widget)

# ----------------------------------------------------------------------
# CAMPOS DEL FORMULARIO (igual que en 05_formulario.py)
# ----------------------------------------------------------------------
label_nombre = QLabel("Nombre")
input_nombre = QLineEdit()
input_nombre.setPlaceholderText("Ingrese su nombre")

label_email = QLabel("Email")
input_email = QLineEdit()
input_email.setPlaceholderText("Ingrese su email")

layout.addWidget(label_nombre)
layout.addWidget(input_nombre)
layout.addWidget(label_email)
layout.addWidget(input_email)

# ----------------------------------------------------------------------
# LOS DOS BOTONES EN UNA MISMA FILA
# ----------------------------------------------------------------------
button_guardar = QPushButton("Guardar")
button_limpiar = QPushButton("Limpiar")

# Un layout puede vivir dentro de otro layout: este se ocupa de la fila
# de botones y después lo agregamos al layout vertical principal.
botones_layout = QHBoxLayout()
botones_layout.addWidget(button_guardar)
botones_layout.addWidget(button_limpiar)

layout.addLayout(botones_layout)

# ----------------------------------------------------------------------
# JERARQUÍA RESULTANTE
# ----------------------------------------------------------------------
# QMainWindow
#     └── central_widget
#             └── layout (QVBoxLayout)
#                     ├── QLabel
#                     ├── QLineEdit
#                     ├── QLabel
#                     ├── QLineEdit
#                     └── botones_layout (QHBoxLayout)
#                             ├── QPushButton "Guardar"
#                             └── QPushButton "Limpiar"

window.setCentralWidget(central_widget)

window.setWindowTitle("Desafío - Guardar y Limpiar")

window.resize(400, 300)

window.show()

sys.exit(app.exec())
