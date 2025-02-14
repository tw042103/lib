import cv2 as cv

# 读取图片
image = cv.imread('cqss.png')

# 创建一个全屏窗口
cv.namedWindow('FullScreen', cv.WND_PROP_FULLSCREEN)
cv.setWindowProperty('FullScreen', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

# 显示图片
cv.imshow('FullScreen', image)

# 等待用户按键
cv.waitKey(0)

# 关闭窗口
cv.destroyAllWindows()
