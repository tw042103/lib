#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/opencv.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <cmath>
using namespace std;
using namespace cv;

//建立Gamma变换函数
Mat Gammatransform(Mat &srcImage,float n)
{
    //建立LUT查找表，对应每个像素值的Gamma转化值
    unsigned char LUT[256];
    for(int i=0;i<256;i++)
    {
        float f = (i + 0.5f) / 255;
		f = (float)(pow(f, n));
		LUT[i] = saturate_cast<uchar>(f*255.0f - 0.5f);
    }
    //对图像进行深拷贝，以防在操作时影响原图像
    Mat resultImage=srcImage.clone();
    //单通道
    if(resultImage.channels()==1)
    {
        MatIterator_<uchar> iterator=resultImage.begin<uchar>();
        MatIterator_<uchar> iteratorEnd=resultImage.end<uchar>();
        for(;iterator<iteratorEnd;iterator++)
        {
            *iterator=LUT[(*iterator)];
        }
    }
    //多通道
    else
    {
        MatIterator_<Vec3b> iterator=resultImage.begin<Vec3b>();
        MatIterator_<Vec3b> iteratorEnd=resultImage.end<Vec3b>();
        for(;iterator<iteratorEnd;iterator++)
        {
            (*iterator)[0]=LUT[((*iterator)[0])];
            (*iterator)[1]=LUT[((*iterator)[1])];
            (*iterator)[2]=LUT[((*iterator)[2])];
        }
    }
    //返回所求图像
    return resultImage;
}

int main()
{
    //读取图像
    Mat img=imread("C:/github/lib/picture/6-1.jpg");
    //引用Gamma变换函数
    Mat result=Gammatransform(img,2.2);
    //显示图像
    imshow("img",img);
    imshow("gamma2.2",result);
    //等待按键关闭
    waitKey(0);
    return 0;
}