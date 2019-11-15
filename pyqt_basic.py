from PyQt5 import QtWidgets
import gui
import sys

def on_button_clicked():
    ui.labelManufacturer_2.setText("Bafang")
    ui.labelModel_2.setText("BBS01")
    ui.labelHardwVers_2.setText("2.4")
    ui.labelFirmVers_2.setText("2.0.3")
    ui.labelMaxCurrent_2.setText("20A")

def actionExitTriggered():
    app.quit()

def actionLoadTriggered():
    print("load file")

def actionSaveTriggered():
    print("save file")

def actionSaveAsTriggered():
    print("save file as")

def prepare_gui():
    ui.pushButtonLoad.clicked.connect(on_button_clicked)
    ui.actionExit.triggered.connect(actionExitTriggered)
    ui.actionLoad.triggered.connect(actionLoadTriggered)
    ui.actionSave.triggered.connect(actionSaveTriggered)
    ui.actionSave_as.triggered.connect(actionSaveAsTriggered)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)

    prepare_gui()

    MainWindow.show()
    sys.exit(app.exec_())
