# 学习笔记
## 一，Linux
### 1.<img width="1179" alt="cc511ba70040cd341b3cb47a3191b03" src="https://github.com/user-attachments/assets/cea9d42a-7324-47b8-8fc1-4ab3dc19d415" />
### 2.非图形化界面能使用的文本编辑器（vim、nano等）的基本用法  

如果需要通过vi/vim编辑器编辑文件，通过如下命令:   

`vi 文件路径  vim 文件路径`

**vi/vim工作模式示意图**

<img width="255" alt="151afbfface16e07c1b2d2a499a8abf" src="https://github.com/user-attachments/assets/980d74d5-5647-44f5-9005-f73682ab7bbe" />

**快捷键**

| 模式 | 命令 | 描述 |
| ---- | ---- | --- |
| 命令模式 | `i` | 在当前光标位置进入输入模式 |
| 命令模式 | `a` | 在当前光标位置之后进入输入模式 |
| 命令模式 | `I` | 在当前行的开头进入输入模式 |
| 命令模式 | `A` | 在当前行的结尾进入输入模式 |
| 命令模式 | `o` | 在当前光标下一行进入输入模式 |
| 命令模式 | `O` | 在当前光标上一行进入输入模式 |
| 输入模式 | `esc` | 在任何情况下输入`esc`都能回到命令模式 |
| 底线命令模式 | `:wq` | 保存并退出 |
| 底线命令模式 | `:q` | 仅退出 |
| 底线命令模式 | `:q!` | 强制退出 |
| 底线命令模式 | `:w` | 仅保存 |
| 底线命令模式 | `:set nu` | 显示行号 |
| 底线命令模式 | `:set paste` | 设置粘贴模式 |

Nano使用方法

1.打开文件：

若要使用 nano 打开文件，只需在终端中输入以下命令，其中 filename 是要编辑的文件名：

`nano filename`

例如，要编辑名为 example.txt 的文件，可以运行：

`nano example.txt`

2.保存文件：

若要保存文件，可以按下 Ctrl 键和 O 键（同时按下），然后按 Enter 键。这将保存文件。

3.退出编辑器：

若要退出 nano，可以按下 Ctrl 键和 X 键（同时按下）。如果文件已更改但尚未保存，nano 会提示你是否要保存更改。按照提示选择是或否。

4.移动光标：

* 使用箭头键（上、下、左、右）来移动光标。
* 使用 Page Up 和 Page Down 键来滚动页面。
* 使用 Ctrl 键和 A 键将光标移到行首。
* 使用 Ctrl 键和 E 键将光标移到行尾。

5.剪切、复制和粘贴：

* 使用 Ctrl 键和 K 键剪切（删除）文本。
* 使用 Ctrl 键和 U 键复制文本。
* 使用 Ctrl 键和 Shift 键和 V 键粘贴文本。

6.查找和替换：

* 使用 Ctrl 键和 W 键进行查找。
* 使用 Ctrl 键和 \\ 键进行替换。

7.撤销和重做：

* 使用 Ctrl 键和 Shift 键和 Z 键撤销。
* 使用 Ctrl 键和 Shift 键和 R 键重做。

8.帮助：
若要查看 nano 的帮助信息，可以按下 Ctrl 键和 G 键（同时按下）。这会显示关于 nano 快捷键的帮助信息。

### 3.ssh

使用：
```
ssh 用户名@hostname
ssh -l [用户名] hostname
ssh hostname
```

<img width="1179" alt="44b5fe5cd63e29a41361ca71e9ab104" src="https://github.com/user-attachments/assets/94c800d3-a4cc-4cc5-8cb1-ee3c2bd81f4e" />

### 4.**Linux命令行基本操作**

ls命令的作用是列出目录下的内容，如下  `ls [-a -l -h] [Linux路径]`

* 直接使用ls命令本体，表示：以平埔形式。列出当前工作目录下的内容
* -a：列出全部文件（包含隐藏文件）
* -l：以竖向排练的方式展示内容，并展示更多信息
* -h：以易于阅读的形式，列出文件大小，如K,M,G（必须搭配-l一起使用）

