
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)


window = QMainWindow()


window.setWindowTitle("Mi primera aplicación")


window.resize(600, 400)

window.show()
sys.exit(app.exec())
