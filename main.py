import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from interfaz import Ui_Dialog  # Importa la interfaz desde el archivo interfaz.py
import ping3
import threading
import time

class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec())

