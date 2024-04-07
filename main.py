import sys
from interfaz import *
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
import ping3
import threading

class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog() 
		self.ui.setupUi(self)
		#acceder a las paginas
		self.ui.btn_general.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.mapa_general)) 
		self.ui.btn_switch.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.swtich)) 
		self.ui.btn_pc.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.pc))

		self.HOST_PRUEBA = '192.168.1.36'
		self.ping_thread = threading.Thread(target=self.correr_ping)
		self.ping_thread.start()
	
	def correr_ping(self):
		while(True):
			response = ping3.ping(self.HOST_PRUEBA)
			if  response is not None and response > 0:
				self.cambiar_label_color((0,255,0))
				print(response)
			if response is False:
				self.cambiar_label_color((255,0,0))
				print(response)

	def cambiar_label_color(self,color):
		style_sheet  = f'background-color:rgb{color}'
		self.ui.label_50.setStyleSheet(style_sheet)

			

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	