import cv2
import numpy as np

# 读取图像
img=cv2.imread("C:/github/lib/picture/11.png",cv2.IMREAD_GRAYSCALE)

# 通过图像阈值分割将原图转化位二值图像
thresh=85
thresh,binary_img=cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)

# 通过闭运算去除黑噪点
kernel=np.ones((3,3),np.uint8)
closing=cv2.morphologyEx(binary_img,cv2.MORPH_CLOSE,kernel)

# 调用函数
retval,labels,stats,centroids=cv2.connectedComponentsWithStats(closing,connectivity=8)

# 输出硬币数量
print("num=",retval-1)

# 绘制硬币重心
k=0
for x,y in centroids:
    k=k+1
    if k==1:continue
    cv2.circle(closing,(int(x),int(y)),3,(0,0,255),-1)

# 显示图像
cv2.imshow("Origin Img",img)
cv2.imshow("Closing",closing)

# 等待按键关闭
cv2.waitKey(0)