# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtWidgets import *

import action_def
import global_env

QString = type("")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        self.myCardButton = QPushButton(self.centralwidget)
        self.myCardButton.setObjectName(u"myCardButton")
        self.myCardButton.clicked.connect(global_env.myCardWindow.open)
        self.gridLayout.addWidget(self.myCardButton, 0, 0, 1, 1)

        self.enemyCardButton = QPushButton(self.centralwidget)
        self.enemyCardButton.setObjectName(u"enemyCardButton")
        self.enemyCardButton.clicked.connect(global_env.enemyCardWindow.open)
        self.gridLayout.addWidget(self.enemyCardButton, 0, 1, 1, 1)

        self.npcSetButton = QPushButton(self.centralwidget)
        self.npcSetButton.setObjectName(u"npcSetButton_3")
        self.npcSetButton.clicked.connect(global_env.npcWindow.open)
        self.gridLayout.addWidget(self.npcSetButton, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.clicked.connect(global_env.battleReadyWindow.open)
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.clicked.connect(self.chooseEXE)
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.clicked.connect(self.helpWindowOpen)
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.clicked.connect(global_env.dailyBattleWindow.open)
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        # self.pushButton_8 = QPushButton(self.centralwidget)
        # self.pushButton_8.setObjectName(u"pushButton_8")
        # self.pushButton_8.clicked.connect(self.enterTestMode)
        # self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"PVP")
        self.pushButton_8.clicked.connect(global_env.pvpWindow.open)
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.clicked.connect(self.aboutWindowOpen)
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)

        self.set_menu = self.menubar.addMenu("设置")

        self.set_threads_action = self.set_menu.addAction('设置线程数')
        self.set_threads_action.triggered.connect(self.set_threads)

        self.set_tests_action = self.set_menu.addAction('设置回数')
        self.set_tests_action.triggered.connect(self.set_tests)

        self.set_verbose_action = self.set_menu.addAction('设置显示进度')
        self.set_verbose_action.triggered.connect(self.set_verbose)

        self.set_reducerate_action = self.set_menu.addAction('设置抵消率')
        self.set_reducerate_action.triggered.connect(self.set_reducerate)

        self.set_seedmax_action = self.set_menu.addAction('设置种子数')
        self.set_seedmax_action.triggered.connect(self.set_seedmax)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.mpShadeWindow = QWidget(MainWindow)
        self.mpShadeWindow.setStyleSheet("QWidget{background-color:rgba(0,0,0,0.3);}")
        self.mpShadeWindow.hide()

        self.mpgridLayout = QHBoxLayout(self.mpShadeWindow)
        self.mpButton = QPushButton(self.mpShadeWindow)
        self.mpButton.clicked.connect(self.mpBreak)
        self.mpgridLayout.addWidget(self.mpButton, 0.1, Qt.AlignCenter)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle('咕咕镇计算器图形化界面(伪（伪）)')
        self.myCardButton.setText("我的卡片")
        self.enemyCardButton.setText("敌方卡片")
        self.npcSetButton.setText("NPC")
        self.pushButton_4.setText("模拟战斗")
        self.pushButton_5.setText("设置newkf.exe路径")
        self.pushButton_6.setText("HELP")
        self.pushButton_7.setText("日常战斗")
        self.pushButton_8.setText("PVP战斗")
        self.pushButton_9.setText("ABOUT")
        self.mpButton.setText("中止计算")

    # retranslateUi

    def chooseEXE(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取newkf.exe",
                                                                ".",  # 起始路径
                                                                "EXE Files (*.exe)")  # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            return
        QMessageBox.information(self, "提示", "已选择" + fileName_choose + "为咕咕镇计算器", QMessageBox.Yes)
        global_env.saveData["setting"]["exeDir"] = fileName_choose

    def aboutWindowOpen(self):
        QMessageBox.about(self, "关于", """autor: ikarosf @kf 
        title: 咕咕镇计算器图形化界面(伪（伪）)
        vision: 2.00
        link: 
        https://bbs.kforz.com/read.php?tid=809582&sf=44f""")

    def helpWindowOpen(self):
        QMessageBox.information(self, "帮助", """
然而并没有什么可以帮你的
出现问题请确认计算器和界面都是最新版且下载完整
最好分别放在各自的文件夹内然后再设置newkf.exe路径
                """)

    def enterTestMode(self):
        yes = QMessageBox.warning(self, "进入测试模式？", "测试模式暂时唯一的功能是保存卡片时不再检测数值合法性", QMessageBox.Yes | QMessageBox.No)
        if yes == QMessageBox.Yes:
            global_env.test_mode = True

    def set_threads(self):
        text, ok = QInputDialog.getInt(self, '设置线程数', '', value=global_env.threads)
        if not (ok and text):
            return
        global_env.threads = text

    def set_tests(self):
        text, ok = QInputDialog.getInt(self, '测试重复数', '', value=global_env.tests)
        if not (ok and text):
            return
        global_env.tests = text

    def set_verbose(self):
        yes = QMessageBox.question(self, "请选择", "是否显示计算进度", QMessageBox.Yes | QMessageBox.No)
        if yes == QMessageBox.Yes:
            global_env.verbose = 1
        elif yes == QMessageBox.No:
            global_env.verbose = 0

    def set_reducerate(self):
        text, ok = QInputDialog.getText(self, '设置技能、暴击的抵消率', '如：“1 3”，填“0”为计算器默认设置', value=global_env.reducerate)
        if not (ok and text):
            return
        global_env.reducerate = text

    def set_seedmax(self):
        text, ok = QInputDialog.getInt(self, '设置初始候选方案最大数量', '默认值1000000(已百万)，最大值100000000（一亿）', value=global_env.seedmax)
        if not (ok and text):
            return
        global_env.seedmax = text

    def disable_all_button(self):
        self.mpShadeWindowShow()

    def enable_all_button(self):
        self.mpShadeWindowHide()

    def mpShadeWindowShow(self):
        self.mpShadeWindow.setGeometry(0, 0, self.width(), self.height())
        self.mpShadeWindow.show()

    def mpShadeWindowHide(self):
        self.mpShadeWindow.hide()

    def mpBreak(self):
        action_def.stopNewFKEXE()
        self.textBrowser.insertPlainText("计算中止！")

