# -*- coding: utf-8 -*-

import sys, os

# import PySide2
# dirname = os.path.dirname(PySide2.__file__)
# plugin_path = os.path.join(dirname, 'plugins', 'platforms')
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
# print(plugin_path)

# if hasattr(sys,'frozen'):
#     os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QFrame
from PySide2 import QtGui

from battleready import Ui_battleReadyForm
from mainWindow import Ui_MainWindow
from mycardWindow import Ui_mycardForm
from enemycardWindow import Ui_enemycardForm
from npcWindow import Ui_npcForm
import global_env
# import logging


import resource_rc


# 打包exe文件用，编程时请注释
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join('.', 'plugins')


class MyWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        # self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/bitbug_favicon.ico'))

    # def wheelEvent(self, event):
    #     super()
    #
    #     angle=event.angleDelta() / 108                                           # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
    #     angleX=angle.x()  # 水平滚过的距离(此处用不上)
    #     angleY=angle.y()  # 竖直滚过的距离
    #     if angleY > 0:
    #         action_def.previous_page()
    #         print("鼠标滚轮上滚")  # 响应测试语句
    #     else:                                                                  # 滚轮下滚
    #         action_def.next_page()
    #         print("鼠标滚轮下滚")  # 响应测试语句

    def closeEvent(self, event):
        # if not global_env.data_saved:
        #     reply = QtWidgets.QMessageBox.question(self,
        #                                            '将关闭程序',
        #                                            "是否保存？",
        #                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel,
        #                                            QtWidgets.QMessageBox.Cancel)
        #     if reply == QtWidgets.QMessageBox.Yes:
        #         global_env.keep_data_store()
        #         event.accept()
        #     elif reply == QtWidgets.QMessageBox.No:
        #         event.accept()
        #     else:
        #         event.ignore()
        # else:
        #     event.accept()
        global_env.storeSaveData()


class myCardWindow(Ui_mycardForm, QFrame):
    def __init__(self, parent=None):
        super(myCardWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)


class enemyCardWindow(Ui_enemycardForm, QFrame):
    def __init__(self, parent=None):
        super(enemyCardWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)


class npcWindow(Ui_npcForm, QFrame):
    def __init__(self, parent=None):
        super(npcWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)


class battleReadyWindow(Ui_battleReadyForm, QFrame):
    def __init__(self, parent=None):
        super(battleReadyWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)


if __name__ == '__main__':
    # logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
    #                     datefmt="%Y/%d/%m %H:%M:%S",
    #                     level=logging.DEBUG,filename="debug.txt",filemode="w")
    app = QApplication(sys.argv)

    if not global_env.readSaveData():
        global_env.initSaveData()

    mainWin = MyWindow()
    global_env.mainWin = mainWin

    myCardWindow = myCardWindow()
    enemyCardWindow = enemyCardWindow()
    npcWindow = npcWindow()
    battleReadyWindow = battleReadyWindow()
    global_env.myCardWindow = myCardWindow
    global_env.enemyCardWindow = enemyCardWindow
    global_env.npcWindow = npcWindow
    global_env.battleReadyWindow = battleReadyWindow

    mainWin.setupUi(mainWin)

    mainWin.show()
    sys.exit(app.exec_())
