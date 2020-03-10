# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'equipChooseWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, SIGNAL, Signal)
from PySide2 import QtGui
from PySide2.QtWidgets import *
import global_env
from SystemClass import EQUIPSet, all_equip, weaponEquip, gloveEquip, ArmorEquip, helmetEquip


class Ui_equipChooseWindow(object):
    Signal_OneParameter = Signal(EQUIPSet)

    def setupUi(self, equipChooseWindow):
        if equipChooseWindow.objectName():
            equipChooseWindow.setObjectName(u"equipChooseWindow")
        equipChooseWindow.resize(1007, 600)
        equipChooseWindow.setStyleSheet("""
        QListView::item:selected { color: blue; }
        QListView::item:selected { background-color: white; }
        QListView::item:selected { border: 1px solid red; }
            """)
        self.centralwidget = QWidget(equipChooseWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout2 = QGridLayout(self.centralwidget)
        self.gridLayout.addLayout(self.gridLayout2, 0, 0, 1, 1)
        self.gridLayout3 = QGridLayout(self.centralwidget)
        self.gridLayout.addLayout(self.gridLayout3, 1, 0, 1, 1)

        self.weaponlistWidget = QListWidget(self.centralwidget)
        self.weaponlistWidget.setObjectName(u"weaponlistWidget")
        self.weaponlistWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.gridLayout2.addWidget(self.weaponlistWidget, 0, 0, 1, 1)

        self.glovelistWidget = QListWidget(self.centralwidget)
        self.glovelistWidget.setObjectName(u"glovelistWidget")
        self.glovelistWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.gridLayout2.addWidget(self.glovelistWidget, 0, 1, 1, 1)

        self.helmetlistWidget = QListWidget(self.centralwidget)
        self.helmetlistWidget.setObjectName(u"helmetlistWidget")
        self.helmetlistWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.gridLayout2.addWidget(self.helmetlistWidget, 0, 3, 1, 1)

        self.ArmorlistWidget = QListWidget(self.centralwidget)
        self.ArmorlistWidget.setObjectName(u"ArmorlistWidget")
        self.ArmorlistWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.gridLayout2.addWidget(self.ArmorlistWidget, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.clicked.connect(self.useEquip)
        self.gridLayout3.addWidget(self.pushButton_4, 0, 4, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"GEAR设置")
        self.pushButton_5.clicked.connect(self.useGear)
        self.gridLayout3.addWidget(self.pushButton_5, 0, 4, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.flash)
        self.gridLayout3.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.clicked.connect(self.delEquip)
        self.gridLayout3.addWidget(self.pushButton_3, 0, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(self.detailCat)
        self.gridLayout3.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.importEquipFromTextButton = QPushButton(self.centralwidget)
        self.importEquipFromTextButton.setObjectName(u"")
        self.importEquipFromTextButton.clicked.connect(self.importEquipFromText)
        self.gridLayout3.addWidget(self.importEquipFromTextButton, 0, 2, 1, 1)

        equipChooseWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(equipChooseWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1007, 22))
        equipChooseWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(equipChooseWindow)
        self.statusbar.setObjectName(u"statusbar")
        equipChooseWindow.setStatusBar(self.statusbar)

        self.retranslateUi(equipChooseWindow)

        QMetaObject.connectSlotsByName(equipChooseWindow)

    # setupUi

    def retranslateUi(self, equipChooseWindow):
        equipChooseWindow.setWindowTitle("装备仓库")
        self.pushButton_4.setText("使用装备！")
        self.pushButton.setText("刷新列表")
        self.pushButton_3.setText("删除选中")
        self.pushButton_2.setText("查看详细")
        self.pushButton_5.setText("设为备用")
        self.importEquipFromTextButton.setText("导入装备")

        self.flash()

    # retranslateUi

    def open(self):
        # for i in ("weapon","glove","Armor","helmet"):
        #     for k,v in global_env[i].items():
        self.show()

    def flash(self):
        self.weaponlistWidget.clear()
        self.glovelistWidget.clear()
        self.ArmorlistWidget.clear()
        self.helmetlistWidget.clear()
        self.weaponlistWidget.addItems(global_env.equipStorageDict["weapon"].keys())
        self.glovelistWidget.addItems(global_env.equipStorageDict["glove"].keys())
        self.ArmorlistWidget.addItems(global_env.equipStorageDict["Armor"].keys())
        self.helmetlistWidget.addItems(global_env.equipStorageDict["helmet"].keys())

    def delEquip(self):
        for item in self.weaponlistWidget.selectedItems():
            if item.text() == "不改变":
                continue
            yes = QMessageBox.question(self, "提问对话框", "确认删除[" + item.text() + "]？", QMessageBox.Yes | QMessageBox.No)
            if yes == QMessageBox.Yes:
                del (global_env.equipStorageDict["weapon"][item.text()])
                self.weaponlistWidget.takeItem(self.weaponlistWidget.row(item))

        for item in self.glovelistWidget.selectedItems():
            if item.text() == "不改变":
                continue
            yes = QMessageBox.question(self, "提问对话框", "确认删除[" + item.text() + "]？", QMessageBox.Yes | QMessageBox.No)
            if yes == QMessageBox.Yes:
                del (global_env.equipStorageDict["glove"][item.text()])
                self.glovelistWidget.takeItem(self.glovelistWidget.row(item))

        for item in self.ArmorlistWidget.selectedItems():
            if item.text() == "不改变":
                continue
            yes = QMessageBox.question(self, "提问对话框", "确认删除[" + item.text() + "]？", QMessageBox.Yes | QMessageBox.No)
            if yes == QMessageBox.Yes:
                del (global_env.equipStorageDict["Armor"][item.text()])
                self.ArmorlistWidget.takeItem(self.ArmorlistWidget.row(item))

        for item in self.helmetlistWidget.selectedItems():
            if item.text() == "不改变":
                continue
            yes = QMessageBox.question(self, "提问对话框", "确认删除[" + item.text() + "]？", QMessageBox.Yes | QMessageBox.No)
            if yes == QMessageBox.Yes:
                del (global_env.equipStorageDict["helmet"][item.text()])
                self.helmetlistWidget.takeItem(self.helmetlistWidget.row(item))

    def detailCat(self):
        text = ""
        for item in self.weaponlistWidget.selectedItems():
            if item.text() == "不改变":
                continue
            text += "[" + item.text() + "]:\n"
            text += global_env.equipStorageDict["weapon"][item.text()].toString() + "\n"
        for item in self.glovelistWidget.selectedItems():
            if item.text() == "不改变":
                continue
            text += "[" + item.text() + "]:\n"
            text += global_env.equipStorageDict["glove"][item.text()].toString() + "\n"
        for item in self.ArmorlistWidget.selectedItems():
            if item.text() == "不改变":
                continue
            text += "[" + item.text() + "]:\n"
            text += global_env.equipStorageDict["Armor"][item.text()].toString() + "\n"
        for item in self.helmetlistWidget.selectedItems():
            if item.text() == "不改变":
                continue
            text += "[" + item.text() + "]:\n"
            text += global_env.equipStorageDict["helmet"][item.text()].toString() + "\n"
        text += " " * 100
        QMessageBox.information(self, "装备详细数据", text, QMessageBox.Yes)

    def useEquip(self):
        weapon = None
        glove = None
        Armor = None
        helmet = None
        if self.weaponlistWidget.selectedItems() and self.weaponlistWidget.selectedItems()[
            0].text() != "不改变":
            weapon = global_env.equipStorageDict["weapon"][self.weaponlistWidget.selectedItems()[0].text()]

        if self.glovelistWidget.selectedItems() and self.glovelistWidget.selectedItems()[
            0].text() != "不改变":
            glove = global_env.equipStorageDict["glove"][self.glovelistWidget.selectedItems()[0].text()]

        if self.ArmorlistWidget.selectedItems() and self.ArmorlistWidget.selectedItems()[
            0].text() != "不改变":
            Armor = global_env.equipStorageDict["Armor"][self.ArmorlistWidget.selectedItems()[0].text()]

        if self.helmetlistWidget.selectedItems() and self.helmetlistWidget.selectedItems()[
            0].text() != "不改变":
            helmet = global_env.equipStorageDict["helmet"][self.helmetlistWidget.selectedItems()[0].text()]

        equipset = EQUIPSet(weapon, glove, Armor, helmet)
        # self.emit(SIGNAL("EquipSetChoose"), equipset)
        self.Signal_OneParameter.emit(equipset)
        self.close()

    def useGear(self):
        gearList = []
        for item in self.weaponlistWidget.selectedItems():
            if item.text() == "不改变":
                continue
            gearList.append(global_env.equipStorageDict["weapon"][item.text()])
        for item in self.glovelistWidget.selectedItems():
            if item.text() == "不改变":
                continue
            gearList.append(global_env.equipStorageDict["glove"][item.text()])
        for item in self.ArmorlistWidget.selectedItems():
            if item.text() == "不改变":
                continue
            gearList.append(global_env.equipStorageDict["Armor"][item.text()])
        for item in self.helmetlistWidget.selectedItems():
            if item.text() == "不改变":
                continue
            gearList.append(global_env.equipStorageDict["helmet"][item.text()])

        # self.emit(SIGNAL("EquipSetChoose"), equipset)
        self.Signal_OneParameter.emit(gearList)
        self.close()

    def importEquipFromText(self):
        text, ok = QInputDialog.getMultiLineText(self, '导入装备', '咕咕镇计算器格式')
        if not (ok and text):
            return
        data = text.split()
        data = [data[i:i + 7] for i in range(0, len(data), 7)]
        for fequip in data:
            equipClass = None
            for i in range(len(all_equip['data']["weapon"])):
                if fequip[0] == all_equip['data']["weapon"][i]:
                    equiptype = i + 1
                    equipClass = weaponEquip
            if equipClass is None:
                for i in range(len(all_equip['data']["glove"])):
                    if fequip[0] == all_equip['data']["glove"][i]:
                        equiptype = i + 1
                        equipClass = gloveEquip
            if equipClass is None:
                for i in range(len(all_equip['data']["Armor"])):
                    if fequip[0] == all_equip['data']["Armor"][i]:
                        equiptype = i + 1
                        equipClass = ArmorEquip
            if equipClass is None:
                for i in range(len(all_equip['data']["helmet"])):
                    if fequip[0] == all_equip['data']["helmet"][i]:
                        equiptype = i + 1
                        equipClass = helmetEquip
            if equipClass is None:
                continue

            level = fequip[1]
            attr1 = fequip[2]
            attr2 = fequip[3]
            attr3 = fequip[4]
            attr4 = fequip[5]
            mystical = int(fequip[6])
            equip = equipClass(level, attr1, attr2, attr3, attr4, mystical, equiptype)

            equipParts = equip.partsText

            result0, result1 = self.preEquipToStorage(equip)
            if not result0:
                QMessageBox.critical(self, "错误", result1, QMessageBox.Yes)
                continue
            text, ok = QInputDialog.getText(self, '设置装备显示名', '输入名称：', text=equip.toSimpleString())
            if ok and text:
                if text in global_env.equipStorageDict[equipParts].keys():
                    QMessageBox.critical(self, "错误", "保存失败，与已有配置重名", QMessageBox.Yes)
                    continue
                global_env.equipStorageDict[equipParts][text] = equip
                self.flash()

    def preEquipToStorage(self, equip):
        if equip.equipType == 0:
            return False, "无类型装备无法添加!"
        if not global_env.test_mode:
            if int(equip.level) > 500:
                return False, "装备等级不能大于500!"
            if int(equip.attr0) < 50 or int(equip.attr1) < 50 or int(equip.attr2) < 50 or int(equip.attr3) < 50:
                return False, "装备属性不能小于50!"
            if int(equip.attr0) > 150 or int(equip.attr1) > 150 or int(equip.attr2) > 150 or int(equip.attr3) > 150:
                return False, "装备属性不能大于150!"

        return True, 'yes'

    # def setChosen(self,GearList):
    #     listWidget = None
    #     for i in GearList:
    #         if i.partsText == "weapon":
    #             listWidget = self.weaponlistWidget
    #         elif i.partsText == "glove":
    #             listWidget = self.glovelistWidget
    #         elif i.partsText == "Armor":
    #             listWidget = self.ArmorlistWidget
    #         elif i.partsText == "helmet":
    #             listWidget = self.helmetlistWidget
    #         else:
    #             return
    #         listWidget.findItems()


class equipChooseWindow(Ui_equipChooseWindow, QMainWindow):
    def __init__(self, parent=None):
        super(equipChooseWindow, self).__init__(parent)

        # self.setAcceptDrops(True)
        self.setupUi(self)
        self.pushButton_5.hide()


class GearSetWindow(Ui_equipChooseWindow, QMainWindow):
    def __init__(self, parent=None, GearList=[]):
        super(GearSetWindow, self).__init__(parent)
        # self.setAcceptDrops(True)

        self.setupUi(self)
        self.pushButton_4.hide()
        self.weaponlistWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.glovelistWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.ArmorlistWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.helmetlistWidget.setSelectionMode(QAbstractItemView.MultiSelection)
