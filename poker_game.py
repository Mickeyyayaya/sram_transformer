import pyautogui
from selenium import webdriver
from time import sleep
from PIL import Image

path = "C:/Users/mickey/sram_transformer/result.png"
path2 = "C:/Users/mickey/sram_transformer/result2.png"
# Open a web browser using Selenium
driver = webdriver.Edge()
driver.get('https://laijunbin.github.io/sevens/v1/index.html')

# Wait for the page to load
sleep(5)
# Use pyautogui to interact with elements
# For example, to click a button located at x=100, y=200
region = (360,310,1040,560)
region2 = (500,800,800,250)
card_pool = pyautogui.screenshot(region=region)
card_dock = pyautogui.screenshot(region=region2)
card_pool.save(path)
card_dock.save(path2)
im = Image.open(path2)
im.show(path2)
sleep(100)