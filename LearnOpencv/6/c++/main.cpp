#include <iostream>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\opencv.hpp>
#include <opencv2\imgproc\imgproc.hpp>
#include <cmath>
using namespace std;
using namespace cv;

Mat Gammatransform(Mat &srcImage,float n)
{
    unsigned char LUT[256];
    for(int i=0;i<256;i++)
    {
        float a=(i=0.5)/256;
        a=pow(a,1/n);
        LUT[i]=saturate_cast<uchar>(a*256.0f-0.5f);
    }
    Mat resultImage=srcImage.clone();
    if(resultImage.channels()==1)
    {
        MatIterator_<uchar> iterator=resultImage.begin<uchar>();
        MatIterator_<uchar> iteratorEnd=resultImage.end<uchar>();
        for(;iterator<=iteratorEnd;iterator++)
        {
            *iterator=LUT[(*iterator)];
        }
    }
    else
    {
        MatIterator_<Vec3b> iterator=resultImage.begin<Vec3b>();
        MatIterator_<Vec3b> iteratorEnd=resultImage.end<Vec3b>();
        for(;iterator<=iteratorEnd;iterator++)
        {
            (*iterator)[0]=LUT[((*iterator)[0])];
            (*iterator)[1]=LUT[((*iterator)[1])];
            (*iterator)[2]=LUT[((*iterator)[2])];
        }
    }
    return resultImage;
}

int main()
{
    //读取图像
    Mat img=imread("C:/github/lib/picture/6-1.jpg");
    Mat result=Gammatransform(img,2.2);
    imshow("img",img);
    imshow("result",result);
    waitKey(0);
    return 0;
}