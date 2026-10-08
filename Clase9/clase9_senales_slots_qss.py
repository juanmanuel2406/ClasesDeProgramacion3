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


def saludar():
    print("Hola desde Qt")


def cambiar_texto():
    label_titulo.setText("¡Hola desde el botón!")


def mostrar():
    nombre = input_nombre.text()
    email = input_email.text()

    if not nombre:
        label_resultado.setText("Debe ingresar un nombre")
        return

    label_resultado.setText("Nombre: " + nombre + "\nEmail: " + email)


def limpiar():
    input_nombre.clear()
    input_email.clear()
    label_resultado.clear()


def salir():
    app.quit()


def nombre_cambio(texto):
    label_estado.setText("Escribiendo: " + texto)


ESTILO = """
    QLabel {
        font-size: 16px;
    }
    QLineEdit {
        padding: 8px;
        font-size: 14px;
        border: 1px solid gray;
    }
    QPushButton {
        background-color: blue;
        color: white;
        padding: 8px;
        font-size: 14px;
    }
    QPushButton:hover {
        background-color: gray;
        font-size: 15px;
    }
    QPushButton:pressed {
        padding-left: 10px;
        padding-top: 10px;
    }
"""


app = QApplication(sys.argv)

app.setStyleSheet(ESTILO)

window = QMainWindow()
window.setWindowTitle("Formulario interactivo")
window.resize(400, 320)

central_widget = QWidget()
layout = QVBoxLayout(central_widget)

label_titulo = QLabel("Texto original")

label_nombre = QLabel("Nombre:")
input_nombre = QLineEdit()
input_nombre.setPlaceholderText("Ingrese su nombre")

label_email = QLabel("Email:")
input_email = QLineEdit()
input_email.setPlaceholderText("Ingrese su email")

layout.addWidget(label_titulo)
layout.addWidget(label_nombre)
layout.addWidget(input_nombre)
layout.addWidget(label_email)
layout.addWidget(input_email)

button_mostrar = QPushButton("Mostrar")
button_limpiar = QPushButton("Limpiar")

botones_layout = QHBoxLayout()
botones_layout.addWidget(button_mostrar)
botones_layout.addWidget(button_limpiar)

layout.addLayout(botones_layout)

button_saludar = QPushButton("Saludar")
button_cambiar = QPushButton("Cambiar texto")
button_salir = QPushButton("Salir")

button_salir.setStyleSheet("background-color: blue;" "color: white;")

acciones_layout = QHBoxLayout()
acciones_layout.addWidget(button_saludar)
acciones_layout.addWidget(button_cambiar)
acciones_layout.addWidget(button_salir)

layout.addLayout(acciones_layout)

label_resultado = QLabel("")
label_resultado.setWordWrap(True)

label_estado = QLabel("")

layout.addWidget(label_resultado)
layout.addWidget(label_estado)

window.setCentralWidget(central_widget)

button_mostrar.clicked.connect(mostrar)
button_limpiar.clicked.connect(limpiar)
button_saludar.clicked.connect(saludar)
button_cambiar.clicked.connect(cambiar_texto)
button_salir.clicked.connect(salir)

input_nombre.textChanged.connect(nombre_cambio)

window.show()

sys.exit(app.exec())
