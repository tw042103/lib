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

# 遍历每个像素
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
        result[y, x] = [f, f, f]  # OpenCV 使用 BGR 顺序

# 显示原图和处理后的图像
cv2.imshow("Original Image", image)
cv2.imshow("Average Image", result)

# 等待按键
cv2.waitKey(0)

# 关闭窗口
cv2.destroyAllWindows()
