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

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.clicked.connect(self.enterTestMode)
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
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        self.pushButton_6.setText("PushButton")
        self.pushButton_7.setText("PushButton")
        self.pushButton_8.setText("TESTMODE")
        self.pushButton_9.setText("ABOUT")

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
        QMessageBox.about(self, "关于", """autor: ikarosf @kf \ntitle: 咕咕镇计算器图形化界面(伪（伪）)\nvision: 0.6\nlink: 
        https://bbs.ikfol.com/read.php?tid=809582&sf=44f""")

    def enterTestMode(self):
        yes = QMessageBox.warning(self, "进入测试模式？", "测试模式暂时唯一的功能是保存卡片时不再检测数值合法性", QMessageBox.Yes | QMessageBox.No)
        if yes:
            global_env.test_mode = True