cd切换工作目录，直接执行时表示回到HOME目录，如下  `cd [Linux路径]`

pwd查看当前工作目录，无选项，无参数，如下  `pwd`

_特殊路径符_

* .表示当前目录，比如cd./Desktop
* ..表示上一级目录，比如cd..或cd../..
* \~表示用户的HOME目录，比如cd\~或cd\~/Desktop

mkdir用于创建新的目录（文件夹），-p适用于创建连续多层级目录，如下  `mkdir [-p] Linux路径`

touch创建文件，如下  `touch [Linux路径]

_注意：mkdir创建的是文件夹，而touch创建的是文件本身！_

cat查看文件内容，如下  `cat [Linux路径]`

more同样可以查看文件内容，与cat不同的是

* cat是直接将内容全部显示出来
* more支持翻页（空格翻页，q退出查看）

语法：  `more [Linux路径]`  

**cp用于复制文件\\文件夹，如下**  `cp [-r] 参数1 参数2`

* -r可选，用于复制文件夹，表示递归
* 参数1，Linux路径，表示被复制的文件或文件夹
* 参数1，Linux路径，表示要复制去的地方

**mv用于移动文件\\或文件夹，如下**  `mv 参数1 参数2`

* 参数1，Linux路径，表示被移动的文件或文件夹
* 参数2，Linux路径，表示要移动去的地方，如果目标不存在，则进行改名，确保目标存在

**rm用于删除文件，文件夹，如下**  `rm [-r -f] 参数1 参数2 ...... 参数N`

* 同cp命令一样，-r用于删除文件夹
* -f强制删除
* 参数1，参数2，......，参数N表示要删除的文件或文件夹路径，按照空格隔开

rm命令支持通配符*，用于做模糊匹配

* test\*，表示匹配任何以test开头的内容
* \*test，表示匹配任何以test结尾的内容
* \*test\*，表示匹配任何包含test的内容

**find搜索指定文件，如下**  `find 起始路径 -name "被查找文件名"`

find命令也满足通配符，规则如上

**find命令可按文件大小查找文件，如下**  `find 起始路径 -size +|-n[kMG]`

* +，-表示大于和小于
* n表示大小数字
* kMG表示大小单位，k（小写字母）表示kb，M表示MB，G表示GB

**重定向符>和>>**

* \>，将左侧命令的结果，覆盖写入符号右侧指定的文件中
* \>>，将左侧命令的结果，追加写入符号右侧指定的文件中

演示：`echo "Hello Linux" >itheima.txt`

tail查看文件尾部内容，跟踪文件最新更改，如下  `tail [-f -num] Linux路径

* 参数，Linux路径，表示被跟踪的文件路径
* 选项，-f，表示持续跟踪
* 选项，-num，表示查看尾部多少行，不填默认10行
  
**grep从文件中通过关键字过滤文件行，如下**  `grep [-n] 关键字 文件路径`

* -n，可选，表示在结果中显示匹配的行的行号
* 关键字，必填，表示过滤的关键字，带有空格或其他符号，建议使用\"\"将关键词包围起来
* 文件路径，必填，表示要过滤的文件路径，可作为内容输入端口

### 5.挂载U盘复制文件

可参考以下网址

>https://blog.csdn.net/weixin_44419695/article/details/88127644

### 6.git命令行基本用法

1.提交步骤

* git init 初始化git仓库 (mac中Command+Shift+. 可以显示隐藏文件)
* git status 查看文件状态
* git add 文件列表 追踪文件
* git commit -m 提交信息 向仓库中提交代码
* git log 查看提交记录

2.撤销

* 用暂存区中的文件覆盖工作目录中的文件： git checkout 文件名
* 将文件从暂存区中删除： git rm --cached 文件名
* 将 git 仓库中指定的更新记录恢复出来，并且覆盖暂存区和工作目录：git reset --hard commitID

3.分支命令

* git branch 查看分支
* git branch 分支名称 创建分支
* git checkout 分支名称 切换分支
* git merge 来源分支 合并分支 (备注：必须在master分支上才能合并develop分支)
* git branch -d 分支名称 删除分支（分支被合并后才允许删除）（-D 强制删除）

