#include <iostream>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\opencv.hpp>
using namespace std;
using namespace cv;

int main()
{
    //读取图像
    Mat img=imread("C:/github/lib/LearnOpencv/1/c++/cqss.png");
    //分别对图像进行深浅拷贝
    Mat simg=img;
    Mat dimg=img.clone();
    for(int h=0;h<simg.rows;h++)
    {
        for(int w=0;w<simg.cols;w++)
        {
            //计算均值并赋值
            int average=(simg.at<Vec3b>(h,w)[0]+simg.at<Vec3b>(h,w)[1]+simg.at<Vec3b>(h,w)[2])/3;
            //用于存放RGB值
            int f;
            //与均值进行比较
            if(average>127) f=255;
            else f=0;
            //设置图像像素
            simg.at<Vec3b>(h,w)=Vec3b(f,f,f);
        }
    }
    for(int h=0;h<dimg.rows;h++)
    {
        for(int w=0;w<dimg.cols;w++)
        {
            //计算均值并赋值
            int average=(dimg.at<Vec3b>(h,w)[0]+dimg.at<Vec3b>(h,w)[1]+dimg.at<Vec3b>(h,w)[2])/3;
            //用于存放RGB值
            int f;
            //与均值进行比较
            if(average>127) f=255;
            else f=0;
            //设置图像像素
            dimg.at<Vec3b>(h,w)=Vec3b(f,f,f);
        }
    }
    //显示图像
    imshow("simg",simg);
    imshow("dimg",dimg);
    //等待按键关闭
    waitKey(0);
    return 0;
}