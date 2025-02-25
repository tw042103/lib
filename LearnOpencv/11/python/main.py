import cv2
import numpy as np

# 读取图像
img=cv2.imread("C:/github/lib/picture/11.png",cv2.IMREAD_GRAYSCALE)

# 调用函数
retval,labels,stats,centroids=cv2.connectedComponentsWithStats(img,connectivity=8)

