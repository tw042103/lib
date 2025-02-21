import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img=cv2.imread("C:/github/lib/picture/9.png",cv2.IMREAD_GRAYSCALE)

# 定义结构元素
kernel=np.ones((5,5),np.uint8)

# 开运算（先腐蚀后膨胀）
transition1=cv2.erode(img,kernel,iterations=1)
result1=cv2.dilate(transition1,kernel,iterations=1)

# 闭运算（先膨胀后腐蚀）
transition2=cv2.dilate(img,kernel,iterations=1)
result2=cv2.erode(transition2,kernel,iterations=1)

#显示图像
cv2.imshow("Img",img)
cv2.imshow("Result1",result1)
cv2.imshow("Result2",result2)

#等待按键关闭
cv2.waitKey(0)