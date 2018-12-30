import numpy as np
import cv2
import pywinauto
import win32gui
import win32com
import win32com.client
import winGuiAuto
from mss import mss
import mss.tools
from PIL import Image
from matplotlib import pyplot as plt


def window_location():
    """Finds the location of the League window on the desktop"""
    while True:
        league_win = winGuiAuto.findTopWindow("League of Legends")
        #print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
        #print("Visible?:", win32gui.IsWindowVisible(league_win))
        if win32gui.IsWindowVisible(league_win) and not win32gui.IsIconic(league_win):
            win_loc = win32gui.GetWindowPlacement(league_win)[-1]
            grab_screen(win_loc)
        else:
            print("window not visible")


def grab_screen(coordinates):
    """Grabs a screenshot from the coordinated provided"""
    # sct = mss()
    with mss.mss() as sct:
        # print("League window coordinates: ", coordinates)
        sct_img = np.array(sct.grab(coordinates))
        detect_queue(sct_img)
        # mss.tools.to_png(sct_img.rgb, sct_img.size,level=6, output="testimage.png")   

def detect_queue(cur_img):
    """Used OpenCV to detect if the queue has popped in the image"""
    template = cv2.imread('templateimages\\winter_queue.png', 0)
    w, h = template.shape[::-1]
    grey_img = cv2.cvtColor(cur_img, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    lol_loc = np.where(res >= threshold)
    for pt in zip(*lol_loc[::-1]):
        if pt:
            cv2.rectangle(cur_img, pt, (pt[0]+ w, pt[1] + h), (0, 225, 255), 2)
            cv2.imshow('Detected', cur_img)
            cv2.waitKey(0)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     top_left = max_loc
#     bottom_right = (top_left[0] + w, top_left[1] + h)

#     cv2.rectangle(cur_img, top_left, bottom_right, 255, 2)

#     plt.subplot(121), plt.imshow(res, cmap='gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122), plt.imshow(cur_img, cmap='gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(method)

#     plt.show()

window_location()
