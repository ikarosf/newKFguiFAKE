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

        self.label_2 = QLabel("次数:")
        self.label_2.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        self.intLineEdit = intLineEdit(self, min=1000, max=10000)
        self.grid_HBoxLayout.addWidget(self.label_2, 1)
        self.grid_HBoxLayout.addWidget(self.intLineEdit, 2)

        self.battleStartButton = QPushButton(self)
        self.battleStartButton.clicked.connect(self.battleStart)
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

    def battleStart(self):
        if not self.allAbleCheck():
            return
        newCard = self.myCardForm.makeMyCard()
        npcList = []
        for i in range(10):
            newNpc = self.npcFormList[i].makeNpcList()
            npcList += newNpc

        text = ""
        text += newCard.make_gu_text()
        text += "\n"
        text += "NPC\n"
        for i in npcList:
            text += i.make_gu_text()
            text += "\n"
        text += "ENDNPC\n"
        text += "\n"

        text += "PC\n"
        text += "ENDPC\n"
        text += "GEAR\nENDGEAR"

        file_path = os.path.join(".", "newkf.in")
        with open(file_path, "w") as f:
            f.write(text)

        num = str(self.intLineEdit.getValue())
        result, textList = execCmdReturn("bnpc " + num)
        thisText = ""
        if not result:
            global_env.mainWin.textBrowser.setText(textList)
            self.close()
            return
        self.index = 0

        def fun(matched):
            self.index += 1
            return npcList[self.index - 1].toFullString()

        for i in textList:
            i = re.sub(r'NPC\d\d', fun, i)
            thisText += i
        thisText = re.sub(r"\n", "\n\n", thisText)
        global_env.mainWin.textBrowser.setText(thisText)
        self.close()

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
