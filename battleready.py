# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'battleready.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtWidgets import *

import global_env
from action_def import execCmd

QString = type("")


class Ui_battleReadyForm(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(740, 482)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mycardlistWidget = QListWidget(Form)
        self.mycardlistWidget.setObjectName(u"mycardlistWidget")
        Form.setStyleSheet("""
    QListView::item:selected { color: blue; }
    QListView::item:selected { background-color: white; }
    QListView::item:selected { border: 1px solid red; }
        """)

        self.gridLayout.addWidget(self.mycardlistWidget, 0, 0, 1, 2)

        self.enemycardlistView = QListWidget(Form)
        self.enemycardlistView.setObjectName(u"enemycardlistView")
        self.enemycardlistView.setSelectionMode(QAbstractItemView.MultiSelection)
        self.gridLayout.addWidget(self.enemycardlistView, 0, 2, 1, 2)

        self.npclistView = QListWidget(Form)
        self.npclistView.setObjectName(u"npclistView")
        self.npclistView.setSelectionMode(QAbstractItemView.MultiSelection)
        self.gridLayout.addWidget(self.npclistView, 0, 4, 1, 2)

        # self.mycardpushButton = QPushButton(Form)
        # self.mycardpushButton.clicked.connect(self.chooseMyCard)
        # self.mycardpushButton.setObjectName(u"mycardpushButton")
        # self.gridLayout.addWidget(self.mycardpushButton, 1, 0, 1, 1)
        self.flashButton = QPushButton(Form)
        self.flashButton.clicked.connect(self.flash)
        self.flashButton.setObjectName(u"mycardpushButton")
        self.gridLayout.addWidget(self.flashButton, 1, 0, 1, 1)
        #
        # self.addenemycardpushButton = QPushButton(Form)
        # self.addenemycardpushButton.setObjectName(u"addenemycardpushButton")
        # self.addenemycardpushButton.clicked.connect(self.chooseEnemyCard)
        # self.gridLayout.addWidget(self.addenemycardpushButton, 1, 1, 1, 1)
        #
        # self.delenemycardpushButton = QPushButton(Form)
        # self.delenemycardpushButton.setObjectName(u"delenemycardpushButton")
        # self.delenemycardpushButton.clicked.connect(self.delEnemyCard)
        # self.gridLayout.addWidget(self.delenemycardpushButton, 1, 2, 1, 1)
        #
        # self.delnpcpushButton = QPushButton(Form)
        # self.delnpcpushButton.setObjectName(u"delnpcpushButton")
        # self.delnpcpushButton.clicked.connect(self.delNpc)
        # self.gridLayout.addWidget(self.delnpcpushButton, 1, 4, 1, 1)
        #
        # self.addnpcpushButton = QPushButton(Form)
        # self.addnpcpushButton.setObjectName(u"addnpcpushButton")
        # self.addnpcpushButton.clicked.connect(self.chooseNpcCard)
        # self.gridLayout.addWidget(self.addnpcpushButton, 1, 3, 1, 1)

        self.freebattlepushButton = QPushButton(Form)
        self.freebattlepushButton.setObjectName(u"battlepushButton")
        self.freebattlepushButton.clicked.connect(self.freeRunTest)
        self.gridLayout.addWidget(self.freebattlepushButton, 1, 4, 1, 1)

        self.battlepushButton = QPushButton(Form)
        self.battlepushButton.setObjectName(u"battlepushButton")
        self.battlepushButton.clicked.connect(self.runTest2)
        self.gridLayout.addWidget(self.battlepushButton, 1, 5, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        self.flash()
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle("战斗准备")
        # self.mycardpushButton.setText("选择我的卡片")
        self.flashButton.setText("刷新选项")
        # self.addenemycardpushButton.setText("添加敌方卡片")
        # self.delenemycardpushButton.setText("移除选择敌方")
        # self.delnpcpushButton.setText("移除选择NPC")
        # self.addnpcpushButton.setText("添加NPC")
        self.freebattlepushButton.setText("自定义命令战斗")
        self.battlepushButton.setText("模拟战斗！")

    # retranslateUi

    def open(self):
        global_env.mainWin.hide()
        # self.flash()
        self.show()

    def closeEvent(self, event):
        global_env.mainWin.show()
        event.accept()

    def chooseMyCard(self):
        items = global_env.myCardList.keys()
        item, ok = QInputDialog.getItem(self, "选择卡片", '我的卡片列表', items, 0, False)
        if ok and item and item != '新卡片':
            self.mycardlistWidget.clear()
            self.mycardlistWidget.addItem(item)

    def chooseEnemyCard(self):
        items = global_env.enemyCardList.keys()
        item, ok = QInputDialog.getItem(self, "选择卡片", '敌方卡片列表', items, 0, False)
        if ok and item and item != '新卡片':
            for i in range(self.enemycardlistView.count()):
                if item == self.enemycardlistView.item(i).text():
                    QMessageBox.critical(self, "错误", "敌方已在列表中", QMessageBox.Yes)
                    return
            self.enemycardlistView.addItem(item)

    def chooseNpcCard(self):
        items = global_env.npcList.keys()
        item, ok = QInputDialog.getItem(self, "选择npc", 'npc列表', items, 0, False)
        if ok and item and item != '新npc':
            for i in range(self.npclistView.count()):
                if item == self.npclistView.item(i).text():
                    QMessageBox.critical(self, "错误", "npc已在列表中", QMessageBox.Yes)
                    return
            self.npclistView.addItem(item)

    def delEnemyCard(self):
        for item in self.enemycardlistView.selectedItems():
            self.enemycardlistView.takeItem(self.enemycardlistView.row(item))

    def delNpc(self):
        for item in self.npclistView.selectedItems():
            self.npclistView.takeItem(self.npclistView.row(item))

    def runTest(self):
        if self.mycardlistWidget.count() == 0:
            QMessageBox.critical(self, "错误", "未选择我方卡片", QMessageBox.Yes)
            return
        if self.enemycardlistView.count() == 0 and self.npclistView.count() == 0:
            QMessageBox.critical(self, "错误", "未选择敌人", QMessageBox.Yes)
            return
        file_path = os.path.join(".", "newkf.in")
        # file_path = os.path.join("E:\\tools\\newkf", "newkf.in")
        gu_text = self.make_full_gu_text()
        if not gu_text:
            QMessageBox.critical(self, "错误", "选择的数据可能已被删除", QMessageBox.Yes)
            return
        with open(file_path, "w") as f:
            f.write(gu_text)
        result = execCmd()
        thisText = ""
        for i in result:
            thisText += i

        global_env.mainWin.textBrowser.setText(thisText)
        self.close()

    def runTest2(self):
        if len(self.mycardlistWidget.selectedItems()) == 0:
            QMessageBox.critical(self, "错误", "未选择我方卡片", QMessageBox.Yes)
            return
        if len(self.enemycardlistView.selectedItems()) == 0 and len(self.npclistView.selectedItems()) == 0:
            QMessageBox.critical(self, "错误", "未选择敌人", QMessageBox.Yes)
            return
        file_path = os.path.join(".", "newkf.in")
        # file_path = os.path.join("E:\\tools\\newkf", "newkf.in")
        gu_text = self.make_full_gu_text2()
        if not gu_text:
            QMessageBox.critical(self, "错误", "选择的数据可能已被删除", QMessageBox.Yes)
            return
        with open(file_path, "w") as f:
            f.write(gu_text)
        result = execCmd()
        thisText = ""
        for i in result:
            thisText += i

        global_env.mainWin.textBrowser.setText(thisText)
        self.close()


    def freeRunTest(self):
        if len(self.mycardlistWidget.selectedItems()) == 0:
            QMessageBox.critical(self, "错误", "未选择我方卡片", QMessageBox.Yes)
            return
        if len(self.enemycardlistView.selectedItems()) == 0 and len(self.npclistView.selectedItems()) == 0:
            QMessageBox.critical(self, "错误", "未选择敌人", QMessageBox.Yes)
            return
        text, ok = QInputDialog.getMultiLineText(self, '自定义参数战斗', '输入参数：', text=global_env.run_args)
        if not (ok and text):
            return
        global_env.run_args = text
        file_path = os.path.join(".", "newkf.in")
        # file_path = os.path.join("E:\\tools\\newkf", "newkf.in")
        gu_text = self.make_full_gu_text2()
        if not gu_text:
            QMessageBox.critical(self, "错误", "选择的数据可能已被删除", QMessageBox.Yes)
            return
        with open(file_path, "w") as f:
            f.write(gu_text)
        result = execCmd(text)
        thisText = ""
        for i in result:
            thisText += i

        global_env.mainWin.textBrowser.setText(thisText)
        self.close()


    def make_full_gu_text(self):
        try:
            myCardName = self.mycardlistWidget.item(0).text()
            myCard = global_env.myCardList[myCardName]

            enemyCardList = []
            npcList = []
            for i in range(self.enemycardlistView.count()):
                enemyCardName = self.enemycardlistView.item(i).text()
                enemyCardList.append(global_env.enemyCardList[enemyCardName])

            for i in range(self.npclistView.count()):
                npcName = self.npclistView.item(i).text()
                npcList.append(global_env.npcList[npcName])
        except KeyError:
            return False

        text = ""
        text += myCard.make_gu_text()
        text += "\n"
        text += "NPC\n"
        for i in npcList:
            text += i.make_gu_text()
            text += "\n"
        text += "ENDNPC\n"
        text += "\n"

        text += "PC\n"
        for i in enemyCardList:
            text += i.make_gu_text()
            text += '\n'
        text += "ENDPC\n"

        text += "GEAR\nENDGEAR"

        return text

    def make_full_gu_text2(self):
        try:
            myCardName = self.mycardlistWidget.selectedItems()[0].text()
            myCard = global_env.myCardList[myCardName]

            enemyCardList = []
            npcList = []
            for i in self.enemycardlistView.selectedItems():
                enemyCardName = i.text()
                enemyCardList.append(global_env.enemyCardList[enemyCardName])

            for i in self.npclistView.selectedItems():
                npcName = i.text()
                npcList.append(global_env.npcList[npcName])
        except KeyError:
            return False

        text = ""
        text += myCard.make_gu_text()
        text += "\n"
        text += "NPC\n"
        for i in npcList:
            text += i.make_gu_text()
            text += "\n"
        text += "ENDNPC\n"
        text += "\n"

        text += "PC\n"
        for i in enemyCardList:
            text += i.make_gu_text()
            text += '\n'
        text += "ENDPC\n"

        text += "GEAR\nENDGEAR"

        return text

    def flash(self):
        self.mycardlistWidget.clear()
        self.enemycardlistView.clear()
        self.npclistView.clear()
        for i in global_env.myCardList.keys():
            if i != "新卡片":
                self.mycardlistWidget.addItem(i)
        for i in global_env.enemyCardList.keys():
            if i != "新卡片":
                self.enemycardlistView.addItem(i)
        for i in global_env.npcList.keys():
            if i != "新npc":
                self.npclistView.addItem(i)
