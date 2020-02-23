# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'equipChooseWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, SIGNAL,Signal)
from PySide2 import QtGui
from PySide2.QtWidgets import *
import global_env
from SystemClass import EQUIPSet


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
        self.weaponlistWidget = QListWidget(self.centralwidget)
        self.weaponlistWidget.setObjectName(u"weaponlistWidget")
        self.weaponlistWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.gridLayout.addWidget(self.weaponlistWidget, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.clicked.connect(self.useEquip)
        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.flash)
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.glovelistWidget = QListWidget(self.centralwidget)
        self.glovelistWidget.setObjectName(u"glovelistWidget")
        self.glovelistWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.gridLayout.addWidget(self.glovelistWidget, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.clicked.connect(self.delEquip)
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.helmetlistWidget = QListWidget(self.centralwidget)
        self.helmetlistWidget.setObjectName(u"helmetlistWidget")
        self.helmetlistWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.gridLayout.addWidget(self.helmetlistWidget, 0, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(self.detailCat)
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.ArmorlistWidget = QListWidget(self.centralwidget)
        self.ArmorlistWidget.setObjectName(u"ArmorlistWidget")
        self.ArmorlistWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.gridLayout.addWidget(self.ArmorlistWidget, 0, 2, 1, 1)

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
            yes = QMessageBox.question(self, "提问对话框", "确认删除[" + item.text() + "]？", QMessageBox.Yes | QMessageBox.No)
            if yes == QMessageBox.Yes:
                del (global_env.equipStorageDict["weapon"][item.text()])
                self.weaponlistWidget.takeItem(self.weaponlistWidget.row(item))

        for item in self.glovelistWidget.selectedItems():
            yes = QMessageBox.question(self, "提问对话框", "确认删除[" + item.text() + "]？", QMessageBox.Yes | QMessageBox.No)
            if yes == QMessageBox.Yes:
                del (global_env.equipStorageDict["glove"][item.text()])
                self.glovelistWidget.takeItem(self.glovelistWidget.row(item))

        for item in self.ArmorlistWidget.selectedItems():
            yes = QMessageBox.question(self, "提问对话框", "确认删除[" + item.text() + "]？", QMessageBox.Yes | QMessageBox.No)
            if yes == QMessageBox.Yes:
                del (global_env.equipStorageDict["Armor"][item.text()])
                self.ArmorlistWidget.takeItem(self.ArmorlistWidget.row(item))

        for item in self.helmetlistWidget.selectedItems():
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


class equipChooseWindow(Ui_equipChooseWindow, QMainWindow):
    def __init__(self, parent=None):
        super(equipChooseWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/bitbug_favicon.ico'))
