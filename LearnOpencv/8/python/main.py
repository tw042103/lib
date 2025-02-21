import cv2
import numpy as np

# 创建一个空图像便于画图
background=np.zeros((480,640,3),dtype=np.uint8)

# 画线
cv2.line(background,(50,50),(50,150),(0,0,255),5)

#画点
cv2.circle(background,(300,50),5,(0,0,255),-1)

#画圆
cv2.circle(background,(300,200),30,(255,0,0),5)

#画矩形
cv2.rectangle(background,(500,300),(600,450),(0,255,0),5)

# 显示图像
cv2.imshow("Background",background)

# 等待按键关闭
cv2.waitKey(0)
