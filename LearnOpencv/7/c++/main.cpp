#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;

int main()
{
    //读取图像
    Mat img=imread("C:/github/lib/picture/p2.jpg");
    
    //通道分离
    Mat hsv_img;
    cvtColor(img,hsv_img,COLOR_BGR2HSV);
    
    //定义红色的HSV范围
    Scalar lower_red1(0, 100, 100);
    Scalar upper_red1(10, 255, 255);
    Scalar lower_red2(160, 100, 100);
    Scalar upper_red2(180, 255, 255);

    //获得红色区域掩码
    Mat mark_red1,mark_red2,mark_red;
    inRange(hsv_img,lower_red1,upper_red1,mark_red1);
    inRange(hsv_img,lower_red2,upper_red2,mark_red2);
    bitwise_or(mark_red1,mark_red2,mark_red);

    //定义蓝色的HSV范围
    Scalar lower_blue(100, 100, 100);
    Scalar upper_blue(140, 255, 255);

    //获得蓝色区域掩码
    Mat mark_blue;
    inRange(hsv_img,lower_blue,upper_blue,mark_blue);

    //利用掩码分别提取红色与蓝色部分
    Mat red_extracted,blue_extracted;
    bitwise_and(img,img,red_extracted,mark_red);
    bitwise_and(img,img,blue_extracted,mark_blue);

    //显示图像
    imshow("Original Img",img);
    imshow("Red_Extracted",red_extracted);
    imshow("Blue_Extracted",blue_extracted);

    //等待按键关闭
    waitKey(0);
    return 0;
}