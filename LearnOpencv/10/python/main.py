import cv2
import numpy as np

def gaussian_kernel(size,sigma):
    kernel=np.zeros((size,size))
    for x in range(size):
        for y in range(size):
            kernel[x,y]=1/(2*np.pi*sigma*sigma)*np.exp(-(x*x+y*y)/(2*sigma*sigma))
    return kernel

def conv(image,kernel):
    Hi,Wi=image.shape
    Hk,Wk=kernel.shape
    out=np.zeros((Hi,Wi))

    # 边缘处理
    pad_width0=Hk//2 #对卷积高度进行整除，计算需要填充的宽度
    pad_width1=Wk//2
    pad_width=((pad_width0,pad_width0),(pad_width1,pad_width1)) #建立一个元组整合填充宽度
    padded=np.pad(image,pad_width,mode='edge') #np.pad 函数用于对输入图像进行填充，这里使用了 mode='edge'，表示用边缘值填充，这样可以在卷积时避免边界效应

    for i in range(pad_width0,Hi+pad_width0):
        for j in range(pad_width1,Wi+pad_width1):
            split_img=padded[i-pad_width0:i+pad_width0+1,j-pad_width1:j+pad_width1+1]# 提取当前卷积核所覆盖的图像区域
            out[i-pad_width0, j-pad_width1] = np.sum(np.multiply(split_img, kernel))
    return out

# 非极大值抑制函数
def non_maximum_suppression(img,theta):
    H,W=img.shape
    out=np.zeros((H,W))
    theta=np.floor((theta+22.5)/45)*45 #使用 np.floor 函数对上一步的结果进行向下取整
    anchor=np.stack(np.where(img!=0)).T 
    for x,y in anchor:
        center_point=img[x,y]
        current_theta=theta[x,y]
        dTmp1=0
        dTmp2=0
        if current_theta==0:
            dTmp1=img[x,y-1]
            dTmp2=img[x,y+1]
        elif current_theta==45:
            dTmp1=img[x+1,y-1]
            dTmp2=img[x-1,y+1]
        elif current_theta==90 or current_theta==-90:
            dTmp1=img[x-1,y]
            dTmp2=img[x+1,y]
        elif current_theta==-45:
            dTmp1=img[x-1,y-1]
            dTmp2=img[x+1,y+1]
        if (center_point>=dTmp1 and center_point>=dTmp2): out[x,y]=center_point
    return out

# 双阈值
def double_thresholding(img,high,low):
    strong_edges=np.zeros(img.shape,dtype=np.bool_)
    weak_edges=np.zeros(img.shape,dtype=np.bool_)
    H,W=img.shape
    for i in range(0,H):
        for j in range(0,W):
            if(img[i,j]>high):strong_edges[i,j]=True
            elif(img[i,j]>=low):weak_edges[i,j]=True
    return strong_edges,weak_edges

def get_neighbors(y,x,H,W):
    neighbors=[]
    for i in (y-1,y,y+1):
        for j in (x-1,x,x+1):
            if(i>=0 and i<H and j>=0 and j<W ):
                if(i==y and j==x):continue
                neighbors.append((i,j))
    return neighbors

def link_edges(strong_edges,weak_edges):
    H,W=strong_edges.shape
    indices=np.stack(np.nonzero(strong_edges)).T
    edge=np.zeros((H,W),dtype=bool)
    for x,y in indices:
        edge[x,y]=True
        neighbors=get_neighbors(x,y,H,W)
        for neighbor in neighbors:
            if(weak_edges[neighbor]==True):edge[neighbor]=True
    return edge

# 读取图像
img=cv2.imread("C:/github/lib/LearnOpencv/1/c++/cqss.png",cv2.IMREAD_GRAYSCALE)

# 缩放图像
img=cv2.resize(img,(640,480),interpolation=cv2.INTER_AREA) 

# 调用函数进行图像平滑操作
kernel=gaussian_kernel(3,1.4)
smoothed=conv(img,kernel)

#计算梯度大小和方向
sobel_x=cv2.Sobel(smoothed,cv2.CV_64F,1,0,ksize=3)
sobel_x=cv2.convertScaleAbs(sobel_x)
sobel_y=cv2.Sobel(smoothed,cv2.CV_64F,0,1,ksize=3)
sobel_y=cv2.convertScaleAbs(sobel_y)
sobel_xy=cv2.addWeighted(sobel_x,0.5,sobel_y,0.5,0) #将两个维度的图像加在一起
theta=np.degrees(np.arctan2(sobel_y,sobel_x)) #计算梯度方向

#非极大值抑制
thinned=non_maximum_suppression(sobel_xy,theta)

strong_edges,weak_edges=double_thresholding(thinned,250,100)
edges=link_edges(strong_edges,weak_edges)
edges=(edges*255).astype(np.uint8)

# 显示图片
cv2.imshow("Smoothed",smoothed.astype(np.uint8))
cv2.imshow("Sobel_xy",sobel_xy.astype(np.uint8))
cv2.imshow("Thinned",thinned.astype(np.uint8))
cv2.imshow("Edges",edges)

# 等待按键关闭
cv2.waitKey(0)

