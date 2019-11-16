from PyQt5 import QtWidgets
from bafang import Bafang
import gui
from serial import Serial, SerialException
from serial.tools import list_ports
import sys
from protocol import Protocol

class BafangConfig:

    def __init__(self):
        ui.pushButtonLoad.clicked.connect(self.on_pushButtonLoad_clicked)
        ui.actionExit.triggered.connect(self.actionExitTriggered)
        ui.actionLoad.triggered.connect(self.actionLoadTriggered)
        ui.actionSave.triggered.connect(self.actionSaveTriggered)
        ui.actionSave_as.triggered.connect(self.actionSaveAsTriggered)
        ui.pushButtonScan.clicked.connect(self.on_pushButtonScan_clicked)
        ui.pushButtonRead.clicked.connect(self.on_pushButtonRead_clicked)
    
    def on_pushButtonLoad_clicked(self):
        self.protocol = Protocol(ui.comboBoxPorts.currentText())
        self.info = self.protocol.get_info()

        info = baf.get_info()
        ui.labelManufacturer_2.setText(str(info[0]))
        ui.labelModel_2.setText(str(info[1]))
        ui.labelHardwVers_2.setText(str(info[2]))
        ui.labelFirmVers_2.setText(str(info[3]))
        ui.labelMaxCurrent_2.setText(str(info[4]))

    def on_pushButtonScan_clicked(self):
        ui.comboBoxPorts.clear()
        ports_list = list_ports.comports()
        if len(ports_list) != 0:
            for p in ports_list:
                ui.comboBoxPorts.addItem(p[0])
        else:
            print("No Com Ports found")
            sys.exit()

    def on_pushButtonRead_clicked(self):
        self.protocol = Protocol('/dev/cu.usbmodem142101')
        self.info = self.protocol.get_info()
        self.baf = Bafang(self.info)
        ui.labelManufacturer_2.setText(self.baf.manufacturer)

    def actionExitTriggered(self):
        app.quit()

    def actionLoadTriggered(self):
        print("load file")

    def actionSaveTriggered(self):
        print("save file")

    def actionSaveAsTriggered(self):
        print("save file as")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)

    config = BafangConfig()

    MainWindow.show()
    sys.exit(app.exec_())
