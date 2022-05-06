'''
Created on May 5, 2022

@author: calch
'''
import pyautogui
import pytesseract
from PIL import ImageGrab
import cv2
stringcount = []
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
stringcount = []
finallist = []
maxnum = []
counter = 0
numberlist = {'0','1','2','3','4','5','6','7','8','9','?'}
rollButton = (460,946)
topline = (367,454,1512,772)
def rollChar():
    pyautogui.click(rollButton)
def getStats():
    stringcount.clear()
    ImageGrab.grab(topline).save('s.png')
    imageStr2 = cv2.imread('s.png')
    stringcount.append((pytesseract.image_to_string(cv2.threshold(src=cv2.cvtColor(imageStr2, cv2.COLOR_BGR2GRAY), thresh=0, maxval=255, type=cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1])))
    finallist2 = []
    finallist.clear()
    for x in stringcount:
        for z in x:
            if z in numberlist:
                finallist2.append(z)             
    for y in range(0,len(finallist2),2):
        if finallist2[y] == '?':
            number1 = 7
        else:
            number1 = int(finallist2[y])
        number1 *= 10
        if finallist2[y+1] == '?':
            number2 = 7
        else:
            number2 = int(finallist2[y+1])
        finalnumber = number1 + number2
        finallist.append(finalnumber)
    maxnum.append(sum(finallist))
    maxnum.sort()
    while len(maxnum) > 10:
        del maxnum[maxnum.index(min(maxnum))]
    print(sum(finallist))
    print(maxnum)    
while sum(finallist) < 500:
    rollChar()
    getStats()
    counter += 1
print(counter)


