# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow4.ui'
#
# Created: Thu Mar  2 22:03:27 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 600))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {\n"
"\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.494, fy:0.494318, stop:0 rgba(0, 51, 75, 255), stop:1 rgba(0, 0, 0, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.676136 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(137, 137, 137, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.448864 rgba(60, 238, 241, 255), stop:1 rgba(0, 0, 0, 255));\n"
"}")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btn2 = QtWidgets.QPushButton(self.centralWidget)
        self.btn2.setGeometry(QtCore.QRect(780, 150, 211, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn1 = QtWidgets.QPushButton(self.centralWidget)
        self.btn1.setGeometry(QtCore.QRect(780, 20, 211, 121))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn3 = QtWidgets.QPushButton(self.centralWidget)
        self.btn3.setGeometry(QtCore.QRect(780, 280, 211, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.centralWidget)
        self.btn4.setGeometry(QtCore.QRect(780, 410, 211, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btnDial = QtWidgets.QPushButton(self.centralWidget)
        self.btnDial.setGeometry(QtCore.QRect(30, 150, 201, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btnDial.setFont(font)
        self.btnDial.setStyleSheet("")
        self.btnDial.setObjectName("btnDial")
        self.btnEnd = QtWidgets.QPushButton(self.centralWidget)
        self.btnEnd.setGeometry(QtCore.QRect(30, 410, 201, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btnEnd.setFont(font)
        self.btnEnd.setObjectName("btnEnd")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(260, 20, 491, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 491, 91))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.676136 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(137, 137, 137, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.448864 rgba(60, 238, 241, 255), stop:1 rgba(0, 0, 0, 255));\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 120, 361, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.448864 rgba(60, 238, 241, 255), stop:1 rgba(0, 0, 0, 255));\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.btnAnswer = QtWidgets.QPushButton(self.centralWidget)
        self.btnAnswer.setGeometry(QtCore.QRect(30, 280, 201, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btnAnswer.setFont(font)
        self.btnAnswer.setObjectName("btnAnswer")
        self.dig1 = QtWidgets.QPushButton(self.centralWidget)
        self.dig1.setGeometry(QtCore.QRect(260, 240, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.dig1.setFont(font)
        self.dig1.setObjectName("dig1")
        self.dig2 = QtWidgets.QPushButton(self.centralWidget)
        self.dig2.setGeometry(QtCore.QRect(390, 240, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.dig2.setFont(font)
        self.dig2.setObjectName("dig2")
        self.dig3 = QtWidgets.QPushButton(self.centralWidget)
        self.dig3.setGeometry(QtCore.QRect(520, 240, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.dig3.setFont(font)
        self.dig3.setObjectName("dig3")
        self.dig4 = QtWidgets.QPushButton(self.centralWidget)
        self.dig4.setGeometry(QtCore.QRect(260, 350, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.dig4.setFont(font)
        self.dig4.setObjectName("dig4")
        self.dig7 = QtWidgets.QPushButton(self.centralWidget)
        self.dig7.setGeometry(QtCore.QRect(260, 460, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.dig7.setFont(font)
        self.dig7.setObjectName("dig7")
        self.dig5 = QtWidgets.QPushButton(self.centralWidget)
        self.dig5.setGeometry(QtCore.QRect(390, 350, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.dig5.setFont(font)
        self.dig5.setObjectName("dig5")
        self.dig8 = QtWidgets.QPushButton(self.centralWidget)
        self.dig8.setGeometry(QtCore.QRect(390, 460, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.dig8.setFont(font)
        self.dig8.setObjectName("dig8")
        self.dig6 = QtWidgets.QPushButton(self.centralWidget)
        self.dig6.setGeometry(QtCore.QRect(520, 350, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.dig6.setFont(font)
        self.dig6.setObjectName("dig6")
        self.dig9 = QtWidgets.QPushButton(self.centralWidget)
        self.dig9.setGeometry(QtCore.QRect(520, 460, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.dig9.setFont(font)
        self.dig9.setObjectName("dig9")
        self.dig0 = QtWidgets.QPushButton(self.centralWidget)
        self.dig0.setGeometry(QtCore.QRect(650, 460, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.dig0.setFont(font)
        self.dig0.setObjectName("dig0")
        self.digHash = QtWidgets.QPushButton(self.centralWidget)
        self.digHash.setGeometry(QtCore.QRect(650, 350, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.digHash.setFont(font)
        self.digHash.setObjectName("digHash")
        self.digStar = QtWidgets.QPushButton(self.centralWidget)
        self.digStar.setGeometry(QtCore.QRect(650, 240, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.digStar.setFont(font)
        self.digStar.setObjectName("digStar")
        self.digBack = QtWidgets.QPushButton(self.centralWidget)
        self.digBack.setGeometry(QtCore.QRect(650, 120, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.digBack.setFont(font)
        self.digBack.setObjectName("digBack")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn2.setText(_translate("MainWindow", "Music"))
        self.btn1.setText(_translate("MainWindow", "Diagnostics"))
        self.btn3.setText(_translate("MainWindow", "Game"))
        self.btn4.setText(_translate("MainWindow", "Off"))
        self.btnDial.setText(_translate("MainWindow", "Dial"))
        self.btnEnd.setText(_translate("MainWindow", "End"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f5f5f5;\">Enter Phone Number</span></p></body></html>"))
        self.btnAnswer.setText(_translate("MainWindow", "Answer"))
        self.dig1.setText(_translate("MainWindow", "1"))
        self.dig2.setText(_translate("MainWindow", "2"))
        self.dig3.setText(_translate("MainWindow", "3"))
        self.dig4.setText(_translate("MainWindow", "4"))
        self.dig7.setText(_translate("MainWindow", "7"))
        self.dig5.setText(_translate("MainWindow", "5"))
        self.dig8.setText(_translate("MainWindow", "8"))
        self.dig6.setText(_translate("MainWindow", "6"))
        self.dig9.setText(_translate("MainWindow", "9"))
        self.dig0.setText(_translate("MainWindow", "0"))
        self.digHash.setText(_translate("MainWindow", "#"))
        self.digStar.setText(_translate("MainWindow", "*"))
        self.digBack.setText(_translate("MainWindow", "❮"))
