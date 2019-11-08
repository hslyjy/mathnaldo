from PyQt5.QtWidgets import *

class SleepTimeUI(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.slbl = QLabel("                                           Sleep Time")
        self.sleepTime = QLineEdit("0")

        layout = QHBoxLayout()
        layout.addWidget(self.slbl)
        layout.addWidget(self.sleepTime)
        self.setLayout(layout)

    def getSleepTime(self):
        if self.sleepTime.text() == '':
            return 0
        else :
            return float(self.sleepTime.text())
    
    def setSleepTIme(self, sleepTime):
        self.sleepTime.setText(str(sleepTime))

