from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from generated_gui import Ui_MainWindow
import sys
from protocol import Protocol
from bafang import Bafang

class BafanConfig(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(BafanConfig, self).__init__()
        self.setupUi(self)
        self.protocol = Protocol()
        self.get_ports()
        self.connect_signals()
        self.connected = False
    
    def connect_signals(self):
        self.pushButtonLoad.clicked.connect(self.on_pushButtonLoad_clicked)
        self.actionExit.triggered.connect(self.actionExitTriggered)
        self.actionLoad.triggered.connect(self.actionLoadTriggered)
        self.actionSave.triggered.connect(self.actionSaveTriggered)
        self.actionSave_as.triggered.connect(self.actionSaveAsTriggered)
        self.pushButtonScan.clicked.connect(self.on_pushButtonScan_clicked)
        self.pushButtonRead.clicked.connect(self.on_pushButtonRead_clicked)
        self.pushButtonConnect.clicked.connect(self.on_pushButtonConnect_clicked)
        self.pushButtonRead.clicked.connect(self.on_pushButtonRead_clicked)
        self.actionAbout.triggered.connect(self.actionAboutTriggered)
    
    def on_pushButtonLoad_clicked(self):
        self.info_bytes = self.protocol.get_info()
        self.bafang = Bafang(self.info_bytes)
        self.updateInfo()

    def on_pushButtonScan_clicked(self):
        self.get_ports()

    def get_ports(self):
        self.comboBoxPorts.clear()
        ports_list = self.protocol.get_ports()
        if len(ports_list) != 0:
            for p in ports_list:
                self.comboBoxPorts.addItem(p[0])
            self.pushButtonConnect.setEnabled(True)
        else:
            print("No Com Ports found")


    def on_pushButtonConnect_clicked(self):
        if not (self.connected):
            self.protocol.connect(self.comboBoxPorts.currentText())
            self.connected = True
            self.pushButtonLoad.setEnabled(True)
            self.pushButtonRead.setEnabled(True)
            self.statusbar.showMessage("connected to: " + self.comboBoxPorts.currentText())
            self.on_pushButtonLoad_clicked()

    def on_pushButtonRead_clicked(self):
        self.info_bytes = self.protocol.get_info()
        self.bafang = Bafang(self.info_bytes)
        self.updateInfo()
            

    def updateInfo(self):
        self.labelManufacturer_2.setText(self.bafang.manufacturer)
        self.labelModel_2.setText(self.bafang.model)
        self.labelHardwVers_2.setText(str(self.bafang.hw_version))
        self.labelFirmVers_2.setText(str(self.bafang.fw_version))
        self.labelMaxCurrent_2.setText(str(self.bafang.max_current))

    def actionExitTriggered(self):
        app.quit()

    def actionLoadTriggered(self):
        print("load file")

    def actionSaveTriggered(self):
        print("save file")

    def actionSaveAsTriggered(self):
        print("save file as")

    def actionAboutTriggered(self):
        QMessageBox.about(self, "About this app", "This is a cross platform tool to configure bafang controllers.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    bafang_config = BafanConfig()
    bafang_config.show()
    app.exec_()