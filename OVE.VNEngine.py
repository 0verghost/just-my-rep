from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import *
import sqlite3
import sys
import os
from os import makedirs
from os.path import exists
from PyQt5.QtWidgets import QMenuBar

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OVE.TNEngine")#окно
        self.setGeometry(150, 110, 1500, 900)
        self.setStyleSheet('background-color: #4287f5')
        self.setFixedSize(1500, 900)#окно
#----------------------------------------------------------------------------
        self.foundation = QLabel('OVE Computer Techologies©️', self)
        self.foundation.setGeometry(1200, 730, 498, 280)

        self.numpaterninf = QLabel('Стили', self)
        self.numpaterninf.setGeometry(780, 750, 200, 20)

        self.buttonForward = QPushButton('>', self)
        self.buttonForward.setGeometry(800, 800, 200, 20)
        self.buttonForward.clicked.connect(self.PaternForward)

        self.buttonBack = QPushButton('<', self)
        self.buttonBack.setGeometry(595, 800, 200, 20)
        self.buttonBack.clicked.connect(self.PaternBack)
        self.buttonBack.setEnabled(False)

        self.textbutton = QPushButton(self)
        self.textbutton.setGeometry(1,1,200,200)
        self.textbutton.clicked.connect(self.test)
        self.textbutton.setHidden(True)

        self.mainwin = QLabel(self)#расположение патернов
        self.mainwin.setGeometry(120, 200, 750, 450)
        self.mainwin.setStyleSheet('background-color:white')

        self.SetColor = QTextEdit('#ffffff', self)
        self.SetColor.setStyleSheet('background-color: white')
        self.SetColor.setGeometry(900, 350, 100, 30)
        self.buttonSetColor = QPushButton('Установить цвет', self)
        self.buttonSetColor.setGeometry(900, 400, 150, 30)
        self.buttonSetColor.clicked.connect(self.SetColorwin)

        #future update
        # self.posYofADDBUTTON = 50
        # self.buttonADDBUTTON = QPushButton('+ Добавить кнопку', self)
        # self.buttonADDBUTTON.setGeometry(1250, self.posYofADDBUTTON, 200, 50)
        # self.buttonADDBUTTON.clicked.connect(self.MoveButton)
        #future update

        #Menu setings of button
        self.LableButtonMenu = QLabel(self)
        self.LableButtonMenu.setGeometry(1120, 50, 350, 150)
        self.LableButtonMenu.setStyleSheet('background-color: white')

        self.nameButton = QTextEdit('Name Button', self)
        self.nameButton.setGeometry(1125, 52, 130, 30)
        self.nameButton.setStyleSheet('background-color:#ebeae8')

        self.PosXButton = QTextEdit('X', self)
        self.PosXButton.setGeometry(1125, 92, 50, 30)
        self.PosXButton.setStyleSheet('background-color:#ebeae8')

        self.PosYButton = QTextEdit('Y',self)
        self.PosYButton.setGeometry(1185, 92, 50, 30)
        self.PosYButton.setStyleSheet('background-color:#ebeae8')

        self.setButtonSettings = QPushButton('Принять изменения', self)
        self.setButtonSettings.setGeometry(1200, 142, 170, 40)

        self.setColorButton = QPushButton('')
        # Menu setings of button

#---------------------------------------------------------------------------




#---------------------------------------------------------------------------
        self.paternNum = 0#переменная номеров патернов

        self.show()


    def test(self):
        print('test')
    def PaternForward(self):
        self.paternNum += 1
        self.PaternsMainWindow()
        self.EnabledRules()

    def PaternBack(self):
        self.paternNum -= 1
        self.PaternsMainWindow()
        self.EnabledRules()

    def PaternsMainWindow(self):#список патернов
        self.buttonNext = QPushButton("Дальше", self)
        self.buttonNext.setStyleSheet('background-color:gray')
        self.buttonNext.setGeometry(350, 620, 50, 20)

        self.buttonEntry = QPushButton("Ввести", self)
        self.buttonEntry.setStyleSheet('background-color:gray')
        self.buttonEntry.setGeometry(550, 620, 50, 20)


        #x +200, y +200
        if self.paternNum == 1:
            self.buttonNext.setGeometry(350, 620, 50, 20)
            self.buttonEntry.setGeometry(550, 620, 50, 20)
            self.textgame.setGeometry(250, 250, 150, 120)
            self.screenGame.setGeometry(650, 320, 70, 50)
        if self.paternNum == 2:
            self.buttonEntry.setGeometry(350, 620, 50, 20)
        if self.paternNum == 3:
            self.mainwin.setStyleSheet('background-color: white')
        if self.paternNum == 4:
            self.mainwin.setStyleSheet('background-color: black')
    def EnabledRules(self):#условия активации и деактивации кнопок
        if self.paternNum > 1:
            self.buttonBack.setEnabled(True)
        if self.paternNum <= 1:
            self.buttonBack.setEnabled(False)
        if self.paternNum >= 4:
            self.buttonForward.setEnabled(False)
        if self.paternNum < 4:
            self.buttonForward.setEnabled(True)
#-----------------------------------------------------------------------
    def SetColorwin(self):
        colorName = self.SetColor.toPlainText()
        try:
            self.mainwin.setStyleSheet(f'background-color:{colorName}')
        except:
            self.mainwin.setStyleSheet('background-color:red')#i dont know why they dont catch the error

    def MoveButton(self):
        self.posYofADDBUTTON += 100
        self.buttonADDBUTTON.setGeometry(1250, self.posYofADDBUTTON, 200, 50)
        self.textbutton.setHidden(False)


App = QApplication(sys.argv)
priv = MainWindow()
sys.exit(App.exec())