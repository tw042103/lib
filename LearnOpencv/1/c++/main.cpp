#include <iostream>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\opencv.hpp>
using namespace std;
using namespace cv;


int main() {
    // 读取图像
    cv::Mat image = cv::imread("cqss.png"); 
    if (image.empty()) {
        std::cerr << "Error: Could not open or find the image!" << std::endl;
        return -1;
    }

    // 创建一个全屏窗口
    cv::namedWindow("FullScreen Image", cv::WINDOW_NORMAL);
    cv::setWindowProperty("FullScreen Image", cv::WND_PROP_FULLSCREEN, cv::WINDOW_FULLSCREEN);

    // 显示图像
    cv::imshow("FullScreen Image", image);

    // 等待按键
    cv::waitKey(0);

    // 关闭窗口
    cv::destroyAllWindows();
    return 0;
}
