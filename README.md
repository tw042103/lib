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

_处理较大图片时，用普通方法计算均值会导致运算量过大，图片无法正常显示，应选用np.mean()函数_

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

使用c++调用opencv时显示图片界面无法成功加载，几秒后闪退，问题出在图像后缀名错误，需注意

![a083260ccb55ad5be313a342277998e](https://github.com/user-attachments/assets/28211c53-2ac1-4daa-876a-a5574dc21940)

