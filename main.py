import sys
from interfaz import *
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets
import ping3
import threading
import time

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


		#Asignacion de las ip de las working station
		self.pc1='192.168.10.1'
		self.pc2='192.168.10.2'
		self.pc3='192.168.10.3'
		self.pc4='192.168.10.4'
		self.pc5='192.168.10.5'
		self.pc6='192.168.10.6'
		self.pc7='192.168.10.7'
		self.pc8='192.168.10.8'
		self.pc9='192.168.10.9'
		self.pc10='192.168.10.10'

		self.pcs=[self.pc1,self.pc2,self.pc3,self.pc4,self.pc5,self.pc6,self.pc7,self.pc8,self.pc9,self.pc10]



		#Asignacion de la ip del router principal
		self.router='192.168.20.1'
		self.routers = [self.router]

		#Asigancion de la ip de los switches 
		self.switch_logistica='192.168.30.1'
		self.switch_talento='192.168.30.2'
		self.switch_sistemas='192.168.30.3'
		self.switch_contabilidad='192.168.30.4'
		self.switch_produccion='192.168.30.5'

		self.switches = [self.switch_logistica,self.switch_talento,self.switch_sistemas,self.switch_contabilidad,self.switch_produccion]


		self.ips = self.pcs + self.routers + self.switches

		self.ping_thread = threading.Thread(target=self.correr_ping)
		self.ping_thread.start()


	
	def correr_ping(self):
		ip = '192.168.1.1'
		while(True):
			response = ping3.ping(ip)
			if  response is not None and response > 0:
					#self.cambiar_label_color((0,255,0))
				print(ip)
				time.sleep(2)
			if response is False:
					#self.cambiar_label_color((255,0,0))
				print(ip)
				time.sleep(2)
			

	def cambiar_label_color(self,color):
		style_sheet  = f'background-color:rgb{color}'
		#self.ui.label_50.setStyleSheet(style_sheet)

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	