#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;

int main()
{
    //创建一个空图像便于画图
    Mat background=Mat::zeros(480,640,CV_8UC3);

    //画线
    line(background,Point(50,50),Point(50,150),Scalar(0,0,255),5);

    //画点
    circle(background,Point(300,50),5,Scalar(0,0,255),-1);

    //画圆
    circle(background,Point(300,200),30,Scalar(255,0,0),5);

    //画矩形
    rectangle(background,Point(500,300),Point(600,450),Scalar(0,255,0),5);
    
    //显示图像
    imshow("Background",background);

    //等待按键关闭
    waitKey(0);
    return 0;
}