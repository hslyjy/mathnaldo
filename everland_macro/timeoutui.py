from PyQt5.QtWidgets import *

class TimeOutUI(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.slbl = QLabel("                                             Time Out")
        self.timeout = QLineEdit("0")

        layout = QHBoxLayout()
        layout.addWidget(self.slbl)
        layout.addWidget(self.timeout)
        self.setLayout(layout)

    def getTimeOut(self):
        if self.timeout.text() == '':
            return 0
        else :
            return float(self.timeout.text())
    
    def setTimeOut(self, sleepTime):
        self.timeout.setText(str(sleepTime))