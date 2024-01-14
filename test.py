import cv2
import pyautogui
import numpy

while True:
    screen = pyautogui.screenshot(region=(484, 772, 913, 96))
    screen = numpy.array(screen)

    cv2.imshow("Screen", screen)

    cv2.waitKey(1)