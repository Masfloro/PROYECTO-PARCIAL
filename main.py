import sys
from interfaz import *
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
import ping3

class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog() 
		self.ui.setupUi(self)
		#acceder a las paginas
		self.ui.btn_general.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.mapa_general)) 
		self.ui.btn_switch.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.swtich)) 
		self.ui.btn_pc.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.pc))
		ping3.verbose_ping('192.168.1.36')
		if ping3.ping('192.168.1.36') is not None:
			self.ui.label_50.setStyleSheet("background-color:rgb(255,0,0)")

	

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	