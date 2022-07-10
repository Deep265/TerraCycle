import cv2
import numpy as np


green = np.uint8([[[0, 255, 0]]])  #green color
hsvGreen = cv2.cvtColor(green, cv2.COLOR_BGR2HSV) #hsv value of green color
print(hsvGreen)

lowerLimit = hsvGreen[0][0][0] - 10, 100, 100  # range of green color lower limit and upper limit
upperLimit = hsvGreen[0][0][0] + 10, 255, 255

print(upperLimit)
print(lowerLimit)

red = np.uint8([[[0, 0, 255]]]) #red color
hsvred = cv2.cvtColor(red, cv2.COLOR_BGR2HSV) #hsv value of red color
print(hsvred)

lower = hsvred[0][0][0] - 10, 100, 100 # range of red color lower limit and upper limit
upper = hsvred[0][0][0] + 10, 255, 255

print(upper)
print(lower)

# image = cv2.imread(r'Apple.jpg') #load your image
image1 = cv2.VideoCapture('http://192.168.82.110:8080/video')
# arduino
from cvzone.SerialModule import SerialObject
from time import sleep

arduino = SerialObject("COM5")


while True:
    ret,image = image1.read()
    image = cv2.resize(image,(600,400))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # convert the image into hsv

    lg = np.array(lowerLimit)  # range of green color
    ug = np.array(upperLimit)

    cv2.imshow('frame',image)

    green_mask = cv2.inRange(hsv, lg, ug)  # green masked image
    #cv2.imshow('green', green_mask)  # show the image

    lr = np.array(lower)  # range of red color
    ur = np.array(upper)

    red_mask = cv2.inRange(hsv, lr, ur)  # red masked image
    #cv2.imshow('red', red_mask)  # show the image
    # bool maker
    bo = 0
    total1 = 0
    g = np.squeeze(green_mask)
    for i in range(len(g)):
        for j in range(len(g[i])):
            total1 = total1 + g[i][j]





    if total1 > 10000:
        bo = 4
    else:
        bo = -1


    if bo:
        print('green',total1)



    arduino.sendData([bo])

    rd = 0
    bo = 0
    key = cv2.waitKey(1)
    if key == ord('q'):
        break



image1.release()
cv2.destroyAllWindows()