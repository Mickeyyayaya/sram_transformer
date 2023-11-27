import cv2
import numpy as np

# 讀取圖片
main_image = cv2.imread('result.png')
template = cv2.imread('card_new/test4.png')

# 轉為灰度圖
main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# 模板匹配
res = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
print(loc)

# 標記匹配區域
for pt in zip(*loc[::-1]):
    cv2.rectangle(main_image, pt, (pt[0] + template.shape[1], pt[0] + template.shape[0]), (0,255,255), 2)

# 顯示結果
cv2.imshow('Detected', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
