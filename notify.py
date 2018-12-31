import numpy as np
import cv2
from mss import mss
import mss.tools
import winGuiAuto
import win32gui



def window_location():
    """Finds the location of the League window on the desktop"""
    while True:
        # league_win = winGuiAuto.findTopWindow("League of Legends")
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
        print("League window coordinates: ", coordinates)
        sct_img = np.array(sct.grab(coordinates))
        detect_queue(sct_img)
        # mss.tools.to_png(sct_img.rgb, sct_img.size,level=6, output="testimage.png")   

def detect_queue(cur_img):
    """Used OpenCV to detect if the queue has popped in the image"""
    template = cv2.imread('templateimages\\winter_queue.png', 0)
    # template = cv2.imread('templateimages\\reg_queue.png', 0)
    w, h = template.shape[::-1]
    grey_img = cv2.cvtColor(cur_img, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    lol_loc = np.where(res >= threshold)
    print(lol_loc)
    print(lol_loc[0])
    if lol_loc[0].any():
        print("found queue")
        exit(0)
    """Used this part to print rectangle around detected image"""
    # for pt in zip(*lol_loc[::-1]):
    #     if pt:
    #         cv2.rectangle(cur_img, pt, (pt[0]+ w, pt[1] + h), (0, 225, 255), 2)
    #         cv2.imshow('Detected', cur_img)
    #         cv2.waitKey(0)

window_location()
