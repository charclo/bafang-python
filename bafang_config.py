from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from generated_gui import Ui_MainWindow
import sys
from protocol import Protocol
from bafang import Bafang
from json_file import JsonWriter

class BafanConfig(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(BafanConfig, self).__init__()
        self.setupUi(self)
        self.protocol = Protocol()
        self.get_ports()
        self.connect_signals()
        self.connected = False

    def connect_signals(self):
        self.pushButtonReadAll.clicked.connect(self.pushButtonReadAll_clicked)
        self.actionExit.triggered.connect(self.actionExitTriggered)
        self.actionLoad.triggered.connect(self.actionLoadTriggered)
        self.actionSave.triggered.connect(self.actionSaveTriggered)
        self.actionSave_as.triggered.connect(self.actionSaveAsTriggered)
        self.pushButtonScan.clicked.connect(self.pushButtonScan_clicked)
        self.pushButtonRead.clicked.connect(self.pushButtonRead_clicked)
        self.pushButtonConnect.clicked.connect(self.pushButtonConnect_clicked)
        self.actionAbout.triggered.connect(self.actionAboutTriggered)
    
    def pushButtonReadAll_clicked(self):
        basic_bytes = self.protocol.get_basic()
        self.bafang.store_basic(basic_bytes)
        pedal_bytes = self.protocol.get_pedal()
        self.bafang.store_pedal(pedal_bytes)
        self.updateBasic()
        self.protocol.get_throttle()

    # @pyqtSlot() this doesn't work for me, function gets called tree times
    # when it is called on_push...
    def pushButtonScan_clicked(self):
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


    def pushButtonConnect_clicked(self):
        if not (self.connected):
            self.protocol.connect(self.comboBoxPorts.currentText())
            self.connected = True
            self.pushButtonReadAll.setEnabled(True)
            self.pushButtonRead.setEnabled(True)
            self.statusbar.showMessage("connected to: " + self.comboBoxPorts.currentText())
            info_bytes = self.protocol.get_info()
            self.bafang = Bafang(info_bytes)
            self.updateInfo()

    def pushButtonRead_clicked(self):
        basic_bytes = self.protocol.get_basic()
        self.bafang.store_basic(basic_bytes)
        self.updateBasic()
            
    def updateInfo(self):
        self.labelManufacturer_2.setText(self.bafang.manufacturer)
        self.labelModel_2.setText(self.bafang.model)
        self.labelHardwVers_2.setText(str(self.bafang.hw_version))
        self.labelFirmVers_2.setText(str(self.bafang.fw_version))
        self.labelMaxCurrent_2.setText(str(self.bafang.max_current))

    def updateBasic(self):
        self.spinBoxLowBatteryVoltage.setValue(self.bafang.low_battery_protect)
        self.spinBoxCurrentLimit.setValue(self.bafang.limited_current)
        self.spinBoxAssist0.setValue(self.bafang.limited_current_assist0)
        self.spinBoxAssist1.setValue(self.bafang.limited_current_assist1)
        self.spinBoxAssist2.setValue(self.bafang.limited_current_assist2)
        self.spinBoxAssist3.setValue(self.bafang.limited_current_assist3)
        self.spinBoxAssist4.setValue(self.bafang.limited_current_assist4)
        self.spinBoxAssist5.setValue(self.bafang.limited_current_assist5)
        self.spinBoxAssist6.setValue(self.bafang.limited_current_assist6)
        self.spinBoxAssist7.setValue(self.bafang.limited_current_assist7)
        self.spinBoxAssist8.setValue(self.bafang.limited_current_assist8)
        self.spinBoxAssist9.setValue(self.bafang.limited_current_assist9)
        self.spinBoxSpeedlimit0.setValue(self.bafang.limited_speed_assist0)
        self.spinBoxSpeedlimit1.setValue(self.bafang.limited_speed_assist1)
        self.spinBoxSpeedlimit2.setValue(self.bafang.limited_speed_assist2)
        self.spinBoxSpeedlimit3.setValue(self.bafang.limited_speed_assist3)
        self.spinBoxSpeedlimit4.setValue(self.bafang.limited_speed_assist4)
        self.spinBoxSpeedlimit5.setValue(self.bafang.limited_speed_assist5)
        self.spinBoxSpeedlimit6.setValue(self.bafang.limited_speed_assist6)
        self.spinBoxSpeedlimit7.setValue(self.bafang.limited_speed_assist7)
        self.spinBoxSpeedlimit8.setValue(self.bafang.limited_speed_assist8)
        self.spinBoxSpeedlimit9.setValue(self.bafang.limited_speed_assist9)
        self.spinBoxSpeedMeterSignals.setValue(self.bafang.speedmeter_signals)


    def actionExitTriggered(self):
        app.quit()

    def actionLoadTriggered(self):
        print("load file")

    def actionSaveTriggered(self):
        self.json_writer = JsonWriter(self.bafang)
        self.json_writer.write_json()

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