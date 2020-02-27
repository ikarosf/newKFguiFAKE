# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dailyBattleWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
import re

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtWidgets import *

import action_def
import global_env
from Qclass import npcHighGainComboBox, intLineEdit
from SystemClass import all_npc
from action_def import execCmdReturn


class Ui_dailybattlewindow(object):
    def __init__(self, *args, **kwargs):
        super(Ui_dailybattlewindow, self).__init__(*args, **kwargs)
        self.npcFormList = None
        self.myCardForm = None

    def setupUi(self, dailybattlewindow):
        if dailybattlewindow.objectName():
            dailybattlewindow.setObjectName(u"dailybattlewindow")
        dailybattlewindow.resize(800, 600)
        self.centralwidget = QWidget(dailybattlewindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.myCardForm, 0, 0, 1, 1)

        self.gridLayout_2 = QVBoxLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 2)

        dailybattlewindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(dailybattlewindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        dailybattlewindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(dailybattlewindow)
        self.statusbar.setObjectName(u"statusbar")
        dailybattlewindow.setStatusBar(self.statusbar)

        self.myCardFormSet()
        self.npcFormSet()
        self.retranslateUi(dailybattlewindow)
        QMetaObject.connectSlotsByName(dailybattlewindow)

    # setupUi

    def retranslateUi(self, dailybattlewindow):
        dailybattlewindow.setWindowTitle("日常战斗")

    # retranslateUi

    def npcFormSet(self):
        for i in range(10):
            self.gridLayout_2.addWidget(self.npcFormList[i])
            self.npcFormList[i].changeToLine()

        self.grid_HBoxLayout = QHBoxLayout()
        self.gridLayout_2.addLayout(self.grid_HBoxLayout)

        self.npcImportButton = QPushButton(self)
        self.npcImportButton.clicked.connect(self.npcImport)
        self.npcImportButton.setText(u"导入NPC")
        self.grid_HBoxLayout.addWidget(self.npcImportButton, 3)

        # self.allDifficultyButton = QPushButton(self)
        # self.allDifficultyButton.clicked.connect(self.allDifficultyChoose)
        # self.allDifficultyButton.setText(u"选择全部难度")
        # self.gridLayout_2_1.addWidget(self.allDifficultyButton)
        self.label = QLabel("难度:")
        self.label.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.combobox = npcHighGainComboBox(self)
        self.combobox.addItem("全部强度")
        self.combobox.currentIndexChanged.connect(lambda: self.allDifficultyChoose(self.combobox.currentIndex()))
        self.grid_HBoxLayout.addWidget(self.label, 1)
        self.grid_HBoxLayout.addWidget(self.combobox, 2)

        self.freebattlepushButton = QPushButton(self)
        self.freebattlepushButton.clicked.connect(self.freeBattleStart)
        self.freebattlepushButton.setText(u"自定义命令战斗")
        self.grid_HBoxLayout.addWidget(self.freebattlepushButton, 3)

        self.battleStartButton = QPushButton(self)
        self.battleStartButton.clicked.connect(lambda: self.battleStart())
        self.battleStartButton.setText(u"开始测试")
        self.grid_HBoxLayout.addWidget(self.battleStartButton, 3)

    def allAbleCheck(self):
        (result, message) = self.myCardForm.ableCheck()
        if not result:
            QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
            return False
        for i in range(10):
            (result, message) = self.npcFormList[i].ableCheck()
            if not result:
                QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
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

    def battleStart(self, cmd_text=None):
        if not self.allAbleCheck():
            return
        if cmd_text is None:
            items = ["bnpc", "anpc"]
            cmd_text, ok = QInputDialog.getItem(self, "选择命令", '', items, 0, False)
            if not (ok and cmd_text):
                return
        aMode = False
        if cmd_text.startswith("a"):
            yes = QMessageBox.question(self, "自动置1", "算点时是否自动将卡片点数全置1", QMessageBox.Yes | QMessageBox.No)
            if yes == QMessageBox.Yes:
                aMode = True
        text = self.make_full_gu_text(aMode)
        file_path = os.path.join(".", "newkf.in")
        with open(file_path, "w") as f:
            f.write(text)

        mythread = action_def.execCmdWorker(parent=self, item=cmd_text)
        mythread.my_signal.connect(action_def.after_calculate)
        action_def.before_calculate()
        mythread.start()
        self.close()

    def make_full_gu_text(self, aMode=False):
        newCard = self.myCardForm.makeMyCard()
        if aMode:
            newCard.attrSet.STR = 1
            newCard.attrSet.AGI = 1
            newCard.attrSet.INT = 1
            newCard.attrSet.VIT = 1
            newCard.attrSet.SPR = 1
            newCard.attrSet.RES = 1
        npcList = []
        for i in range(10):
            newNpc = self.npcFormList[i].makeNpcList()
            npcList += newNpc

        text = action_def.make_full_gu_text(newCard, npcList)
        return text

    def allDifficultyChoose(self, index):
        for i in range(10):
            self.npcFormList[i].comboBox_4.setCurrentIndex(index)

    def npcImport(self):
        text, ok = QInputDialog.getMultiLineText(self, '导入全部npc', '如“Lv60 铁皮木人”：')
        if not (ok and text):
            return
        npcList = re.findall(r'Lv(\d+) ([\u4E00-\u9FA5]+)', text)
        print(npcList)
        for i in range(len(npcList)):
            thisType = npcList[i][1]
            thisLv = npcList[i][0]
            for j in range(len(all_npc["name"])):
                if all_npc["name"][j] in thisType:
                    self.npcFormList[i].comboBox.setCurrentIndex(j)
                    self.npcFormList[i].lineEdit.setText(thisLv)
                    break

    def myCardFormSet(self):
        self.myCardForm.pushButton.hide()
        self.myCardForm.pushButton_2.hide()
        self.myCardForm.pushButton_3.hide()
        self.myCardForm.weaponToStorage.hide()
        self.myCardForm.gloveToStorage.hide()
        self.myCardForm.ArmorToStorage.hide()
        self.myCardForm.helmetToStorage.hide()
        self.cardListUpdateButton = QPushButton(self)
        self.myCardForm.myCardListUpdate()
        self.cardListUpdateButton.clicked.connect(self.myCardForm.myCardListUpdate)
        self.myCardForm.gridLayout_8.addWidget(self.cardListUpdateButton, 2, 0, 1, 1)
        self.cardListUpdateButton.setText("更新卡片列表")

    def closeEvent(self, event):
        global_env.mainWin.show()
        self.hide()

    def open(self):
        global_env.mainWin.hide()
        self.show()
