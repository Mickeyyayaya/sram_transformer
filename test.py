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
    
    #cv2.imshow('Detected', main_image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    return a

club_card = []
diamond_card = []
heart_card = []
spade_card = []
pool_card = np.zeros((4,2))
pool_card[:, 0] = 999

club_pos = []
diamond_pos = []
heart_pos = []
spade_pos = []

for i in range(52):
    if i <= 12:
        loc = check_card('C:/Users/mickey/sram_transformer/result2.png',f'C:/Users/mickey/sram_transformer/card_new/club_{i+1}.png',0.98)
        loc2 = check_card('C:/Users/mickey/sram_transformer/result3.png',f'C:/Users/mickey/sram_transformer/card_new/club_{i+1}.png',0.9)
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
        loc2 = check_card('C:/Users/mickey/sram_transformer/result3.png',f'C:/Users/mickey/sram_transformer/card_new/diamond_{i-12}.png',0.9)
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
        loc2 = check_card('C:/Users/mickey/sram_transformer/result3.png',f'C:/Users/mickey/sram_transformer/card_new/heart_{i-25}.png',0.9)
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
        loc2 = check_card('C:/Users/mickey/sram_transformer/result3.png',f'C:/Users/mickey/sram_transformer/card_new/spade_{i-38}.png',0.9)
        if loc != None:
            spade_card.append(i-38)
            spade_pos.append(loc)
        if loc2 != None:
            if pool_card[3][0] > i-38 :
                pool_card[3][0] = i-38
            if pool_card[3][1] < i-38:
                pool_card[3][1] = i-38

print(club_card)
print(club_pos)

print(diamond_card)
print(diamond_pos)

print(heart_card)
print(heart_pos)

print(spade_card)
print(spade_pos)

print(pool_card)