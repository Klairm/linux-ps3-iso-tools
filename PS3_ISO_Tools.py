#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication,QMessageBox)
import numpy,time,sys

p = QtCore.QProcess()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PS3 ISO TOOLS")
        MainWindow.resize(382, 254)
        app_icon = QtGui.QIcon()
        app_icon.addFile('16x16.png', QtCore.QSize(16,16))
        app_icon.addFile('24x24.png', QtCore.QSize(24,24))
        app_icon.addFile('32x32.png', QtCore.QSize(32,32))
        app_icon.addFile('48x48.png', QtCore.QSize(48,48))
        app_icon.addFile('256x256.png', QtCore.QSize(256,256))
        app.setWindowIcon(app_icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PbExtract = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PbExtract.setObjectName("PbExtract")
        self.gridLayout.addWidget(self.PbExtract, 0, 0, 1, 1)
        self.PbExtract.clicked.connect(self.extractISO)
        self.PbConvertISO = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PbConvertISO.setObjectName("PbConvertISO")
        self.gridLayout.addWidget(self.PbConvertISO, 0, 1, 1, 1)
        self.PbConvertISO.clicked.connect(self.makeISO)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 180, 351, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 382, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.actionHow_to_use = QtWidgets.QAction(MainWindow)
        self.actionHow_to_use.setObjectName("actionHow_to_use")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PbExtract.setText(_translate("MainWindow", "Extract ISO"))
        self.PbConvertISO.setText(_translate("MainWindow", "Convert to ISO"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use"))
    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("The process has been completed! You can now close the program.")
        msg.setWindowTitle("Completed!")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def ready_to_read(self):
        output = p.readAllStandardOutput()
        print(str(output))
        for j in range(101):
            if "Finish!" in str(output):
                self.showdialog()
                self.progressBar.setValue(100)
                break
            time.sleep(0.5)
            self.progressBar.setValue(j)
        

    def extractISO(self):
      filename = QFileDialog.getOpenFileName(None, "Open ISO File", '.', "ISO Files (*.iso)")
      if filename:
       destination =QFileDialog.getExistingDirectory(None, "Select destination folder") 
       if destination:
           command = "extractps3iso"
           arguments = [filename[0],destination]
           p.start(command,arguments)
           p.readyReadStandardOutput.connect(self.ready_to_read)
                
    def makeISO(self):
        game =QFileDialog.getExistingDirectory(None, "Select game folder (example BLES/BLUS)") 
        if game:
            destination = QFileDialog.getExistingDirectory(None, "Select destination folder") 
            if destination:
                command = "makeps3iso"
                arguments = [game,destination]
                p.start(command,arguments)
                p.readyReadStandardOutput.connect(self.ready_to_read)
                
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
