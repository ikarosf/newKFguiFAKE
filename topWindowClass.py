from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QFrame, QDialog
# from PySide2.QtCore import Qt
from PySide2 import QtGui

from battlereadyWindow import Ui_battleReadyForm
from dailyBattleWindow import Ui_dailybattlewindow
from mainWindow import Ui_MainWindow
from mycardWindow import Ui_mycardForm
from enemycardWindow import Ui_enemycardForm
from npcWindow import Ui_npcForm

import global_env


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
        global_env.storeSaveData()
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

    def resizeEvent(self, event):
        if not self.mpShadeWindow.isHidden():
            self.mpShadeWindow.setGeometry(0, 0, self.width(), self.height())
        event.accept()


class myCardWindow(Ui_mycardForm, QFrame):
    def __init__(self, parent=None):
        super(myCardWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/bitbug_favicon.ico'))


class enemyCardWindow(Ui_enemycardForm, QFrame):
    def __init__(self, parent=None):
        super(enemyCardWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/bitbug_favicon.ico'))


class npcWindow(Ui_npcForm, QFrame):
    def __init__(self, parent=None):
        super(npcWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/bitbug_favicon.ico'))


class battleReadyWindow(Ui_battleReadyForm, QFrame):
    def __init__(self, parent=None):
        super(battleReadyWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/bitbug_favicon.ico'))


class dailyBattleWindow(Ui_dailybattlewindow, QMainWindow):
    def __init__(self, parent=None):
        super(dailyBattleWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.myCardForm = myCardWindow(self)
        self.npcFormList = [npcWindow(self) for i in range(10)]

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/bitbug_favicon.ico'))
