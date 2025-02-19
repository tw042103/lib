import cv2
import numpy as np

# 读取彩色图像
image = cv2.imread("C:/github/lib/LearnOpencv/1/c++/cqss.png")
if image is None:
    print("Error: Could not open or find the image!")
    exit()

#调整大小便于显示    
image=cv2.resize(image,(320,320),interpolation=cv2.INTER_AREA)

# 通道分离
B,G,R=cv2.split(image)

# 显示图像
cv2.imshow("R",R)
cv2.imshow("G",G)
cv2.imshow("B",B)
cv2.imshow("img",image)

# 等待按键关闭
cv2.waitKey(0)
