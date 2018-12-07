import numpy as np
import cv2
import pywinauto
import win32gui
import winGuiAuto
from mss import mss
from PIL import Image

findWin = winGuiAuto.findTopWindow("League of Legends")
winLoc = win32gui.GetWindowPlacement(findWin)[-1]
print(winLoc)