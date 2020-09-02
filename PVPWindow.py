import os
import re

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import QCursor
from PySide2.QtWidgets import *

import action_def
import global_env
from ansyrun import execCmdWorkerAnsy
from equipChooseWindow import GearSetWindow
from mutliChooseDialog import mutliChooseWindow


class Ui_pvpwindow(object):
    def __init__(self, *args, **kwargs):
        super(Ui_pvpwindow, self).__init__(*args, **kwargs)
        self.myCardForm = None
        self.enemyCardForm = None
        self.GearList = []

    def setupUi(self, pvpwindow):
        if pvpwindow.objectName():
            pvpwindow.setObjectName(u"pvpwindow")
        pvpwindow.resize(1100, 600)
        self.centralwidget = QWidget(pvpwindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.myCardForm.setMaximumWidth(575)
        self.gridLayout.addWidget(self.myCardForm)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.addWidget(self.enemyCardForm)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.gridLayout_3 = QVBoxLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 2)

        pvpwindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(pvpwindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        pvpwindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(pvpwindow)
        self.statusbar.setObjectName(u"statusbar")
        pvpwindow.setStatusBar(self.statusbar)

        self.CardFormSet()
        # self.npcFormSet()
        self.buttonFormSet()
        self.retranslateUi(pvpwindow)
        QMetaObject.connectSlotsByName(pvpwindow)

    # setupUi

    def retranslateUi(self, pvpwindow):
        pvpwindow.setWindowTitle("日常战斗")

    # retranslateUi

    def buttonFormSet(self):
        self.grid_HBoxLayout = QHBoxLayout()
        self.gridLayout_3.addLayout(self.grid_HBoxLayout)

        # self.npcImportButton = QPushButton(self)
        # self.npcImportButton.clicked.connect(self.npcImport)
        # self.npcImportButton.setText(u"导入NPC")
        # self.grid_HBoxLayout.addWidget(self.npcImportButton, 3)

        # self.allDifficultyButton = QPushButton(self)
        # self.allDifficultyButton.clicked.connect(self.allDifficultyChoose)
        # self.allDifficultyButton.setText(u"选择全部难度")
        # self.gridLayout_2_1.addWidget(self.allDifficultyButton)
        # self.label = QLabel("难度:")
        # self.label.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        # self.combobox = npcHighGainComboBox(self)
        # self.combobox.addItem("全部强度")
        # self.combobox.currentIndexChanged.connect(lambda: self.allDifficultyChoose(self.combobox.currentIndex()))
        # self.grid_HBoxLayout.addWidget(self.label, 1)
        # self.grid_HBoxLayout.addWidget(self.combobox, 2)

        self.showGearButton = QPushButton(self)
        self.showGearButton.setObjectName(u"查看Gear")
        self.showGearButton.setText(u"查看备选装备")
        self.showGearButton.clicked.connect(lambda: self.showGear())
        self.grid_HBoxLayout.addWidget(self.showGearButton, 1)

        self.openGearWindowButton = QPushButton(self)
        self.openGearWindowButton.setObjectName(u"设置Gear")
        self.openGearWindowButton.setText(u"设置备选装备")
        self.openGearWindowButton.clicked.connect(lambda: self.openGearWindow())
        self.grid_HBoxLayout.addWidget(self.openGearWindowButton, 1)

        self.freebattlepushButton = QPushButton(self)
        self.freebattlepushButton.clicked.connect(self.freeBattleStart)
        self.freebattlepushButton.setText(u"自定义命令战斗")
        self.grid_HBoxLayout.addWidget(self.freebattlepushButton, 3)

        self.battleStartButton = QPushButton(self)
        self.battleStartButton.clicked.connect(lambda: self.runTestWindow())
        self.battleStartButton.setText(u"开始测试")
        self.grid_HBoxLayout.addWidget(self.battleStartButton, 3)

        # self.QLabel = QLabel(self)
        # self.openGearWindowButton.setObjectName(u"battlepushButton")
        # self.openGearWindowButton.clicked.connect(lambda: self.openGearWindow())
        # self.grid_HBoxLayout2.addWidget(self.QLabel, 2)

        self.rightMenuCreat()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)

    def allAbleCheck(self):
        (result, message) = self.myCardForm.ableCheck()
        if not result:
            QMessageBox.critical(self, "我方卡片设置错误", message, QMessageBox.Yes)
            return False
        (result, message) = self.enemyCardForm.ableCheck()
        if not result:
            QMessageBox.critical(self, "敌方卡片错误", message, QMessageBox.Yes)
            return False
        return True

    def freeBattleStart(self):
        if not self.allAbleCheck():
            return
        cmd_text, ok = QInputDialog.getMultiLineText(self, '自定义参数战斗', '输入参数：', text=global_env.run_args)
        if not (ok and cmd_text):
            return
        global_env.run_args = cmd_text
        self.battleStart(cmd_text)

    def runTestWindow(self):
        mcw, text, setting = mutliChooseWindow.pcLaunch(self)
        if mcw:
            self.battleStart(text, setting)

    def battleStart(self, cmd_text, setting=None):
        if not self.allAbleCheck():
            return

        text = self.make_full_gu_text(setting)
        file_path = os.path.join(".", "newkf.in")
        with open(file_path, "w") as f:
            f.write(text)

        mythread = execCmdWorkerAnsy(parent=self, item=cmd_text)
        mythread.start()
        self.close()

    def make_full_gu_text(self, setting):
        newCard = self.myCardForm.makeMyCard()
        enemyCard = self.enemyCardForm.makeMyCard()
        enemyCardList = [enemyCard]
        npcList = []
        gearList = self.GearList

        text = action_def.make_full_gu_text(newCard, npcList, enemyCardList, gearList=gearList, setting=setting)
        return text

    def allDifficultyChoose(self, index):
        for i in range(10):
            self.npcFormList[i].comboBox_4.setCurrentIndex(index)

    def CardFormSet(self):
        # self.myCardForm.pushButton.hide()
        # self.myCardForm.pushButton_2.hide()
        # self.myCardForm.pushButton_3.hide()
        self.myCardForm.weaponToStorage.hide()
        self.myCardForm.gloveToStorage.hide()
        self.myCardForm.ArmorToStorage.hide()
        self.myCardForm.helmetToStorage.hide()
        self.cardListUpdateButton = QPushButton(self)
        self.myCardForm.myCardListUpdate()
        self.cardListUpdateButton.clicked.connect(self.myCardForm.myCardListUpdate)
        self.myCardForm.gridLayout_8.addWidget(self.cardListUpdateButton, 2, 0, 1, 1)
        self.cardListUpdateButton.setText("更新卡片列表")

        self.enemyCardForm.weaponToStorage.hide()
        self.enemyCardForm.gloveToStorage.hide()
        self.enemyCardForm.ArmorToStorage.hide()
        self.enemyCardForm.helmetToStorage.hide()
        self.cardListUpdateButton = QPushButton(self)
        self.myCardForm.myCardListUpdate()
        self.cardListUpdateButton.clicked.connect(self.myCardForm.myCardListUpdate)
        self.myCardForm.gridLayout_8.addWidget(self.cardListUpdateButton, 2, 0, 1, 1)
        self.cardListUpdateButton.setText("更新卡片列表")

        self.enemycardListUpdateButton = QPushButton(self)
        self.enemyCardForm.myCardListUpdate()
        self.enemycardListUpdateButton.clicked.connect(self.enemyCardForm.myCardListUpdate)
        self.enemyCardForm.gridLayout_8.addWidget(self.enemycardListUpdateButton, 2, 0, 1, 1)
        self.enemycardListUpdateButton.setText("更新卡片列表")

    def closeEvent(self, event):
        global_env.mainWin.show()
        self.hide()

    def open(self):
        global_env.mainWin.hide()
        self.show()

    def openGearWindow(self):
        ecw = GearSetWindow(self, self.GearList)
        ecw.setWindowModality(Qt.ApplicationModal)
        ecw.Signal_OneParameter.connect(self.GearSet)
        ecw.open()

    def GearSet(self, GearList):
        self.GearList = GearList

    def showGear(self):
        text = ""
        for i in self.GearList:
            text += i.toString() + "\n"
        text += " " * 100
        QMessageBox.information(self, "备用详细数据", text, QMessageBox.Yes)

    def rightMenuShow(self):
        self.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
        self.contextMenu.show()

    def rightMenuCreat(self):
        self.contextMenu = QMenu(self)

        self.allImport = self.contextMenu.addAction(u'设置测试回数')

        self.allImport.triggered.connect(global_env.mainWin.set_tests)
