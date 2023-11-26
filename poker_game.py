import pygetwindow
import pyautogui
from PIL import Image


path = "C://Users/mickey/sram_transformer/result.png"
titles = pygetwindow.getAllTitles()

window = pygetwindow.getWindowsWithTitle('Sevens')[0]

left, top = window.topleft
right, bottom = window.bottomright
pyautogui.screenshot(path)
im = Image.open(path)
#im = im.crop((left,top,right,bottom))
#im.save(path)
im.show(path)