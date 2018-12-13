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


def window_location():
	findWin = winGuiAuto.findTopWindow("League of Legends")
	if win32gui.IsWindowVisible(findWin) and not win32gui.IsIconic(findWin):
		winLoc = win32gui.GetWindowPlacement(findWin)[-1]
		#shell = win32com.client.Dispatch("Wscript.Shell")
		#success = shell.AppActivate("League of Legends")
		#print(winLoc)
		grab_screen(winLoc)
	else:
		print("window not visible")


def grab_screen(coordinates):
    #sct = mss()
    with mss.mss() as sct:
        print("League window coordinates: ",coordinates)
        sct_img = sct.grab(coordinates)
        #mss.tools.to_png(sct_img.rgb, sct_img.size,level=6, output="testimage.png")   

window_location()
