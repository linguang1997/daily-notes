'当.ui转化为.py时需要添加的代码如下:'
import sys
from PyQt5.QtWidgets import*
from PyQt5 import QtCore, QtGui, QtWidgets  #添加到程序的头部
class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()

    sys.exit(app.exec_())          #添加到程序的尾部

'或者新建一个文档调用：'
import sys
import mainUI    ###
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mainUI.Ui_MainWindow()    ###
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



' 产生随机数字'
import random
import time
while True:
    num = 1
    time.sleep(num)
    print(random.randint(0,20))   



pyqt环境配置
#在从源代码构建PyQt5之前，您必须已经构建并安装了SIP    #pip3 install SIP
# pip install pyqt5-tools(产生exe文件)     #pip intall PyQt5    #pip uninstall QtDesigner
"配置pyuic(将ui转化为py)"      #路径为解释器的路径        
 #   -m PyQt5.uic.pyuic  $FileName$ -o $FileNameWithoutExtension$.py       #   $FileDir$   
 "配置Qt Designer"        #路径为designer的路径     #  $ProjectFileDir$
 



linux系统cmd的一些快捷键
# cd 修改路径
#pwd 查看当前所在路径
# pip --version
# linux系统的路径前面会有 $
# ls dir 查看目标文件夹下的文档
# vi Setting.xml 不知道什么命令
#打开一个文档之前最好cd路径，也可以输入路径然后tab出文档
if(os.name == 'posix'):  #判断操作系统是否为Linux操作系统



formot()函数的使用： 
msg = '{} : {}'.format('self.checkbox_sensor.isChecked()',self.checkbox_sensor.isChecked())
#{}中的内容将会被formot()中的字符串所替代


XML   （extensive markup language）
#为扩展标记语言，作用是传输和存储数据，是独立于软件和硬件之间的信息传输工具
#xml标签没有预定义，需要自定义
ET.parse  #解析xml    讲解：https://developer.51cto.com/art/201602/505662.htm


HTML    （hypertype markup language）
#为超文本标记语言，作用是显示数据


os模块
os.path.dirname(__file__)  #得到当前文件的绝对路径
os.path.join  #路径拼接   讲解：https://www.jb51.net/article/171478.htm


QApplication.processEvents()    #页面刷新   讲解：https://www.cnblogs.com/liugp/p/10382624.html


import RPi.GPIO as GPIO #导入树莓派模块   #GPIO详解：https://www.jianshu.com/p/f31b90cc756f
GPIO.setwarnings(False)   #禁用警告


sys.argv #获取命令行参数，返回值是list，第一个元素是程序本身


eval()函数的使用：                     #https://blog.csdn.net/quanlingtu1272/article/details/95454722


import subprocess #创建子线程


import datetime 导入时间模块   #两种方式：http://www.360doc.com/content/18/0911/22/54508727_785802574.shtml


迭代（Interation）
#方法：for in        用于list tuple 或其他可迭代的对象
判断是否可迭代 from collections import  Iterable
>>> isinstance('abc', Iterable)
#可迭代和对象可迭代区别   


列表的方法    range(1,6)=[1, 2, 3, 4, 5]
for key in d   (d是一个字典)
for value in d.values()
for k, v in d.items()  

>>> a = [66.25, 333, 333, 1, 1234.5]
>>> print(a.count(333), a.count(66.25), a.count('x'))
2 1 0
>>> a.insert(2, -1)
>>> a.append(333)
>>> a
[66.25, 333, -1, 333, 1, 1234.5, 333]
>>> a.index(333)
1
>>> a.remove(333)
>>> a
[66.25, -1, 333, 1, 1234.5, 333]
>>> a.reverse()
>>> a
[333, 1234.5, 1, 333, -1, 66.25]
>>> a.sort()
>>> a
[-1, 1, 66.25, 333, 333, 1234.5]    


'pyqt关闭窗口button'    
from PyQt5.QtCore import QCoreApplication     #要使用quit首先要调用QCoreApplication
qtn = QPushButton('Quit', self)      #定义button,名称为quit
#创建一个按钮，qtn是QPushButton类的一个实例，QPushButton的第一个参数是按钮上的文字，第二个参数指明这个按钮的父部件，在这里是Exp。
qtn.clicked.connect(QCoreApplication.quit)   #退出函数（信号和槽）
