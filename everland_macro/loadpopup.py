import sys
from PyQt5.QtWidgets import *
import pyautogui as m
import coordinates
import time
import executeui
import json
import os

class LoadPopupUI(QWidget):
    saveData = {"coord1":{"x":0,"y":0}, "coord2":{"x":0,"y":0}, "coord3":{"x":0,"y":0}, "coord4":{"x":0,"y":0}, "coord5":{"x":0,"y":0}}
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(0, 0, 300, 50)
        self.center()
        self.lb = QLabel("불러올 파일 이름")
        self.et = QLineEdit()
        self.loadBtn = QPushButton("Load")

        layout = QVBoxLayout()
        layout.addWidget(self.lb)
        layout.addWidget(self.et)
        layout.addWidget(self.loadBtn)

        self.setLayout(layout)
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def loadFile(self, loadFunc):
        loadFunc()
        
