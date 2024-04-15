 # Acceder a las páginas
        self.ui.btn_general.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.mapa_general))
        self.ui.btn_switch.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.swtich))
        self.ui.btn_pc.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pc))

        self.HOST_PRUEBA = '192.168.1.36'

        # Asignación de las IP de las working station
        self.pc1 = '192.168.10.1'
        self.pc2 = '192.168.10.2'
        # Otros PCs...
        self.pc10 = '192.168.10.10'

        self.pcs = [self.pc1, self.pc2, self.pc3, self.pc4, self.pc5, self.pc6, self.pc7, self.pc8, self.pc9, self.pc10]

        # Asignación de la IP del router principal y de los switches
        self.router = '192.168.20.1'
        self.routers = [self.router]

        self.switch_logistica = '192.168.30.1'
        self.switch_talento = '192.168.30.2'
        self.switch_sistemas = '192.168.30.3'
        self.switch_contabilidad = '192.168.30.4'
        self.switch_produccion = '192.168.30.5'

        self.switches = [self.switch_logistica, self.switch_talento, self.switch_sistemas, self.switch_contabilidad, self.switch_produccion]

        self.ips = self.pcs + self.routers + self.switches

        self.ping_thread = threading.Thread(target=self.correr_ping)
        self.ping_thread.start()

    def correr_ping(self):
        while True:
            response = ping3.ping('192.168.100.1')
            if response is not None and response > 0:
                self.cambiar_label_color((0, 255, 0))
                print('RESPONDE')
                time.sleep(2)
            elif response is False:
                self.cambiar_label_color((255, 0, 0))
                print('NO RESPONDE')
                time.sleep(2)

    def cambiar_label_color(self, color):
        style_sheet = f'background-color:rgb{color}'
        self.ui.status_pc10.setStyleSheet(style_sheet)