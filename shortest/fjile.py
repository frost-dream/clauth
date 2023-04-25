import pyautogui
import cv2
import numpy as np
out = cv2.VideoWriter('file.avi', cv2.VideoWriter_fourcc(*"XVID"), 1000, (1920,1080))
out.write(cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_BGR2RGB))
out.release()
