from PyQt5 import QtWidgets
from bafang import Bafang
import gui
from serial import Serial, SerialException
from serial.tools import list_ports
import sys

class BafangConfig:
    
    def on_pushButtonLoad_clicked(self):
        info = baf.get_info()
        ui.labelManufacturer_2.setText(str(info[0]))
        ui.labelModel_2.setText(str(info[1]))
        ui.labelHardwVers_2.setText(str(info[2]))
        ui.labelFirmVers_2.setText(str(info[3]))
        ui.labelMaxCurrent_2.setText(str(info[4]))

    def on_pushButtonScan_clicked(self):
        ports_list = list_ports.comports()
        if len(ports_list) != 0:
            for p in ports_list:
                ui.comboBoxPorts.addItem(p[0])
        else:
            print("No Com Ports found")
            sys.exit()

    def actionExitTriggered(self):
        app.quit()

    def actionLoadTriggered(self):
        print("load file")

    def actionSaveTriggered(self):
        print("save file")

    def actionSaveAsTriggered(self):
        print("save file as")

    def set_signals(self):
        ui.pushButtonLoad.clicked.connect(self.on_pushButtonLoad_clicked)
        ui.actionExit.triggered.connect(self.actionExitTriggered)
        ui.actionLoad.triggered.connect(self.actionLoadTriggered)
        ui.actionSave.triggered.connect(self.actionSaveTriggered)
        ui.actionSave_as.triggered.connect(self.actionSaveAsTriggered)
        ui.pushButtonScan.clicked.connect(self.on_pushButtonScan_clicked)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    baf = Bafang( "HZXT", "SZZ6", 22, 2011, 1, 20, 27)

    config = BafangConfig()
    config.set_signals()

    MainWindow.show()
    sys.exit(app.exec_())
