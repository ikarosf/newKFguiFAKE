# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mutliChooseDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

from ALDialogWindow import Ui_ALWindow

attrClear = True
skillClear = True
equipClear = True
DEFENDERmode = False


class Ui_mutliChooseDialog(object):
    def __init__(self, *args, **kwargs):
        super(Ui_mutliChooseDialog, self).__init__(*args, **kwargs)
        self.value = ""
        self.attrClear = False
        self.skillClear = False
        self.equipClear = False
        self.DEFENDERmode = False

    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 130)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(lambda: self.return_value("bnpc", False))
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.return_value("bpc", False))
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet("color:red;")
        self.pushButton_3.clicked.connect(lambda: self.return_value("anpc", True))
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet("color:red;")
        self.pushButton_4.clicked.connect(lambda: self.return_value("apc", True))
        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 4)

        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet("color:red;")
        self.pushButton_5.clicked.connect(lambda: self.openALDialog())
        self.gridLayout_2.addWidget(self.pushButton_5, 1, 0, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout3")
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 2, 1, 2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout3")
        self.gridLayout_2.addLayout(self.gridLayout_4, 2, 3, 1, 2)

        self.checkbox = QCheckBox(Dialog)
        self.checkbox.setStyleSheet("color:red;")
        self.gridLayout_3.addWidget(self.checkbox, 0, 1, 1, 1)

        self.checkbox2 = QCheckBox(Dialog)
        self.checkbox2.setStyleSheet("color:red;")
        self.gridLayout_3.addWidget(self.checkbox2, 0, 2, 1, 1)

        self.checkbox3 = QCheckBox(Dialog)
        self.checkbox3.setStyleSheet("color:red;")
        self.gridLayout_3.addWidget(self.checkbox3, 0, 3, 1, 1)

        self.checkbox4 = QCheckBox(Dialog)
        self.gridLayout_3.addWidget(self.checkbox4, 0, 4, 1, 1)

        self.tiplabel = QLabel(Dialog)
        self.tiplabel.setStyleSheet("color:red;")
        self.gridLayout_4.addWidget(self.tiplabel, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)

        self.gridLayout_2.addWidget(self.buttonBox, 3, 1, 1, 4)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("测试参数")
        self.pushButton.setText("bnpc")
        self.pushButton_2.setText("bpc")
        self.pushButton_3.setText("anpc")
        self.pushButton_4.setText("apc")
        self.pushButton_5.setText("al")
        self.checkbox.setText("属性自动置1")
        self.checkbox2.setText("技能自动清空")
        self.checkbox3.setText("装备自动清空")
        self.checkbox4.setText("防守模式")
        self.tiplabel.setText("选择装备清空请先设置备选装备")

    # retranslateUi
    def return_value(self, text, aMode):
        self.value = text
        if aMode:
            if self.checkbox.isChecked():
                self.attrClear = True
            if self.checkbox2.isChecked():
                self.skillClear = True
            if self.checkbox3.isChecked():
                self.equipClear = True
        if self.checkbox4.isChecked():
            self.DEFENDERmode = True
        self.accept()

    def openALDialog(self):
        mcw, cmd, startLevel, difficultyList = Ui_ALWindow.launch(self)
        if mcw:
            text = "startlevel " + str(startLevel) + "\n" + cmd + " "
            for item in difficultyList:
                text += str(item) + " "
            self.return_value(text, True)


class mutliChooseWindow(Ui_mutliChooseDialog, QDialog):
    def __init__(self, parent=None):
        super(mutliChooseWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.valueInit()

    @staticmethod
    def launch(parent):
        dlg = mutliChooseWindow(parent)
        r = dlg.exec_()
        if r:
            return True, dlg.value, (dlg.attrClear, dlg.skillClear, dlg.equipClear, dlg.DEFENDERmode)
        return False, None, None

    @staticmethod
    def npcLaunch(parent):
        dlg = mutliChooseWindow(parent)
        dlg.pushButton_2.hide()
        dlg.pushButton_4.hide()
        dlg.checkbox4.hide()
        r = dlg.exec_()
        if r:
            return True, dlg.value, (dlg.attrClear, dlg.skillClear, dlg.equipClear, dlg.DEFENDERmode)
        return False, None, None

    @staticmethod
    def pcLaunch(parent):
        dlg = mutliChooseWindow(parent)
        dlg.pushButton.hide()
        dlg.pushButton_3.hide()
        dlg.pushButton_5.hide()
        r = dlg.exec_()
        if r:
            return True, dlg.value, (dlg.attrClear, dlg.skillClear, dlg.equipClear, dlg.DEFENDERmode)
        return False, None, None

    def accept(self):
        global attrClear, skillClear, equipClear,DEFENDERmode
        attrClear = self.checkbox.isChecked()
        skillClear = self.checkbox2.isChecked()
        equipClear = self.checkbox3.isChecked()
        DEFENDERmode = self.checkbox4.isChecked()
        QDialog.accept(self)

    def valueInit(self):
        self.checkbox.setChecked(attrClear)
        self.checkbox2.setChecked(skillClear)
        self.checkbox3.setChecked(equipClear)
        self.checkbox4.setChecked(DEFENDERmode)
