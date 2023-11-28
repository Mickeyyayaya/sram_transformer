import pyautogui
from selenium import webdriver
from time import sleep
from PIL import Image
import cv2
import numpy as np


def check_card(source,target,thr): 

    main_image = cv2.imread(source)
    template = cv2.imread(target)


    main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


    res = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    threshold = thr
    loc = np.where(res >= threshold)
    a = None

    
    for pt in zip(*loc[::-1]):
        a = pt
        cv2.rectangle(main_image, pt, (pt[0] + template.shape[1], pt[0] + template.shape[0]), (0,255,255), 2)

    '''
    cv2.imshow('Detected', main_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    return a


path = "C:/Users/mickey/sram_transformer/result.png"
path2 = "C:/Users/mickey/sram_transformer/result2.png"

driver = webdriver.Edge()
driver.get('https://laijunbin.github.io/sevens/v1/index.html')
driver.maximize_window()

for x in range(13):
    sleep(5)

    # capture the dock and the pool of the game
    region = (360,310,1040,480)
    region2 = (500,800,800,250)
    card_pool = pyautogui.screenshot(region=region)
    card_dock = pyautogui.screenshot(region=region2)
    test = pyautogui.screenshot(path)
    card_pool.save(path)
    card_dock.save(path2)
    
    ## Justify the card num and position
    club_card = []
    diamond_card = []
    heart_card = []
    spade_card = []
    pool_card = np.zeros((4,2))
    pool_card[:, 0] = 999
    a = []
    loca = []
    club_pos = []
    diamond_pos = []
    heart_pos = []
    spade_pos = []


    for i in range(52):
        if i <= 12:
            loc = check_card('C:/Users/mickey/sram_transformer/result2.png',f'C:/Users/mickey/sram_transformer/card_new/club_{i+1}.png',0.98)
            loc2 = check_card('C:/Users/mickey/sram_transformer/result.png',f'C:/Users/mickey/sram_transformer/card_new/club_{i+1}.png',0.9)
            if loc != None:
                club_card.append(i+1)
                club_pos.append(loc)
            if loc2 != None:
                if pool_card[0][0] > i+1 :
                    pool_card[0][0] = i+1
                if pool_card[0][1] < i+1:
                    pool_card[0][1] = i+1
        elif i > 12 and i <=25:
            loc = check_card('C:/Users/mickey/sram_transformer/result2.png',f'C:/Users/mickey/sram_transformer/card_new/diamond_{i-12}.png',0.98)
            loc2 = check_card('C:/Users/mickey/sram_transformer/result.png',f'C:/Users/mickey/sram_transformer/card_new/diamond_{i-12}.png',0.9)
            if loc != None:
                diamond_card.append(i-12)
                diamond_pos.append(loc)
            if loc2 != None:
                if pool_card[1][0] > i-12 :
                    pool_card[1][0] = i-12
                if pool_card[1][1] < i-12:
                    pool_card[1][1] = i-12
        elif i > 25 and i <= 38:
            loc = check_card('C:/Users/mickey/sram_transformer/result2.png',f'C:/Users/mickey/sram_transformer/card_new/heart_{i-25}.png',0.98)
            loc2 = check_card('C:/Users/mickey/sram_transformer/result.png',f'C:/Users/mickey/sram_transformer/card_new/heart_{i-25}.png',0.9)
            if loc != None:
                heart_card.append(i-25)
                heart_pos.append(loc)
            if loc2 != None:
                
                if pool_card[2][0] > i-25 :
                    pool_card[2][0] = i-25
                if pool_card[2][1] < i-25:
                    pool_card[2][1] = i-25
        elif i > 38 and i <= 51:
            loc = check_card('C:/Users/mickey/sram_transformer/result2.png',f'C:/Users/mickey/sram_transformer/card_new/spade_{i-38}.png',0.98)
            loc2 = check_card('C:/Users/mickey/sram_transformer/result.png',f'C:/Users/mickey/sram_transformer/card_new/spade_{i-38}.png',0.9)
            if loc != None:
                spade_card.append(i-38)
                spade_pos.append(loc)
            if loc2 != None:
                if pool_card[3][0] > i-38 :
                    pool_card[3][0] = i-38 
                if pool_card[3][1] < i-38:
                    pool_card[3][1] = i-38
    
    print(pool_card)
    if x == 0 and 7 in club_card:
        max = len(club_card)
        a = club_card
        loca = club_pos
        if 7 in diamond_card:
            if max < len(diamond_card):
                max = len(diamond_card)
                a = diamond_card
                loca = diamond_pos
        if 7 in heart_card:
            if max < len(heart_card):
                max = len(heart_card)
                loca = heart_pos
                a = heart_card
        if 7 in spade_card:
            if max < len(spade_card):
                max = len(spade_card)
                a = spade_card
                loca = spade_pos
        pyautogui.click(loca[a.index(7)][0]+500,loca[a.index(7)][1]+800)
    
    else:
        # send 7 first
        if 7 in club_card:
            pyautogui.click(club_pos[club_card.index(7)][0]+500,club_pos[club_card.index(7)][1]+800)
            continue
        if 7 in diamond_card: 
            pyautogui.click(diamond_pos[diamond_card.index(7)][0]+500,diamond_pos[diamond_card.index(7)][1]+800)
        if 7 in heart_card:
            pyautogui.click(heart_pos[heart_card.index(7)][0]+500,heart_pos[heart_card.index(7)][1]+800)
            continue
        if 7 in spade_card: 
            pyautogui.click(spade_pos[spade_card.index(7)][0]+500,spade_pos[spade_card.index(7)][1]+800)
            continue
        # send another card
        if pool_card[0][0]-1 in club_card:
            pyautogui.click(club_pos[club_card.index(pool_card[0][0]-1)][0]+500,club_pos[club_card.index(pool_card[0][0]-1)][1]+800)
            continue
        elif pool_card[0][1]+1 in club_card:
            pyautogui.click(club_pos[club_card.index(pool_card[0][1]+1)][0]+500,club_pos[club_card.index(pool_card[0][1]+1)][1]+800)
            continue
        if pool_card[1][0]-1 in diamond_card:
            pyautogui.click(diamond_pos[diamond_card.index(pool_card[1][0]-1)][0]+500,diamond_pos[diamond_card.index(pool_card[1][0]-1)][1]+800)
            continue
        elif pool_card[1][1]+1 in diamond_card:
            pyautogui.click(diamond_pos[diamond_card.index(pool_card[1][1]+1)][0]+500,diamond_pos[diamond_card.index(pool_card[1][1]+1)][1]+800)
            continue
        if pool_card[2][0]-1 in heart_card:
            pyautogui.click(heart_pos[heart_card.index(pool_card[2][0]-1)][0]+500,heart_pos[heart_card.index(pool_card[2][0]-1)][1]+800)
            continue
        elif pool_card[2][1]+1 in heart_card:
            pyautogui.click(heart_pos[heart_card.index(pool_card[2][1]+1)][0]+500,heart_pos[heart_card.index(pool_card[2][1]+1)][1]+800)
            continue
        if pool_card[3][0]-1 in spade_card:
            pyautogui.click(spade_pos[spade_card.index(pool_card[3][0]-1)][0]+500,spade_pos[spade_card.index(pool_card[3][0]-1)][1]+800)
            continue
        elif pool_card[3][1]+1 in spade_card:
            pyautogui.click(spade_pos[spade_card.index(pool_card[3][1]+1)][0]+500,spade_pos[spade_card.index(pool_card[3][1]+1)][1]+800)
            continue



sleep(100)