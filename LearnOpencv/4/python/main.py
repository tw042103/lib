import cv2
import numpy as np
import copy

# 读取彩色图像
image = cv2.imread("C:/github/lib/LearnOpencv/1/c++/cqss.png")
if image is None:
    print("Error: Could not open or find the image!")
    exit()

#分别对该图像进行深浅拷贝
copyimage=copy.copy(image)
dcopyimage=copy.deepcopy(image)

for y in range(copyimage.shape[0]):
    for x in range(copyimage.shape[1]):
        # 获取当前像素的 RGB 值
        pixel = copyimage[y, x]
        # 计算当前像素的均值
        average = int(np.mean(pixel))  
        # 根据均值设置结果图像的像素
        if average > 127:
            f = 255
        else:
            f = 0    
        # 设置结果图像的像素
        copyimage[y, x] = [f, f, f]  # OpenCV 使用 BGR 顺序

for y in range(dcopyimage.shape[0]):
    for x in range(dcopyimage.shape[1]):
        # 获取当前像素的 RGB 值
        pixel = dcopyimage[y, x]
        # 计算当前像素的均值
        average = int(np.mean(pixel))  
        # 根据均值设置结果图像的像素
        if average > 127:
            f = 255
        else:
            f = 0    
        # 设置结果图像的像素
        dcopyimage[y, x] = [f, f, f]  # OpenCV 使用 BGR 顺序

# 显示两种图像
cv2.imshow("CopyImage", copyimage)
cv2.imshow("DeepcopyImage", dcopyimage)

# 等待按键
cv2.waitKey(0)

# 关闭窗口
cv2.destroyAllWindows()
