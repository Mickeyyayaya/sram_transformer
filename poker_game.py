import pyautogui
from selenium import webdriver
from time import sleep
from PIL import Image

path = "C:/Users/m8974/Desktop/sram transformer/result.png"
path2 = "C:/Users/m8974/Desktop/sram transformer/result2.png"
# Open a web browser using Selenium
driver = webdriver.Edge()
driver.get('https://laijunbin.github.io/sevens/v1/index.html')
driver.set_window_size(1920,1080)
# Wait for the page to load
sleep(5)
# Use pyautogui to interact with elements
# For example, to click a button located at x=100, y=200
#region = (360,310,1040,560)
#region2 = (500,800,800,250)
#card_pool = pyautogui.screenshot(region=region)
#card_dock = pyautogui.screenshot(region=region2)
#test = pyautogui.screenshot(path)
pyautogui.useImageNotFoundException()
try:
    location = pyautogui.locateOnScreen('./card_new/card_back.jpg',confidence=0.4)
    print(location)
except pyautogui.ImageNotFoundException:
    print('ImageNotFoundException: image not found')

#card_pool.save(path)
#card_dock.save(path2)
#im = Image.open(path)
#im.show(path)
sleep(100)