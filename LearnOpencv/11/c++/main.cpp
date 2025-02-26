#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;

int main()
{
    // 读取图像
    Mat img=imread("C:/github/lib/picture/11.png",IMREAD_GRAYSCALE);

    // 通过图像阈值分割将原图转化位二值图像
    int thresh=85;
    Mat binary_img;
    threshold(img,binary_img,thresh,255,THRESH_BINARY);

    // 通过闭运算去除黑噪点
    Mat closing;
    Mat kernel=getStructuringElement(MORPH_RECT,Size(3,3));
    morphologyEx(binary_img,closing,MORPH_CLOSE,kernel);

    // 调用函数
    Mat labels,stats,centroids;
    int retval=connectedComponentsWithStats(closing,labels,stats,centroids);

    // 输出硬币数量
    cout<<retval-1;

    // 绘制硬币重心
    for(int i=1;i<retval;i++)
    {
        Point centroid(centroids.at<double>(i,0),centroids.at<double>(i,1));
        circle(closing,centroid,3,Scalar(0,0,255),-1);
    }

    // 显示图像
    imshow("Original Img",img);
    imshow("Result",closing);

    // 等待按键关闭
    waitKey(0);
    return 0;
}