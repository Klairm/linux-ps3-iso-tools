#!/usr/bin/env python3

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication, QMessageBox)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PS3 ISO TOOLS")
        MainWindow.resize(377, 363)
        app_icon = QtGui.QIcon()
        app_icon.addFile('icons/256x256.png', QtCore.QSize(256, 256))
        app.setWindowIcon(app_icon)
        self.p = None  # Default empty value for the process

        # Set Widgets  and size, buttons, layout, plaintext...

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 331, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.PbExtract = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PbExtract.setObjectName("PbExtract")
        self.gridLayout.addWidget(self.PbExtract, 0, 1, 1, 1)
        self.PbExtract.clicked.connect(
            lambda: self.extract_create_iso('extractps3iso'))

        self.PbConvertISO = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.PbConvertISO.setObjectName("PbConvertISO")
        self.gridLayout.addWidget(self.PbConvertISO, 1, 1, 1, 1)
        self.PbConvertISO.clicked.connect(
            lambda: self.extract_create_iso('makeps3iso'))

        self.text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text.setReadOnly(True)
        self.text.setGeometry(QtCore.QRect(20, 120, 331, 211))

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PS3 ISO TOOLS"))
        self.PbExtract.setText(_translate("MainWindow", "Extract ISO"))
        self.PbConvertISO.setText(_translate("MainWindow", "Convert to ISO"))

    def extract_create_iso(self, command):
        if self.p != None:
            self.p.kill()
        self.text.clear()

        game = False
        if command == 'extractps3iso':
            game, _ = QFileDialog.getOpenFileName(
                None, "Open ISO File", '.', "ISO Files (*.iso)")
        elif command == 'makeps3iso':
            game = QFileDialog.getExistingDirectory(
                None, "Select game folder (example BLES/BLUS)")
        if game and os.path.exists(game):
            destination = QFileDialog.getExistingDirectory(
                None, "Select destination folder")
            if destination:
                binary = f'./bin/{command}'
                arguments = [game, destination]
                self.start_process(binary, arguments)
            else:
                self.message("Select destination folder!")
        else:
            self.message("Select game!")

    def start_process(self, command, arguments):
        if self.p is None:
            self.message("Wait, Executing process...")
            self.p = QtCore.QProcess()
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.stateChanged.connect(self.handle_state)
            self.p.finished.connect(self.process_finished)
            self.p.start(command, arguments)

    def message(self, s):
        self.text.appendPlainText(s)

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.message(stderr)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def handle_state(self, state):
        states = {
            QtCore.QProcess.NotRunning: 'Not running',
            QtCore.QProcess.Starting: 'Starting...',
            QtCore.QProcess.Running: 'Running...',
        }
        state_name = states[state]
        self.message(f"State changed: {state_name}")

    def process_finished(self):
        self.message("Process finished! You can close the program now.")
        self.p = None


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
