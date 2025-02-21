import cv2
import numpy as np

# 读取彩色图像
image = cv2.imread("C:/github/lib/picture/p2.jpg")
if image is None:
    print("Error: Could not open or find the image!")
    exit()

# 调整大小便于显示    
image=cv2.resize(image,(320,320),interpolation=cv2.INTER_AREA)

# 通道分离
hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

# 定义红色的HSV范围
lower_red1=np.array([0,100,100])
upper_red1=np.array([10,255,255])  
lower_red2=np.array([160,100,100]) 
upper_red2=np.array([180,255,255])

# 获得红色区域掩码
mask_red1=cv2.inRange(hsv_image,lower_red1,upper_red1)
mask_red2=cv2.inRange(hsv_image,lower_red2,upper_red2)
mask_red=cv2.bitwise_or(mask_red1,mask_red2)

# 定义蓝色的HSV范围
lower_blue=np.array([100,100,100])   
upper_blue=np.array([140,255,255])

# 获得蓝色区域掩码
mask_blue=cv2.inRange(hsv_image,lower_blue,upper_blue)

# 利用掩码分别提取红色与蓝色部分
red_extracted=cv2.bitwise_and(image,image,mask=mask_red)
blue_extracted=cv2.bitwise_and(image,image,mask=mask_blue)

# 显示图像
cv2.imshow("Original Image",image)
cv2.imshow("Red_Extraced",red_extracted)
cv2.imshow("Blue_Extraced",blue_extracted)

# 等待按键关闭
cv2.waitKey(0)