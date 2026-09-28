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
window.setWindowTitle("Formulario de Registro")


central_widget = QWidget()
main_layout = QVBoxLayout(central_widget)


label_nombre = QLabel("Nombre:")
input_nombre = QLineEdit()
input_nombre.setPlaceholderText("Ingrese su nombre")

label_email = QLabel("Email:")
input_email = QLineEdit()
input_email.setPlaceholderText("Ingrese su email")


button_guardar = QPushButton("Guardar")
button_limpiar = QPushButton("Limpiar")

buttons_layout = QHBoxLayout()
buttons_layout.addWidget(button_guardar)
buttons_layout.addWidget(button_limpiar)


main_layout.addWidget(label_nombre)
main_layout.addWidget(input_nombre)
main_layout.addWidget(label_email)
main_layout.addWidget(input_email)


main_layout.addLayout(buttons_layout)


window.setCentralWidget(central_widget)


window.show()
sys.exit(app.exec())
