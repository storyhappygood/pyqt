#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('w3.ico'))
        # 上面的三个方法都继承自QWidget类。setGeometry()有两个作用：
        # 把窗口放到屏幕上并且设置窗口大小。参数分别代表屏幕坐标的x、y和
        # 窗口大小的宽、高。也就是说这个方法是resize()和move()的合体。
        # 最后一个方法是添加了图标。先创建一个QIcon对象，然后接受一个路径
        # 作为参数显示图标。
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())