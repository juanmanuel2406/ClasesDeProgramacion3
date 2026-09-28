import sys

from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()

window.setWindowTitle("Sistema de alumnos")

window.resize(800, 500)


window.setWindowTitle("Sistema de alumnos - mi primera ventana con Qt")
window.show()

sys.exit(app.exec())
