# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'npc.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtWidgets import *

import global_env
from Qclass import skillComboBox, npcTypeComboBox, npcHighGainComboBox, intLineEdit, myComboBox
from SystemClass import skill, SKILLSet
from npcClass import npc

QString = type("")


class Ui_npcForm(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(281, 403)
        self.Form = Form
        # self.gridLayout = QGridLayout(Form)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.comboBox_2 = myComboBox(Form)
        self.npcListUpdate()
        self.comboBox_2.currentIndexChanged.connect(lambda: self.chooseNpc(self.comboBox_2.currentText()))
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 0, 1, 1, 2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.comboBox = npcTypeComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.skillComboBox0 = skillComboBox(Form)
        self.skillComboBox0.setObjectName(u"skillComboBox0")
        self.gridLayout.addWidget(self.skillComboBox0, 2, 1, 1, 2)

        self.skillComboBox1 = skillComboBox(Form)
        self.skillComboBox1.setObjectName(u"skillComboBox1")
        self.gridLayout.addWidget(self.skillComboBox1, 3, 1, 1, 2)

        self.skillComboBox2 = skillComboBox(Form)
        self.skillComboBox2.setObjectName(u"skillComboBox2")
        self.gridLayout.addWidget(self.skillComboBox2, 4, 1, 1, 2)

        self.skillComboBox3 = skillComboBox(Form)
        self.skillComboBox3.setObjectName(u"skillComboBox3")
        self.gridLayout.addWidget(self.skillComboBox3, 5, 1, 1, 2)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.lineEdit = intLineEdit(Form, max=500)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 6, 2, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)

        self.comboBox_4 = npcHighGainComboBox(Form)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout.addWidget(self.comboBox_4, 7, 2, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.clicked.connect(self.saveNpc)
        self.pushButton.setObjectName(u"pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.clicked.connect(self.editNpc)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 8, 1, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.clicked.connect(self.delNpc)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 8, 2, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle("NPC")
        self.label_2.setText("npc列表")
        self.label.setText("NPC类型")

        self.label_3.setText("技能")

        self.label_4.setText("等级")
        self.label_5.setText("NPC高收益")

        self.pushButton.setText("存储配置")
        self.pushButton_2.setText("覆盖当前")
        self.pushButton_3.setText("删除当前")

    # retranslateUi
    def changeToLine(self):
        self.label_2.hide()
        self.label.hide()
        # self.label_3.hide()
        self.label_4.hide()
        # self.label_5.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.comboBox_2.hide()

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.comboBox.addItem("不测试")
        self.lvLabel = QLabel("lv")
        self.gridLayout.addWidget(self.lvLabel, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.gridLayout.setColumnMinimumWidth(2,30)
        self.label_5.setText("强度")
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.comboBox_4.addItem("全部强度")
        self.gridLayout.addWidget(self.comboBox_4, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)
        self.gridLayout.addWidget(self.skillComboBox0, 0, 6, 1, 1)
        self.gridLayout.addWidget(self.skillComboBox1, 0, 7, 1, 1)
        self.gridLayout.addWidget(self.skillComboBox2, 0, 8, 1, 1)
        self.gridLayout.addWidget(self.skillComboBox3, 0, 9, 1, 1)

    def open(self):
        global_env.mainWin.hide()
        self.show()

    def closeEvent(self, event):
        global_env.mainWin.show()
        event.accept()

    def makeNpc(self):
        npcType = self.comboBox.currentIndex()
        npcSkill_1 = skill(self.skillComboBox0.currentIndex())
        npcSkill_2 = skill(self.skillComboBox1.currentIndex())
        npcSkill_3 = skill(self.skillComboBox2.currentIndex())
        npcSkill_4 = skill(self.skillComboBox3.currentIndex())
        npcLevel = self.lineEdit.text()
        npcHighGain = self.comboBox_4.currentIndex()

        skillSet = SKILLSet(npcSkill_1, npcSkill_2, npcSkill_3, npcSkill_4)

        thisNpc = npc(npcType, skillSet, npcLevel, npcHighGain)
        return thisNpc

    def makeNpcList(self):
        npcType = self.comboBox.currentIndex()
        if npcType == 4:
            return []
        npcHighGain = self.comboBox_4.currentIndex()
        npcList = []
        if npcHighGain == 4:
            for i in range(4):
                self.comboBox_4.setCurrentIndex(i)
                npcList.append(self.makeNpc())
            self.comboBox_4.setCurrentIndex(4)
        else:
            npcList.append(self.makeNpc())
        return npcList

    def setNpc(self, thisNpc):
        npcType = thisNpc.role
        npcLevel = thisNpc.level
        npcHighGain = thisNpc.highGain
        skillSet = thisNpc.skillSet

        npcSkill_1 = skillSet.skill_1.data
        npcSkill_2 = skillSet.skill_2.data
        npcSkill_3 = skillSet.skill_3.data
        npcSkill_4 = skillSet.skill_4.data

        self.comboBox.setCurrentIndex(npcType)
        self.lineEdit.setText(npcLevel)
        self.comboBox_4.setCurrentIndex(npcHighGain)
        self.skillComboBox0.setCurrentIndex(npcSkill_1)
        self.skillComboBox1.setCurrentIndex(npcSkill_2)
        self.skillComboBox2.setCurrentIndex(npcSkill_3)
        self.skillComboBox3.setCurrentIndex(npcSkill_4)

    def newNpc(self):
        npcType = 0
        npcLevel = '1'
        npcHighGain = 0
        # skillSet = thisNpc.skillSet

        npcSkill_1 = 0
        npcSkill_2 = 0
        npcSkill_3 = 0
        npcSkill_4 = 0

        self.comboBox.setCurrentIndex(npcType)
        self.lineEdit.setText(npcLevel)
        self.comboBox_4.setCurrentIndex(npcHighGain)
        self.skillComboBox0.setCurrentIndex(npcSkill_1)
        self.skillComboBox1.setCurrentIndex(npcSkill_2)
        self.skillComboBox2.setCurrentIndex(npcSkill_3)
        self.skillComboBox3.setCurrentIndex(npcSkill_4)

    def npcListUpdate(self):
        npcList = global_env.npcList
        currentIndex = self.comboBox_2.currentIndex()
        self.comboBox_2.clear()
        for k, v in npcList.items():
            self.comboBox_2.addItem(k)
        self.comboBox_2.setCurrentIndex(currentIndex)

    def saveNpc(self):
        (result, message) = self.ableCheck()
        if not result:
            QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
            return
        newNpc = self.makeNpc()
        text, ok = QInputDialog.getText(self, '设置卡片显示名', '输入名称：', text=newNpc.tostring())
        if ok and text:
            if text in global_env.npcList.keys():
                QMessageBox.critical(self, "错误", "保存失败，与已有配置重名", QMessageBox.Yes)
                return
            global_env.npcList[text] = newNpc
            self.comboBox_2.setCurrentText(text)

    def editNpc(self):
        (result, message) = self.ableCheck()
        if not result:
            QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
            return
        newNpc = self.makeNpc()
        # index = self.comboBox.currentIndex()
        text = self.comboBox_2.currentText()
        if text == "":
            QMessageBox.critical(self, "错误", "修改失败，空名称", QMessageBox.Yes)
            return
        if text == "新npc":
            QMessageBox.critical(self, "错误", "模板不可修改", QMessageBox.Yes)
            return
        yes = QMessageBox.question(self, "提问对话框", "确认修改？", QMessageBox.Yes | QMessageBox.No)
        if yes == QMessageBox.Yes:
            global_env.npcList[text] = newNpc

    def delNpc(self):
        # index = self.comboBox.currentIndex()
        text = self.comboBox_2.currentText()
        if text == "新npc":
            QMessageBox.critical(self, "错误", "模板不可删除", QMessageBox.Yes)
            return
        yes = QMessageBox.question(self, "提问对话框", "确认删除？", QMessageBox.Yes | QMessageBox.No)
        if yes == QMessageBox.Yes:
            del (global_env.npcList[text])

    def chooseNpc(self, tag):  # combobox点击事件
        if tag not in global_env.npcList.keys():
            return
        mynpc = global_env.npcList[tag]
        if mynpc is None:
            self.newNpc()
        else:
            self.setNpc(mynpc)

    def ableCheck(self):
        skl_1 = self.skillComboBox0.currentIndex()
        skl_2 = self.skillComboBox1.currentIndex()
        skl_3 = self.skillComboBox2.currentIndex()
        skl_4 = self.skillComboBox3.currentIndex()
        sklList = []
        if skl_1 != 0:
            sklList.append(skl_1)
        if skl_2 != 0:
            if skl_2 in sklList:
                return False, "技能重复！"
            sklList.append(skl_2)
        if skl_3 != 0:
            if skl_3 in sklList:
                return False, "技能重复！"
            sklList.append(skl_3)
        if skl_4 != 0:
            if skl_4 in sklList:
                return False, "技能重复！"
            sklList.append(skl_4)
        return True, "无错误"
