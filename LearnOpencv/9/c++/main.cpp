#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;

int main()
{
    //读取图像
    Mat img=imread("C:/github/lib/picture/9.png",IMREAD_GRAYSCALE);

    //生成结构元素图像
    Mat kernel=getStructuringElement(2,Size(8,8));

    //开运算
    Mat result1;
    morphologyEx(img,result1,MORPH_OPEN,kernel);

    //闭运算
    Mat result2;
    morphologyEx(img,result2,MORPH_CLOSE,kernel);

    //显示图像
    imshow("Img",img);
    imshow("Open",result1);
    imshow("Close",result2);

    //等待按键关闭
    waitKey(0);
    return 0;
}