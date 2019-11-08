import sys
import pyautogui as m
import coordinates, executeui, popup, loadpopup, secretpopup, timerui, timeoutui, sleeptimeui, imageprocess
import time
import json
import threading
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyDialog(QDialog):
    globX = 0
    globY = 0
    isImgUse = False
    
    def __init__(self):
        QDialog.__init__(self)
        self.setFixedSize(340, 820)
        self.center()
        self.setWindowTitle("예약 매크로")
        self.setMouseTracking(False)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        #레이블, Edit, 버튼 컨트롤

        #이미지 영역
        self.imgCheckbox = QCheckBox("이미지 파일로 실행하기")
        self.coordImglbl1 = QLabel("이미지 검색 영역 처음 좌표")
        self.coordImg1 = coordinates.CoordinatesUI()
        self.coordImglbl2 = QLabel("이미지 검색 영역 마지막 좌표")
        self.coordImg2 = coordinates.CoordinatesUI()
        self.timeoutui = timeoutui.TimeOutUI()
        self.coordImg1.setEnabled(False)
        self.coordImg2.setEnabled(False)

        #좌표 영역
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
        
        # 이벤트 실행 영역
        self.executeui.btnOk.clicked.connect(self.clickPlayBtn)
        self.executeui.btnSave.clicked.connect(self.clickSaveBtn)
        self.executeui.btnLoad.clicked.connect(self.clickLoadBtn)
        
        self.coordImg1.getCoordBtn.clicked.connect(lambda: self.coordImg1.setCoord({"x":self.globX, "y":self.globY}))
        self.coordImg2.getCoordBtn.clicked.connect(lambda: self.coordImg2.setCoord({"x":self.globX, "y":self.globY}))
        self.coord1.getCoordBtn.clicked.connect(lambda: self.coord1.setCoord({"x":self.globX, "y":self.globY}))
        self.coord2.getCoordBtn.clicked.connect(lambda: self.coord2.setCoord({"x":self.globX, "y":self.globY}))
        self.coord3.getCoordBtn.clicked.connect(lambda: self.coord3.setCoord({"x":self.globX, "y":self.globY}))
        self.coord4.getCoordBtn.clicked.connect(lambda: self.coord4.setCoord({"x":self.globX, "y":self.globY}))
        self.coord5.getCoordBtn.clicked.connect(lambda: self.coord5.setCoord({"x":self.globX, "y":self.globY}))

        # 타이머 영역
        self.timerui.executeBtn.clicked.connect(self.executeTimer)

        #이미지 체크박스 클릭 이벤트
        self.imgCheckbox.stateChanged.connect(self.clickImgCheckBox)

        layout = QVBoxLayout()
        layout.addWidget(self.imgCheckbox)
        layout.addWidget(self.coordImglbl1)
        layout.addWidget(self.coordImg1)
        layout.addWidget(self.coordImglbl2)
        layout.addWidget(self.coordImg2)
        layout.addWidget(self.timeoutui)
        layout.addWidget(QLabel("----------------------------------------------------"))
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
        if self.isImgUse == False :
            m.click(x=self.coord1.getXord(), y=self.coord1.getYord(), clicks=1)
            time.sleep(self.sleepTime1.getSleepTime())
            m.click(x=self.coord2.getXord(), y=self.coord2.getYord(), clicks=1)
            time.sleep(self.sleepTime2.getSleepTime())
            m.click(x=self.coord3.getXord(), y=self.coord3.getYord(), clicks=1)
            time.sleep(self.sleepTime3.getSleepTime())
            m.click(x=self.coord4.getXord(), y=self.coord4.getYord(), clicks=1)
            time.sleep(self.sleepTime4.getSleepTime())
            m.click(x=self.coord5.getXord(), y=self.coord5.getYord(), clicks=1)
        else :
            imageProcessorClass = imageprocess.ImageProcessorClass()
            imageProcessorClass.setTimeout(self.timeoutui.getTimeOut())
            imageProcessorClass.setImages(imageprocess.searchImages())

            self.checkEmptyStringAndSetZero(self.coordImg1.xord)
            self.checkEmptyStringAndSetZero(self.coordImg1.yord)
            self.checkEmptyStringAndSetZero(self.coordImg2.xord)
            self.checkEmptyStringAndSetZero(self.coordImg2.yord)

            imageProcessorClass.setRoiPosition(
                (int(self.coordImg1.xord.text()), int(self.coordImg1.yord.text())),
                (int(self.coordImg2.xord.text()), int(self.coordImg2.yord.text())))
            
            imageProcessorClass.playImageMacro()

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

    def clickImgCheckBox(self):
        if self.imgCheckbox.isChecked():
            self.isImgUse = True
            self.disableAllCoord()
        else :
            self.isImgUse = False
            self.disableAllCoord()

    def disableAllCoord(self):
        self.coordImg1.setEnabled(self.isImgUse == True)
        self.coordImg2.setEnabled(self.isImgUse == True)
        self.timeoutui.timeout.setEnabled(self.isImgUse == True)
        self.coord1.setEnabled(self.isImgUse == False) 
        self.coord2.setEnabled(self.isImgUse == False) 
        self.coord3.setEnabled(self.isImgUse == False) 
        self.coord4.setEnabled(self.isImgUse == False) 
        self.coord5.setEnabled(self.isImgUse == False) 
        self.sleepTime1.setEnabled(self.isImgUse == False)
        self.sleepTime2.setEnabled(self.isImgUse == False)
        self.sleepTime3.setEnabled(self.isImgUse == False)
        self.sleepTime4.setEnabled(self.isImgUse == False)
        self.executeui.btnSave.setEnabled(self.isImgUse == False) 
        self.executeui.btnLoad.setEnabled(self.isImgUse == False)
        
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

    def checkEmptyStringAndSetZero(self, item):
        if item.text().strip() == "":
            item.setText("0")
        

app = QApplication([])
dialog = MyDialog()
dialog.sec.show()
dialog.sec.checkBtn.clicked.connect(lambda: dialog.sec.checkMember(dialog))

app.exec_()