4.暂时保存更改
* 在git中，可以暂时提取分支上所有的改动并存储，让开发人员得到一个干净的工作副本，临时转向其他工作。
* 使用场景：分支临时切换
* 存储临时改动：git stash
* 恢复改动：git stash pop
                       
>原文链接：https://blog.csdn.net/weixin_51170516/article/details/111187007

复制内容生成ssh密钥时，无法打开id_rsa.pub这个文件，解决方法如下：

在windows终端使用type命令查看文件内容

## 二，Opencv

### 1.基础命令

#### python:

1.

图像读取：  `cv2.IMREAD(img_path,flag)`

* img_path:图片路径，路径错误返回None
* flag:cv2.IMREAD_COLOR，读取彩色图片，图片透明性会被忽略，为默认参数，也可传入1
* flag:cv2.IMREAD_GRAYSCALE，灰度模式，也可传0
* flag:cv2.IMREAD_UNCHANGED，读取图像，包括其alpha通道，也可以传入-1

图像保存：  `cv2.imwrite(img_path,img)`

* img_path_name:文件名
* img:文件对象

图像缩放：  `cv2.resize(img,dsize,fx,fy,interpolation)`

* fx,fy表示水平方向和垂直方向的缩放比例
* interpolation表示插值方式

图像色彩空间转换：  `cv2.cvtColor(img,code)`

图像显示：  `cv2.imshow(winname,img)`

* winname:窗口名称
* img:显示的图像

2.

**数组之间不能直接赋值，可用`result = np.zeros_like(image)`**

3.

图像阈值分割threshold

`thresh,result=cv2.threshold (src, thresh, maxval, type)`

* thresh为设定阈值，取值范围为0-255，数据类型为浮点型（输入可以为整型）
* result为进行阈值分割后的结果图像，数据类型为整数矩阵
* src为被进行分割的源图像
* maxval为最大值，为分割后的图像所取到的灰度最大值
* type为阈值分割的类型

cv2.THRESH_BINARY_INV: 这是阈值类型，表示使用反向二值化。

_处理较大图片时，用普通方法计算均值会导致运算量过大，图片无法正常显示，应选用np.mean()函数_

_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)使用 Otsu's 方法自动选择阈值

3.

浅拷贝  

```
import copy

c = copy.copy(a)
```

深拷贝

```
import copy

d = copy.deepcopy(a)
```

**深拷贝和浅拷贝的区别**

（1）由于 Python 内部引用计数的特性，对于不可变对象，浅拷贝和深拷贝的作用是一致的，就相当于复制了一份副本，原对象内部的不可变对象的改变，不会影响到复制对象
（2）浅拷贝的拷贝。其实是拷贝了原始元素的引用（内存地址），所以当拷贝可变对象时，原对象内可变对象的对应元素的改变，会在复制对象的对应元素上，有所体现
（3）深拷贝在遇到可变对象时，又在内部做了新建了一个副本。所以，不管它内部的元素如何变化，都不会影响到原来副本的可变对象

9.

`opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)`  开运算

`closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)`  闭运算

_开运算去白噪点，闭运算去黑噪点_

10.

python中def用来建立函数

高斯函数核由高斯公式生成

image.shape返回图像的高度（行数）和宽度（列数）

11.

* num_labels：所有连通域的数目
* labels：图像上每一像素的标记，用数字1、2、3…表示（不同的数字表示不同的连通域）
* stats：每一个标记的统计信息，是一个5列的矩阵，每一行对应每个连通区域的外接矩形的x、y、width、height和面积，示例如下： 0 0 720 720 291805
* centroids：连通域的中心点

`num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(arr_gray, connectivity=8)`

12.

cv2.findContours()查找图像中轮廓

`contours, hierarchy = cv2.findContours(image, mode, method)`

参数：

