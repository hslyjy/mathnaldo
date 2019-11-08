import sys
from PyQt5.QtWidgets import *
import pyautogui as m
import coordinates
import time
import executeui
import json

class SecretPopupUI(QWidget):
    memberData = ["경재하","이한솔","이지선","최인재","정하욱","리테일개발그룹","김성훈","김홍준", "박장순", "박원석"]   
    
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(0, 0, 300, 50)
        self.center()
        self.setWindowTitle("멤버 확인")
        self.lb = QLabel("누구십니까")
        self.et = QLineEdit()
        self.checkBtn = QPushButton("확인")

        layout = QVBoxLayout()
        layout.addWidget(self.lb)
        layout.addWidget(self.et)
        layout.addWidget(self.checkBtn)

        self.setLayout(layout)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def checkMember(self, dialog):
        if self.et.text().strip() in self.memberData:
            QMessageBox.about(None, "멤버 확인", "확인되었습니다.")
            dialog.show()
            dialog.sec.destroy()
            
        else :
            QMessageBox.about(None, "멤버가 아니시군요..", "빠이...")
            dialog.sec.destroy()
            sys.exit()


