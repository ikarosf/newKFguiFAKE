# -*- coding: utf-8 -*-

import sys
import os

# import PySide2
# dirname = os.path.dirname(PySide2.__file__)
# plugin_path = os.path.join(dirname, 'plugins', 'platforms')
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
# print(plugin_path)

# if hasattr(sys,'frozen'):
#     os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication
from topWindowClass import *
import global_env
# import logging
import resource_rc

# 打包exe文件用，编程时请注释
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join('.', 'plugins')

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

    dailyBattleWindow = dailyBattleWindow()
    global_env.dailyBattleWindow = dailyBattleWindow
    # dailyBattleWindow.setWindowModality(Qt.ApplicationModal)

    mainWin.setupUi(mainWin)

    mainWin.show()
    sys.exit(app.exec_())