* mode:轮廓检索模式。常用的选项包括：cv2.RETR_EXTERNAL: 只提取外部轮廓。cv2.RETR_LIST: 提取所有轮廓，但不建立层次关系。cv2.RETR_TREE: 提取所有轮廓，并建立层次关系。
* method:轮廓近似方法。常用的选项包括：cv2.CHAIN_APPROX_SIMPLE: 只保留轮廓的端点，减少存储所需的点的数量。cv2.CHAIN_APPROX_NONE: 保留所有轮廓点。

返回值：

* contours: 轮廓的列表，每个轮廓是一个点的数组，表示轮廓的边界
* hierarchy: 可选的层次结构信息，描述轮廓之间的关系（例如，父轮廓和子轮廓）

cv2.drawContours()绘制轮廓

`cv2.drawContours(image, contours, contourIdx, color, thickness, lineType=cv2.LINE_8, hierarchy=None, maxLevel=0, offset=(0, 0))`

参数：

* contours:包含轮廓的列表。通常是通过 cv2.findContours() 函数获得的。
* contourIdx:要绘制的轮廓的索引。可以是以下值：-1: 绘制所有轮廓。具体的索引值: 只绘制指定索引的轮廓。
* hierarchy (可选):轮廓的层次结构信息，通常在不需要时可以忽略。
* maxLevel (可选):指定绘制的轮廓层次的最大级别。默认为 0，表示绘制所有层次。
* offset (可选):从图像的左上角开始绘制轮廓的偏移量，默认为 (0, 0)

**python中常见函数**

1.np.where 函数接受一个布尔数组作为输入，并返回满足条件的元素的索引。对于二维数组，它会返回两个数组：第一个数组包含满足条件的元素的行索引，第二个数组包含列索引。

2.np.stack 函数用于将多个数组沿着新的轴进行堆叠。

3..T 是 NumPy 数组的转置操作。通过转置，行和列的位置会互换。

4.for x, y in anchor 的含义：

这个循环会遍历 anchor 中的每一行（或每个二元组），并将每一行的两个元素分别赋值给变量 x 和 y。这意味着在每次循环中，x 将接收当前行的第一个元素，y 将接收当前行的第二个元素。

5.np.tan() 函数计算输入弧度的正切值。

6.abs() 函数用于取绝对值。

7.if后应用elif

8.def创建函数

9.np.degrees(theta)，将弧度转换为度。

10.cv2.convertScaleAbs(sobel_x) 是 OpenCV 中的一个函数，它用于将图像的像素值转换为无符号 8 位整型（uint8）格式，并且在这个过程中进行缩放和绝对值处理。这个函数的主要用途是在图像处理过程中处理梯度图像时，确保结果在适当的范围内，以便可以正确显示。

11.append 是 Python 列表对象的一个方法，用于在列表的末尾添加新的元素。

12.numpy中的取整函数（数据类型不变）

* `np.floor()`  向下取整
* `np.ceil()`  向上取整
* `np.round()`  四舍五入
* `np.trunc()`  返回小于或等于给定数字的最大整数（与 int() 类似）

#### c++:

1.

在写简单的opencv程序时，可用以下头文件

```
#include <opencv2/core/core.hpp>

#include <opencv2/highgui/highgui.hpp>

using namespace cv;
```

**图像的载入：imread()函数**

`Mat imread(const string& filename,intflags=1);`

* 前者为地址，后者为模式

**图像的显示：imshow()函数**

`void imshow((const string& winname, InputArray mat);`

* 前者为窗口名，后者为传入的图像

2.

OpenCV操作像素的几种方法(单个像素|操作多像素|遍历像素)

at()访问像素

* 改变像素：template T& Mat::at(int i, int j)
* 读取像素：template const T& Mat::at(int i, int j) const
* **在灰度图中，Opencv里可用uchar代替unsigned char,在彩色图中，Opencv里可用Ver3b代替将三个uchar组成的容器(vector)，且可在后面加上[]。注明是要操作此元素的哪个通道**

下面操作一个8位元灰度图，分别改变某个像素的值，以及查看此像素的值：

```
Mat gray_img(100, 100, CV_8U, Scalar(100));

gray_img.at<uchar>(30,20) =255;            

uchar value1 = gray_img.at<uchar>(30,20); 
```

