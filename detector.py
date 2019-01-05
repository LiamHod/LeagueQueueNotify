import numpy as np
import cv2
from mss import mss
import mss.tools
import winGuiAuto
import win32gui



def window_location():
    """Finds the location of the League window on the desktop"""
    try:
        league_win = winGuiAuto.findTopWindow("League of Legends")
    except:
        return None
    if win32gui.IsWindowVisible(league_win) and not win32gui.IsIconic(league_win):
        win_loc = win32gui.GetWindowPlacement(league_win)[-1]
        return win_loc
    else:
        return None


def grab_screen(coordinates):
    """Grabs a screenshot from the coordinated provided"""
    with mss.mss() as sct:
        # print("League window coordinates: ", coordinates)
        league_img = np.array(sct.grab(coordinates))
        return league_img

def detect_queue(cur_img, template_path, threshold):
    """Used OpenCV to detect if the queue has popped in the image"""
    try:
        template = cv2.imread(template_path, 0)
    except cv2.error:
        print('Incorrect file path for template image')
    # template = cv2.imread('templateimages\\reg_queue.png', 0)
    #w, h = template.shape[::-1]
    grey_img = cv2.cvtColor(cur_img, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)
    lol_loc = np.where(res >= threshold)
    return bool(lol_loc[0].any())
    """Used this part to print rectangle around detected image"""
    # for pt in zip(*lol_loc[::-1]):
    #     if pt:
    #         cv2.rectangle(cur_img, pt, (pt[0]+ w, pt[1] + h), (0, 225, 255), 2)
    #         cv2.imshow('Detected', cur_img)
    #         cv2.waitKey(0)
