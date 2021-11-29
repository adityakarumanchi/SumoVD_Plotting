import numpy as np
import cv2
from mss import mss
from PIL import Image
import os
# import pyautogui

# output = "video.mkv"
# # img = pyautogui.screenshot()
# sct = mss()
# img = sct.shot()
# # img = np.array(img)
# img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
# # # get info from img
# height, width, channels = img.shape
# # # Define the codec and create VideoWriter object
# # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# # out = cv2.VideoWriter(output, fourcc, 30.0, (width, height))
# #
# # while True:
# #     try:
# #         # img = pyautogui.screenshot()
# #         img = sct.grab(img.shape)
# #         image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
# #         out.write(image)
# #         StopIteration(0.5)
# #     except KeyboardInterrupt:
# #         break
# #
# # out.release()
# # cv2.destroyAllWindows()

bounding_box = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

sct = mss()
output = "video.avi"

# # Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv2.VideoWriter(output, fourcc, 20, (bounding_box['width'], bounding_box['height']))

while True:
    # sct_img = np.array(sct.grab(bounding_box))
    # cv2.imshow('screen', sct_img)
    # out.write(sct_img)
    #
    # if (cv2.waitKey(1) & 0xFF) == ord('q'):
    #     cv2.destroyAllWindows()
    #     break
    try:
        sct_img = np.array(sct.grab(bounding_box))
        out.write(sct_img)
        # cv2.imshow('screen', sct_img)
    except KeyboardInterrupt:
        break

cv2.destroyAllWindows()
out.release()
