"""
Programación 3 - Clase 8: Widgets - los componentes de una interfaz
==================================================================
Un widget es un componente visual de la interfaz gráfica. Prácticamente
todo elemento que colocamos dentro de una ventana está representado
mediante un objeto.

Los tres widgets básicos de esta clase:

    QLabel      -> muestra texto
    QLineEdit   -> permite ingresar texto
    QPushButton -> botón

Todavía no hacemos que el botón haga algo: las señales y slots se ven
en la sección siguiente.

Correr: .\\.venv\\Scripts\\python.exe 03_widgets_basicos.py
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

# ----------------------------------------------------------------------
# 1) WIDGET CENTRAL + LAYOUT VERTICAL
# ----------------------------------------------------------------------
# Sobre QMainWindow no se agrega un layout directamente: primero creamos
# un QWidget que será el "central widget" y le asignamos un layout.
central_widget = QWidget()
layout = QVBoxLayout(central_widget)

# ----------------------------------------------------------------------
# 2) CREAR LOS WIDGETS
# ----------------------------------------------------------------------
# QLabel muestra un texto fijo.
label = QLabel("Nombre")

# QLineEdit es el cuadro de texto donde el usuario escribe.
input_nombre = QLineEdit()

# Texto de ayuda que se ve cuando el campo está vacío.
input_nombre.setPlaceholderText("Ingrese su nombre")

# QPushButton representa un botón. Todavía no tiene comportamiento.
button = QPushButton("Guardar")

# ----------------------------------------------------------------------
# 3) AGREGAR LOS WIDGETS AL LAYOUT
# ----------------------------------------------------------------------
# El orden en que los agregamos es el orden en que aparecen en pantalla.
layout.addWidget(label)
layout.addWidget(input_nombre)
layout.addWidget(button)

# ----------------------------------------------------------------------
# 4) CONECTAR TODO CON LA VENTANA
# ----------------------------------------------------------------------
window.setCentralWidget(central_widget)

window.setWindowTitle("Widgets básicos")

window.resize(400, 300)

window.show()

sys.exit(app.exec())
