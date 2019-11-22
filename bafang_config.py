from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from generated_gui import Ui_MainWindow
import sys
from protocol import Protocol
from bafang import Bafang
import json_file

class BafanConfig(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super(BafanConfig, self).__init__()
        # uic.loadUi('BafangConfigTool.ui', self) # Load the .ui file, no code completion
        self.started = False
        self.setupUi(self)
        self.protocol = Protocol()
        self.get_ports()
        self.bafang = Bafang()
        self.connect_signals()
        self.connected = False
        self.started = True

    def connect_signals(self):
        self.pushButtonReadAll.clicked.connect(self.pushButtonReadAll_clicked)
        self.actionExit.triggered.connect(self.actionExitTriggered)
        self.actionLoad.triggered.connect(self.actionLoadTriggered)
        self.actionSave_as.triggered.connect(self.actionSaveAsTriggered)
        self.pushButtonScan.clicked.connect(self.pushButtonScan_clicked)
        self.pushButtonRead.clicked.connect(self.pushButtonRead_clicked)
        self.pushButtonConnect.clicked.connect(self.pushButtonConnect_clicked)
        self.actionAbout.triggered.connect(self.actionAboutTriggered)
        self.actionHelp.triggered.connect(self.actionHelpTriggered)
    
    def pushButtonReadAll_clicked(self):
        basic_bytes = self.protocol.get_basic()
        self.bafang.set_basic(basic_bytes)
        pedal_bytes = self.protocol.get_pedal()
        self.bafang.set_pedal(pedal_bytes)
        self.update_basic()
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
            if (self.started):
                print("No Com Ports found")
                QMessageBox.about(self, "Com ports", "No COM ports found")


    def pushButtonConnect_clicked(self):
        if not (self.connected):
            self.protocol.connect(self.comboBoxPorts.currentText())
            self.connected = True
            self.pushButtonReadAll.setEnabled(True)
            self.pushButtonRead.setEnabled(True)
            self.statusbar.showMessage("connected to: " + self.comboBoxPorts.currentText())
            info_bytes = self.protocol.get_info()
            self.bafang.set_info(info_bytes)
            self.update_info()

    def pushButtonRead_clicked(self):
        basic_bytes = self.protocol.get_basic()
        self.bafang.set_basic(basic_bytes)
        self.update_basic()
            
    def update_info(self):
        self.labelManufacturer_2.setText(self.bafang.manufacturer)
        self.labelModel_2.setText(self.bafang.model)
        self.labelHardwVers_2.setText(str(self.bafang.hw_version))
        self.labelFirmVers_2.setText(str(self.bafang.fw_version))
        self.labelMaxCurrent_2.setText(str(self.bafang.max_current))

    def update_basic(self):
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
        filename = self.openFileNameDialog()
        if filename:
            info, basic = json_file.read_json(filename)
            self.bafang.setbasicwithdict(basic)
            self.update_basic()

    def actionSaveAsTriggered(self):
        filename = self.saveFileDialog()
        if filename:
            json_file.write_json(self.bafang, filename)

    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self,"Load Bafang Settings", "","Text Files (*.json)")
        return fileName

    def saveFileDialog(self):
        fileName, _ = QFileDialog.getSaveFileName(self,"Backup Bafang settings","","Text Files (*.json)")
        return fileName

    def actionHelpTriggered(self):
        url = QtCore.QUrl('https://github.com/charclo/bafang-python/wiki')
        if not QtGui.QDesktopServices.openUrl(url):
            QtGui.QMessageBox.warning(self, 'Open Url', 'Could not open url')

    def actionAboutTriggered(self):
        QMessageBox.about(self, "About this app", "This is a cross platform tool to configure bafang controllers.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    bafang_config = BafanConfig()
    bafang_config.show()
    app.exec_()