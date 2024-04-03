import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Cambiar Color del Rectángulo')

        self.rect_color = QColor(168, 34, 3)  # Color inicial del rectángulo

        self.btn_change_color = QPushButton('Cambiar Color', self)
        self.btn_change_color.setGeometry(10, 10, 120, 30)
        self.btn_change_color.clicked.connect(self.changeColor)

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.rect_color)  # Establecer el color del borde
        painter.setBrush(self.rect_color)  # Establecer el color de relleno
        painter.drawRect(10, 50, 150, 80)  # Dibujar el rectángulo

    def changeColor(self):
        # Generar un color aleatorio
        new_color = QColor.fromRgbF(
            self.randFloat(), self.randFloat(), self.randFloat()
        )
        self.rect_color = new_color
        self.update()  # Actualizar la ventana para reflejar el nuevo color

    def randFloat(self):
        import random
        return random.uniform(0.0, 1.0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

