import pyautogui
import time
import cv2
import pytesseract

import numpy as nm

time.sleep(1)
x, y = pyautogui.locateCenterOnScreen('img/calibration.png')

# whole grid
im = pyautogui.screenshot('img/grid.png',region=(x-200,y+190, 400, 400))

# first line
im = pyautogui.screenshot('img/line1.png',region=(x-195,y+200, 390, 65))

# first letter
im = pyautogui.screenshot('img/letter1.png',region=(x-195,y+200, 65, 65))

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
config = ('-l eng --oem 1 --psm 3')
im = cv2.imread('img/letter1.png', cv2.IMREAD_COLOR)
cv2.cvtColor(im,  cv2.COLOR_BGR2GRAY) 
tesstr = pytesseract.image_to_string(
                cv2.cvtColor(nm.array(im), cv2.COLOR_BGR2GRAY), 
                lang ='eng')
#text = pytesseract.image_to_string(im, config=config)
print('+----+')
print(tesstr)
print('+----+')