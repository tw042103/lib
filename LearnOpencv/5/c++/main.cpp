#include <iostream>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\opencv.hpp>
using namespace std;
using namespace cv;

int main()
{
    //读取图像
    Mat img=imread("C:/github/lib/LearnOpencv/1/c++/cqss.png");
    //调整图像大小便于显示
    Size newsize(320,320);
    resize(img,img,newsize);
    //建立新数组用来存放分离后的通道
    vector<Mat> c;
    //通道分离
    split(img,c);
    //显示图像
    imshow("B",c[0]);
    imshow("G",c[1]);
    imshow("R",c[2]);
    imshow("img",img);
    //等待按键关闭
    waitKey(0);
    return 0;
}