import sys
import cv2
import time
import pyautogui
import numpy as np
import os
from PyQt5.QtWidgets import *

class ImageProcessorClass:
    def __init__(self):
        self.images = []
        self.roiFirstPos = (0, 0)
        self.roiSecondPos = (0, 0)
        self.timeout = 0.0

    def setTimeout(self, timeout):
        self.timeout = timeout

    def setImages(self, images) :
        self.images = images
    
    def setRoiPosition(self, roiFirstPos, roiSecondPos) :
        self.roiFirstPos = roiFirstPos
        self.roiSecondPos = roiSecondPos

    def playImageMacro(self):
        for macroImage in self.images :
            start_time = time.time()

            while True:
                current_time = time.time() # 현재 시간을 받아온다.
                
                if( current_time - start_time > self.timeout): # 프로그램을 20초 동안만 실행
                    print("Time Out")
                    # sys.exit(0) # 정상종료 코드
                    
                    QMessageBox.about(None, "이미지 검색 실패", "이미지를 찾을 수 없습니다.ㅠㅠ")
                    time.sleep(1)
                    return  

                sourceImage = getImageOfROI( self.roiFirstPos, self.roiSecondPos ) # im에 roi의 이미지를 저장
                if sourceImage == None:
                    print("Error - can't capture image of ROI")
                    sys.exit(1)
                
                pos = getImageLoc(sourceImage, macroImage, 0.82, self.roiFirstPos)
                if pos == ():
                    print("image not found", macroImage)
                else:
                    print(macroImage, " position : ", pos) 
                    imageClicks( macroImage, pos )
                    # time.sleep(0.1) # delay
                    break


def getImageOfROI( p1, p2 ): # -> roi를 스크린샷으로 찍은 이미지
    im = pyautogui.screenshot(region= p1+p2) # roi를 스크린샷으로 찍음
    return im

def getImageLoc(image, tpl, precision, p1) :
    img_rgb = np.array(image)
    # opencv가 b g r 순서대로 처리하기 떄문에 b 와 r의 순서를 바꿔준다
    b, g, r = cv2.split(img_rgb)
    img_bgr = cv2.merge([r,g,b])

    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(tpl, 0) # 0은 cv.IMREAD_GRAYSCALE을 의미
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)    

    position = np.where(res >= precision) # 이미지에서 template의 위치를 받아온다.    
    locations = list()
    for point in zip(*position[::-1]):
        x = point[0] + p1[0]
        y = point[1] + p1[1]
        cv2.circle(img_bgr, point, 1, (0, 0, 255), 1) # 반지름이 1px인 점을 그린다
        abs_pos = x, y
        locations.append(abs_pos)        
    
    # cv2.imwrite('C:/modules/mole_catching/image/captured.png', img_bgr) # result를 저장
        
    return tuple(locations)

def imageClicks(image, pos):
    img = cv2.imread(image)
    height, width, channels = img.shape
    
    for p in pos:
        x = p[0] + width/2
        y = p[1] + height/2
        pyautogui.click( x, y )
        print('클릭 성공!!')

def searchImages():
    images = []
    for i in range(1,10):
        fileName = ""
        if os.path.isfile(".\\image\\macro{0}.png".format(i)) :
            fileName = ".\\image\\macro{0}.png".format(i)
        elif os.path.isfile(".\\image\\macro{0}.jpg".format(i)) :
            fileName = ".\\image\\macro{0}.jpg".format(i)
        elif os.path.isfile(".\\image\\macro{0}.PNG".format(i)) :
            fileName = ".\\image\\macro{0}.jpg".format(i)
        if fileName != "":
            images.append(fileName)
    return images
