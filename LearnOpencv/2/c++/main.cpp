#include <iostream>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\opencv.hpp>
using namespace std;
using namespace cv;

int main()
{
    //读取图像
    Mat img=imread("C:/github/lib/LearnOpencv/1/c++/cqss.png");
    //存放原图像
    Mat img0=img.clone();
    //遍历图像的每一个像素
    for(int h=0;h<img.rows;h++)
    {
        for(int w=0;w<img.cols;w++)
        {
            //计算均值并赋值
            int average=(img.at<Vec3b>(h,w)[0]+img.at<Vec3b>(h,w)[1]+img.at<Vec3b>(h,w)[2])/3;
            img.at<Vec3b>(h,w)=Vec3b(average,average,average);
        }
    }
    //显示图像
    imshow("img0",img0);
    imshow("img",img);
    //等待按键关闭
    waitKey(0);
    return 0;
}