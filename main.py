import cv2
import pydirectinput
import keyboard
import time
import pyautogui
import numpy

def main():
    run = True
    locate = False

    # Capture the initial screenshot
    img = pyautogui.screenshot("img.jpg", region=(484, 772, 913, 96))
    img = numpy.asarray(img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    # make the threshold for the confidence detection
    threshold = 0.95

    while run:
        # Capture the current screenshot
        screen = pyautogui.screenshot(region=(484, 772, 913, 96))
        screen = numpy.asarray(screen)
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

        loc_image = cv2.matchTemplate(screen, img_gray, cv2.TM_CCOEFF_NORMED)

        # Check if the thing should start running
        if keyboard.is_pressed("r"):
            locate = True
        elif keyboard.is_pressed("t"):
            locate = False

        if locate:
            extracted_image = loc_image[0][0]

            if extracted_image <= threshold:
                print(extracted_image)
                pydirectinput.leftClick()
                time.sleep(5)
                pydirectinput.leftClick()
                cv2.imwrite("img.jpg", img)
        else:
            cv2.imwrite("img.jpg", img)

if __name__ == "__main__":
    main()
