# 学习笔记
## 一，Linux
### 1.<img width="1179" alt="cc511ba70040cd341b3cb47a3191b03" src="https://github.com/user-attachments/assets/cea9d42a-7324-47b8-8fc1-4ab3dc19d415" />
### 2.非图形化界面能使用的文本编辑器（vim、nano等）的基本用法  

如果需要通过vi/vim编辑器编辑文件，通过如下命令:   

`vi 文件路径  vim 文件路径`

**vi/vim工作模式示意图**

<img width="255" alt="151afbfface16e07c1b2d2a499a8abf" src="https://github.com/user-attachments/assets/980d74d5-5647-44f5-9005-f73682ab7bbe" />

**命令模式快捷键**

| 模式 | 命令 | 描述 |
| ---- | ---- | --- |
| 命令模式 | `i` | 在当前光标位置进入输入模式 |
| 命令模式 | `a` | 在当前光标位置之后进入输入模式 |
| 命令模式 | `I` | 在当前行的开头进入输入模式 |
| 命令模式 | `A` | 在当前行的结尾进入输入模式 |
| 命令模式 | `o` | 在当前光标下一行进入输入模式 |
| 命令模式 | `O` | 在当前光标上一行进入输入模式 |
| 输入模式 | `esc` | 在任何情况下输入`esc`都能回到命令模式 |

### 3.2

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
