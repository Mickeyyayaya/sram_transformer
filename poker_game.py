import pyautogui
from selenium import webdriver
from time import sleep
from PIL import Image

path = "C:/Users/mickey/sram_transformer/result.png"
# Open a web browser using Selenium
driver = webdriver.Edge()
driver.get('https://laijunbin.github.io/sevens/v1/index.html')

# Wait for the page to load
sleep(5)
# Use pyautogui to interact with elements
# For example, to click a button located at x=100, y=200
region = (360,310,1040,560)
screenshot = pyautogui.screenshot(region=region)
screenshot.save(path)
im = Image.open(path)
im.show(path)
sleep(100)