# Import Needed Libraries
import sys
import os
import time
#Import Needed Gui Classes
import PyQt5
from PyQt5.QtWidgets import *

#Import Gui script
import mainwindow_auto

#Main Gui Class
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    ### functions for the buttons to call
    
    def pressed1Button(self):
        print ("Pressed Diagnostics!")

    def pressed2Button(self):
        print ("Pressed Music!")

    def pressed3Button(self):
        print ("Pressed Game!")
        #os.system("python3 main.py")

    def pressed4Button(self):
        print ("Pressed Off!")
        os.system('reboot')

    def pressedDialButton(self):
        print ("Pressed Dial!")
        phoneNumber= self.lineEdit.text()
        print (phoneNumber)
        wrt = open("/dev/ttyUSB0", "w")
        wrt.write('AT\r')
        time.sleep(0.5)
        wrt.write('ATD')
        time.sleep(0.5)
        wrt.write(phoneNumber)
        time.sleep(0.5)
        wrt.write(';\r')
        wrt.close()

    def pressedEndButton(self):
        print ("Pressed End!")
        wrt = open("/dev/ttyUSB0", "w")
        wrt.write('ATH\r')
        wrt.close()

    def pressedAnswerButton(self):
        print ("Pressed Answer!")
        wrt = open("/dev/ttyUSB0", "w")
        wrt.write('ATA\r')
        wrt.close()

    def pressedDig1(self):
        self.lineEdit.insert('1')
    def pressedDig1(self):
        self.lineEdit.insert('1')
    def pressedDig1(self):
        self.lineEdit.insert('1')
    def pressedDig2(self):
        self.lineEdit.insert('2')
    def pressedDig3(self):
        self.lineEdit.insert('3')
    def pressedDig4(self):
        self.lineEdit.insert('4')
    def pressedDig5(self):
        self.lineEdit.insert('5')
    def pressedDig6(self):
        self.lineEdit.insert('6')
    def pressedDig7(self):
        self.lineEdit.insert('7')
    def pressedDig8(self):
        self.lineEdit.insert('8')
    def pressedDig9(self):
        self.lineEdit.insert('9')
    def pressedDig0(self):
        self.lineEdit.insert('0')
    def pressedDigStar(self):
        self.lineEdit.insert('*')
    def pressedDigHash(self):
        self.lineEdit.insert('#')
    def pressedDigBack(self):
        self.lineEdit.backspace()


    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        ### Hooks to for buttons
        self.btn1.clicked.connect(lambda: self.pressed1Button())
        self.btn2.clicked.connect(lambda: self.pressed2Button())
        self.btn3.clicked.connect(lambda: self.pressed3Button())
        self.btn4.clicked.connect(lambda: self.pressed4Button())
        self.btnDial.clicked.connect(lambda: self.pressedDialButton())
        self.btnEnd.clicked.connect(lambda: self.pressedEndButton())        
        self.btnAnswer.clicked.connect(lambda: self.pressedAnswerButton())
        ### keypad button hooks
        self.dig1.clicked.connect(lambda: self.pressedDig1())
        self.dig2.clicked.connect(lambda: self.pressedDig2())
        self.dig3.clicked.connect(lambda: self.pressedDig3())
        self.dig4.clicked.connect(lambda: self.pressedDig4())
        self.dig5.clicked.connect(lambda: self.pressedDig5())
        self.dig6.clicked.connect(lambda: self.pressedDig6())
        self.dig7.clicked.connect(lambda: self.pressedDig7())
        self.dig8.clicked.connect(lambda: self.pressedDig8())
        self.dig9.clicked.connect(lambda: self.pressedDig9())
        self.dig0.clicked.connect(lambda: self.pressedDig0())
        self.digStar.clicked.connect(lambda: self.pressedDigStar())
        self.digHash.clicked.connect(lambda: self.pressedDigHash())
        self.digBack.clicked.connect(lambda: self.pressedDigBack())

def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    #Stops script from exiting instantly
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
