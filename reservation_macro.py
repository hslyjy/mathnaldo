import sys
import pyautogui as m
import coordinates, executeui, popup, loadpopup, secretpopup, timerui, sleeptimeui
import time
import json
import threading
import os
import psutil
from PyQt5.QtWidgets import *

class MyDialog(QDialog):
    globX = 0
    globY = 0
    def __init__(self):
        QDialog.__init__(self)
        self.setGeometry(0, 0, 300, 500)
        self.center()
        self.setWindowTitle("예약 매크로")
        self.setMouseTracking(False)
        #레이블, Edit, 버튼 컨트롤
        self.coordlb1 = QLabel("예약 버튼 좌표")
        self.coordlb2 = QLabel("선택 드롭다운 좌표")
        self.coordlb3 = QLabel("매수 좌표")
        self.coordlb4 = QLabel("신청 버튼 좌표")
        self.coordlb5 = QLabel("확인 버튼 좌표")
        self.coord1 = coordinates.CoordinatesUI()
        self.coord2 = coordinates.CoordinatesUI()
        self.coord3 = coordinates.CoordinatesUI()
        self.coord4 = coordinates.CoordinatesUI()
        self.coord5 = coordinates.CoordinatesUI()
        self.sleepTime1 = sleeptimeui.SleepTimeUI()
        self.sleepTime2 = sleeptimeui.SleepTimeUI()
        self.sleepTime3 = sleeptimeui.SleepTimeUI()
        self.sleepTime4 = sleeptimeui.SleepTimeUI()
        self.executeui = executeui.ExecuteUI()
        self.timerui = timerui.TimerUI()
        self.exp24 = QLabel("실행 시간은 24시 표기법 입니다.")
        self.currentOrd = QLabel("마우스를 클릭한채로 움직이면 좌표가 보입니다.")
        
        self.executeui.btnOk.clicked.connect(self.clickPlayBtn)
        self.executeui.btnSave.clicked.connect(self.clickSaveBtn)
        self.executeui.btnLoad.clicked.connect(self.clickLoadBtn)
        
        self.coord1.getCoordBtn.clicked.connect(lambda: self.coord1.setCoord({"x":self.globX, "y":self.globY}))
        self.coord2.getCoordBtn.clicked.connect(lambda: self.coord2.setCoord({"x":self.globX, "y":self.globY}))
        self.coord3.getCoordBtn.clicked.connect(lambda: self.coord3.setCoord({"x":self.globX, "y":self.globY}))
        self.coord4.getCoordBtn.clicked.connect(lambda: self.coord4.setCoord({"x":self.globX, "y":self.globY}))
        self.coord5.getCoordBtn.clicked.connect(lambda: self.coord5.setCoord({"x":self.globX, "y":self.globY}))

        self.timerui.executeBtn.clicked.connect(self.executeTimer)

        layout = QVBoxLayout()
        layout.addWidget(self.coordlb1)
        layout.addWidget(self.coord1)
        layout.addWidget(self.sleepTime1)
        layout.addWidget(self.coordlb2)
        layout.addWidget(self.coord2)
        layout.addWidget(self.sleepTime2)
        layout.addWidget(self.coordlb3)
        layout.addWidget(self.coord3)
        layout.addWidget(self.sleepTime3)
        layout.addWidget(self.coordlb4)
        layout.addWidget(self.coord4)
        layout.addWidget(self.sleepTime4)
        layout.addWidget(self.coordlb5)
        layout.addWidget(self.coord5)
        layout.addWidget(self.executeui)
        layout.addWidget(self.timerui)
        layout.addWidget(self.exp24)
        layout.addWidget(self.currentOrd)
        self.setLayout(layout)
        self.sec = secretpopup.SecretPopupUI()
        self.thread = threading.Thread(target = self.run)
        self.thread.running = False

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        self.globX = x
        self.globY = y
        text = "현재 좌표 : x = {0}, y = {1} ".format(x, y)
        self.currentOrd.setText(text)

    def clickPlayBtn(self):
        m.click(x=self.coord1.getXord(), y=self.coord1.getYord(), clicks=1)
        time.sleep(self.sleepTime1.getSleepTime())
        m.click(x=self.coord2.getXord(), y=self.coord2.getYord(), clicks=1)
        time.sleep(self.sleepTime2.getSleepTime())
        m.click(x=self.coord3.getXord(), y=self.coord3.getYord(), clicks=1)
        time.sleep(self.sleepTime3.getSleepTime())
        m.click(x=self.coord4.getXord(), y=self.coord4.getYord(), clicks=1)
        time.sleep(self.sleepTime4.getSleepTime())
        m.click(x=self.coord5.getXord(), y=self.coord5.getYord(), clicks=1)

    def clickSaveBtn(self):
        self.w = popup.PopupUI()
        saveData = self.w.saveData
        saveData["coord1"]["x"] = self.coord1.getXord()
        saveData["coord1"]["y"] = self.coord1.getYord()
        saveData["coord2"]["x"] = self.coord2.getXord()
        saveData["coord2"]["y"] = self.coord2.getYord()
        saveData["coord3"]["x"] = self.coord3.getXord()
        saveData["coord3"]["y"] = self.coord3.getYord()
        saveData["coord4"]["x"] = self.coord4.getXord()
        saveData["coord4"]["y"] = self.coord4.getYord()
        saveData["coord5"]["x"] = self.coord5.getXord()
        saveData["coord5"]["y"] = self.coord5.getYord()
        saveData["sleepTime1"] = self.sleepTime1.getSleepTime()
        saveData["sleepTime2"] = self.sleepTime2.getSleepTime()
        saveData["sleepTime3"] = self.sleepTime3.getSleepTime()
        saveData["sleepTime4"] = self.sleepTime4.getSleepTime()
        self.w.saveData = saveData
        self.w.show()
        
    def clickLoadBtn(self):
        
        self.w = loadpopup.LoadPopupUI()
        self.w.loadBtn.clicked.connect(lambda: self.w.loadFile(self.loadFunc))
        self.w.show()
        
    def loadFunc(self):
        fileName = self.w.et.text()
        if os.path.isfile("{0}.json".format(fileName)) == False:
            QMessageBox.about(None, "불러오기 실패", "파일을 찾을 수 없습니다.")
            return
        with open("{0}.json".format(fileName)) as json_file:
            saveFile = json.load(json_file)
            
            self.coord1.setCoord(saveFile["coord1"])
            self.coord2.setCoord(saveFile["coord2"])
            self.coord3.setCoord(saveFile["coord3"])
            self.coord4.setCoord(saveFile["coord4"])
            self.coord5.setCoord(saveFile["coord5"])
            self.sleepTime1.setSleepTIme(saveFile["sleepTime1"])
            self.sleepTime2.setSleepTIme(saveFile["sleepTime2"])
            self.sleepTime3.setSleepTIme(saveFile["sleepTime3"])
            self.sleepTime4.setSleepTIme(saveFile["sleepTime4"])
        self.w.destroy()
        QMessageBox.about(None, "불러오기 완료", "파일을 불러왔습니다.")

    def executeTimer(self):
        self.currentHour = self.timerui.et1.text()
        self.currentMinute = self.timerui.et2.text()
        QMessageBox.about(None, "타이머 실행!!", "{0}시 {1}분에 매크로가 실행됩니다.".format(self.currentHour, self.currentMinute))
        if self.thread.isAlive() == False:
            self.thread = threading.Thread(target = self.run)
            self.thread.start()
        
    def run(self):
        self.thread.running = True
        print("현재 시간 : {0}:{1}:{2}".format(00, 00, 00), end="")
        self.timerui.currentTime.setText("{0}:{1}:{2}".format(str(00), str(00), str(00)))
        while self.thread.running == True:
            
            lcTime = time.localtime(time.time())
            currentHour = lcTime[3]
            currentMinute = lcTime[4]
            currentSec = lcTime[5]
            self.timerui.currentTime.setText("{0}:{1}:{2}".format(str(currentHour), str(currentMinute), str(currentSec)))
            print("\r현재 시간 : {0}:{1}:{2}".format(currentHour, currentMinute, currentSec), end="")
           
            if currentHour == int(self.currentHour) and currentMinute == int(self.currentMinute):
                
                self.clickPlayBtn()
                self.thread.running = False
                self.timerui.currentTime.setText("현재 시간")
                self.thread.join()

                return

    def closeEvent(self, event):
        if self.thread.isAlive() == True:
            self.thread = threading.Thread(target = self.run)
        while self.thread.isAlive() == True:
            time.sleep(1)
            
        sys.exit()

app = QApplication([])
dialog = MyDialog()
dialog.sec.show()
dialog.sec.checkBtn.clicked.connect(lambda: dialog.sec.checkMember(dialog))

app.exec_()
