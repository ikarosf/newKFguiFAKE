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


class Ui_mutliChooseDialog(object):
    def __init__(self, *args, **kwargs):
        super(Ui_mutliChooseDialog, self).__init__(*args, **kwargs)
        self.value = ""
        self.attrClear = False
        self.skillClear = False

    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(434, 116)
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
        self.pushButton_3.clicked.connect(lambda: self.return_value("anpc", True))
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.return_value("apc", True))
        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 4)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout3")
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 2, 1, 2)

        self.checkbox = QCheckBox(Dialog)
        self.checkbox.setChecked(True)
        self.gridLayout_3.addWidget(self.checkbox, 0, 1, 1, 1)

        self.checkbox2 = QCheckBox(Dialog)
        self.checkbox2.setChecked(True)
        self.gridLayout_3.addWidget(self.checkbox2, 0, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)

        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 4)

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
        self.checkbox.setText("属性自动置1")
        self.checkbox2.setText("技能自动清空")

    # retranslateUi
    def return_value(self, text, aMode):
        self.value = text
        if aMode:
            if self.checkbox.isChecked():
                self.attrClear = True
            if self.checkbox2.isChecked():
                self.skillClear = True
        self.accept()


class mutliChooseWindow(Ui_mutliChooseDialog, QDialog):
    def __init__(self, parent=None):
        super(mutliChooseWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)

    @staticmethod
    def launch(parent):
        dlg = mutliChooseWindow(parent)
        r = dlg.exec_()
        if r:
            return True, dlg.value, (dlg.attrClear, dlg.skillClear)
        return False, None, None

    @staticmethod
    def simpleLaunch(parent):
        dlg = mutliChooseWindow(parent)
        dlg.pushButton_2.hide()
        dlg.pushButton_4.hide()
        r = dlg.exec_()
        if r:
            return True, dlg.value, (dlg.attrClear, dlg.skillClear)
        return False, None, None
