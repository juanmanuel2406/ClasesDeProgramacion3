"""
Programación 3 - Clase 8: Práctica - Formulario
================================================
Armamos un formulario con los elementos pedidos:

    Nombre  + caja de texto
    Email   + caja de texto
    [ Guardar ]

El botón no tiene que hacer nada todavía: el objetivo es concentrarnos en
la creación y organización de los widgets.

Correr: .\\.venv\\Scripts\\python.exe 05_formulario.py
"""

import sys

from PySide6.QtWidgets import (
    QApplication,
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
# WIDGETS DEL FORMULARIO
# ----------------------------------------------------------------------
label_nombre = QLabel("Nombre")
input_nombre = QLineEdit()
input_nombre.setPlaceholderText("Ingrese su nombre")

label_email = QLabel("Email")
input_email = QLineEdit()
input_email.setPlaceholderText("Ingrese su email")

button_guardar = QPushButton("Guardar")

# ----------------------------------------------------------------------
# ORDEN EN PANTALLA
# ----------------------------------------------------------------------
# El layout vertical apila los controles en el orden en que los agregamos.
layout.addWidget(label_nombre)
layout.addWidget(input_nombre)
layout.addWidget(label_email)
layout.addWidget(input_email)
layout.addWidget(button_guardar)

window.setCentralWidget(central_widget)

window.setWindowTitle("Formulario - Sistema de alumnos")

window.resize(400, 300)

window.show()

sys.exit(app.exec())
