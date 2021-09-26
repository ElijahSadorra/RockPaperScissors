import os

import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

folderPath = "Pictures"
fingers = os.listdir(folderPath)
fingerList = []
for i in fingers:
    image = cv2.imread(f'{folderPath}/{i}')
    fingerList.append(image)

capture = cv2.VideoCapture(0)
detector = htm.handDetector()
tipIDs = [4, 8, 12, 16, 20]

while True:
    success, img = capture.read()
    img = detector.findHands(img, draw = False)

    l1_list = detector.findposition(img, 0)

    if (len(l1_list) != 0):
        fingers = []

        if l1_list[tipIDs[0]][1] < l1_list[tipIDs[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for i in range(1, 5):
            if l1_list[tipIDs[i]][2] < l1_list[tipIDs[i]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        if fingers == [0,0,0,0,0]:
            h, w, c = fingerList[0].shape
            img[0:h, 0:w] = fingerList[0]
        elif fingers == [1,1,1,1,1]:
            h, w, c = fingerList[2].shape
            img[0:h, 0:w] = fingerList[2]
        elif fingers == [0,1,1,0,0]:
            h, w, c = fingerList[1].shape
            img[0:h, 0:w] = fingerList[1]

    cv2.imshow("Image", img)
    cv2.waitKey(1)