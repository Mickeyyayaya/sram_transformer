import pyautogui
from selenium import webdriver
from time import sleep
from PIL import Image
import cv2
import numpy as np


def check_card(source,target,thr): 
    #def test
    # 讀取圖片
    main_image = cv2.imread(source)
    template = cv2.imread(target)

    # 轉為灰度圖
    main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # 模板匹配
    res = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    threshold = thr
    loc = np.where(res >= threshold)
    a = None
    # 標記匹配區域
    
    for pt in zip(*loc[::-1]):
        a = pt
        cv2.rectangle(main_image, pt, (pt[0] + template.shape[1], pt[0] + template.shape[0]), (0,255,255), 2)

    # 顯示結果
    '''
    cv2.imshow('Detected', main_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    return a


path = "C:/Users/mickey/sram_transformer/result.png"
path2 = "C:/Users/mickey/sram_transformer/result2.png"
# Open a web browser using Selenium
driver = webdriver.Edge()
driver.get('https://laijunbin.github.io/sevens/v1/index.html')
driver.maximize_window()
# Wait for the page to load
while 1:
    sleep(5)
    # Use pyautogui to interact with elements
    # For example, to click a button located at x=100, y=200
    region = (360,310,1040,560)
    region2 = (500,800,800,250)
    card_pool = pyautogui.screenshot(region=region)
    card_dock = pyautogui.screenshot(region=region2)
    test = pyautogui.screenshot(path)

    card_pool.save(path)
    card_dock.save(path2)
    
    loc = check_card('C:/Users/mickey/sram_transformer/result2.png','C:/Users/mickey/sram_transformer/card_new/club_7.png',0.9)
    num_seconds=5
    pyautogui.moveTo(loc[0]+500,loc[1]+800,duration=num_seconds)

sleep(100)