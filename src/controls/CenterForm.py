
import sys
, QApplication,QDesktopWidget
from PyQt5.QtGui import QIconfrom PyQt5.QtWidgets import QMainWindow

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm,self).__init__()

        # 设置主窗口的标题

        self.setWindowTitle('让窗口居中')

        # 设置窗口的尺寸

        self.resize(400,300)

        # 获得状态栏

        self.status = self.statusBar()

        self.status.showMessage('只存在5秒的信息',5000)

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget.screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newleft = (screen.width() - size.width()) / 2
        newTop = (screen.height() -  size.height()) / 2
        self.move(newleft,newTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./img/w3.ico'))
    main = CenterForm()
    main.show()
    sys.exit(app.exec_())