下面分别改变彩色图某个像素的第一通道值，以此查看此元素第一通道的值：

```
Mat color_img(100, 100, CV_8UC3, Scalar(200,100,0));

img.at<Vec3b>(30,20)[0] =255;        

uchar value2 = img.at<Vec3b>(30,20)[0]; 
```
ptr函数输入指定列，返回指向此列的第一个元素

* 改变像素：template T* Mat::ptr(int i=0)
* 读取像素：template const T* Mat::ptr(int i=0) const

**注意：数组之间不能直接赋值，可用`Mat img0=img.clone();`,OpenCV 使用 BGR 顺序!!输出时要反过来输出**

5.

多通道分离函数split()
```
void cv::split(const Mat & src,
                 Mat * mvbegin
                 )
void cv::split(InputArray m,
                 OutputArrayOfArrays mv
                 )

```

* src：待分离的多通道图像。
* mvbegin：分离后的单通道图像，为数组形式，数组大小需要与图像的通道数相同
* m：待分离的多通道图像
* mv：分离后的单通道图像，为向量vector形式

该函数主要是用于将多通道的图像分离成若干单通道的图像，两个函数原型中不同之处在于前者第二个参数输入的是Mat类型的数组，其数组的长度需要与多通道图像的通道数相等并且提前定义；第二种函数原型的第二个参数输入的是一个vector容器，不需要知道多通道图像的通道数。两个函数原型虽然输入参数的类型不同，但是通道分离的原理是相同的

6.

**通过调校亮度的分布就是进行伽马校正意味着那些效果会得到补偿修复。gamma校正的意义就在于将人眼感受到的灰度值, 转换到自然界真正的灰度值(因为人不是测量器, 人只能感受和比较)**

gamma校正原理

假设图像中有一个像素，值是 200 ，那么对这个像素进行校正必须执行如下步骤： 
　　1. 归一化 ：将像素值转换为  0 ～ 1  之间的实数。 算法如下 : ( i + 0. 5)/256  这里包含 1 个除法和 1 个加法操作。对于像素  A  而言  , 其对应的归一化值为  0. 783203 。 

　　2. 预补偿 ：根据公式  , 求出像素归一化后的 数据以  1 /gamma  为指数的对应值。这一步包含一个 求指数运算。若  gamma  值为  2. 2 ,  则  1 /gamma  为  0. 454545 , 对归一化后的  A  值进行预补偿的结果就 是  0. 783203 ^0. 454545 = 0. 894872 。 

　　3. 反归一化 ：将经过预补偿的实数值反变换为  0  ～  255  之间的整数值。具体算法为 : f*256 - 0. 5  此步骤包含一个乘法和一个减法运算。续前 例  , 将  A  的预补偿结果  0. 894872  代入上式  , 得到  A  预补偿后对应的像素值为  228 , 这个  228  就是最后送 入显示器的数据。

9.

getStructuringElement 函数用于生成形态学操作所需的结构元素

`cv::Mat cv::getStructuringElement(int shape, const cv::Size& ksize, cv::Point anchor = cv::Point(-1, -1));`

* shape: 结构元素的形状，可以是以下之一：
cv::MORPH_RECT: 矩形结构元素
cv::MORPH_ELLIPSE: 椭圆形结构元素
cv::MORPH_CROSS: 十字形结构元素
* ksize: 结构元素的大小，使用 cv::Size(width, height) 指定宽度和高度。
* anchor: 结构元素的锚点，默认为 (-1, -1)，表示结构元素的中心点。

10.

**Canny的实现步骤**

（1）应用高斯滤波来平滑图像，目的是去除噪声

（2）找寻图像的强度梯度（可用Sobel算子）

（3）应用非最大抑制技术来消除边缘误检

（4）应用双阈值的方法来决定可能的边界

**opencv-c++中的常见函数**

1.cv::Point 是 OpenCV 中的一个类，用于表示二维点的坐标。它通常用于图像处理中的坐标表示，例如绘制图形或标记特定位置。
