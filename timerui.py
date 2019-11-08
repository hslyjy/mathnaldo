import time
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import threading

class TimerUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.xlbl = QLabel("실행 시간")
        self.et1 = QLineEdit("09")
        self.xlb2 = QLabel(":")
        self.et2 = QLineEdit("00")
        self.currentTime = QLabel("현재시간")
        self.executeBtn = QPushButton("타이머 실행")
        layout = QHBoxLayout()
        layout.addWidget(self.xlbl)
        layout.addWidget(self.et1)
        layout.addWidget(self.xlb2)
        layout.addWidget(self.et2)
        layout.addWidget(self.currentTime)
        layout.addWidget(self.executeBtn)
        self.setLayout(layout)

        self.et1.resize(10,10)
        self.et2.resize(10,10)



        
    

        


