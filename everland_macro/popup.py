import sys
from PyQt5.QtWidgets import *
import pyautogui as m
import coordinates
import time
import executeui
import json

class PopupUI(QWidget):
    saveData = {"coord1":{"x":0,"y":0}, "coord2":{"x":0,"y":0}, "coord3":{"x":0,"y":0}, "coord4":{"x":0,"y":0}, "coord5":{"x":0,"y":0}}
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(0, 0, 300, 50)
        self.center()
        self.lb = QLabel("저장할 파일 이름")
        self.et = QLineEdit()
        self.saveBtn = QPushButton("Save")

        self.saveBtn.clicked.connect(lambda: self.saveFile(self.et.text()))

        layout = QVBoxLayout()
        layout.addWidget(self.lb)
        layout.addWidget(self.et)
        layout.addWidget(self.saveBtn)

        self.setLayout(layout)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def saveFile(self, fileName):
        with open('{0}.json'.format(fileName), 'w', encoding="utf-8") as make_file:
            json.dump(self.saveData, make_file, ensure_ascii=False)

        QMessageBox.about(None, "저장 확인", "저장되었습니다.")
        self.destroy()