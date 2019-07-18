import sys
import MainWinFormLayout

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='__main__':
    # 创建QApplication的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    mainWindow = QMainWindow()
    # 创建一个MainWinHorizontalLayout对象
    ui = MainWinFormLayout.Ui_MainWindow()
    # 向主窗口添加控件
    ui.setupUi(mainWindow)
    # 窗口显示
    mainWindow.show()
    # 安全退出
    sys.exit(app.exec_())
