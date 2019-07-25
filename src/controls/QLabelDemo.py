import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,QToolTip,QWidget,QPushButton,QVBoxLayout,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap,QPalette
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color=yellow>这是一个文本标签</font>')
        label1.setAutoFillBackground(True)
        patette = QPalette()
        patette.setColor(QPalette.Window,Qt.blue)#设置背景颜色

        label1.setPalette(patette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        label3.setAlignment(Qt.AlignHCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./img/cat.ico")

        # 如果设为True，用浏览器打开网页，如果设为False,调用槽函数
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注这本书</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')
    def linkHovered(self):
        print('当鼠标划过label2标签时，触发事件')

    def linkClicked(self):
        print('当鼠标划过label4标签时，触发事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())