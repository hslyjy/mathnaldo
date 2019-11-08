from PyQt5.QtWidgets import *

class CoordinatesUI(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.xlbl = QLabel("x 좌표")
        self.ylbl = QLabel("y 좌표")
        self.xord = QLineEdit()
        self.yord = QLineEdit()
        self.getCoordBtn = QPushButton("현재 좌표 가져오기")

        layout = QHBoxLayout()
        layout.addWidget(self.xlbl)
        layout.addWidget(self.xord)
        layout.addWidget(self.ylbl)
        layout.addWidget(self.yord)
        layout.addWidget(self.getCoordBtn)
        self.setLayout(layout)

    def getXord(self):
        if self.xord.text() == '':
            return 0
        else :
            return int(self.xord.text())

    def getYord(self):
        if self.yord.text() == '':
            return 0
        else :
            return int(self.yord.text())
    
    def setCoord(self, coord):
        self.xord.setText(str(coord["x"])) 
        self.yord.setText(str(coord["y"]))

