# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ALDialogWindow.ui'
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

from Qclass import npcHighGainComboBox, bigSpinBox

startLevel = 50
MUDifficulty = 3
ZHUDifficulty = 3
DENGDifficulty = 3
SHOUDifficulty = 3


class Ui_ALDialog(object):
    def __init__(self, *args, **kwargs):
        super(Ui_ALDialog, self).__init__(*args, **kwargs)
        self.startLevel = 1
        self.MUDifficulty = 3
        self.ZHUDifficulty = 3
        self.DENGDifficulty = 3
        self.SHOUDifficulty = 3
        self.cmd = "al"

    def setupUi(self, ALDialog):
        if ALDialog.objectName():
            ALDialog.setObjectName(u"ALDialog")
        ALDialog.resize(286, 174)
        self.gridLayout = QGridLayout(ALDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.MUlabel = QLabel(ALDialog)
        self.MUlabel.setObjectName(u"MUlabel")

        self.gridLayout.addWidget(self.MUlabel, 0, 0, 1, 1)

        self.MUcomboBox = npcHighGainComboBox(ALDialog)
        self.MUcomboBox.addItem("不挑战")
        self.MUcomboBox.setObjectName(u"MUcomboBox")

        self.gridLayout.addWidget(self.MUcomboBox, 0, 1, 1, 2)

        self.ZHUlabel = QLabel(ALDialog)
        self.ZHUlabel.setObjectName(u"ZHUlabel")

        self.gridLayout.addWidget(self.ZHUlabel, 0, 3, 1, 1)

        self.ZHUcomboBox = npcHighGainComboBox(ALDialog)
        self.ZHUcomboBox.addItem("不挑战")
        self.ZHUcomboBox.setObjectName(u"ZHUcomboBox")

        self.gridLayout.addWidget(self.ZHUcomboBox, 0, 4, 1, 1)

        self.DENGlabel = QLabel(ALDialog)
        self.DENGlabel.setObjectName(u"DENGlabel")

        self.gridLayout.addWidget(self.DENGlabel, 1, 0, 1, 1)

        self.DENGcomboBox = npcHighGainComboBox(ALDialog)
        self.DENGcomboBox.addItem("不挑战")

        self.DENGcomboBox.setObjectName(u"DENGcomboBox")

        self.gridLayout.addWidget(self.DENGcomboBox, 1, 1, 1, 2)

        self.SHOUlabel = QLabel(ALDialog)
        self.SHOUlabel.setObjectName(u"SHOUlabel")

        self.gridLayout.addWidget(self.SHOUlabel, 1, 3, 1, 1)

        self.SHOUcomboBox = npcHighGainComboBox(ALDialog)
        self.SHOUcomboBox.addItem("不挑战")

        self.SHOUcomboBox.setObjectName(u"SHOUcomboBox")

        self.gridLayout.addWidget(self.SHOUcomboBox, 1, 4, 1, 1)

        self.startlevellabel = QLabel(ALDialog)
        self.startlevellabel.setObjectName(u"startlevellabel")

        self.gridLayout.addWidget(self.startlevellabel, 2, 0, 1, 1)

        self.startlevelspinBox = bigSpinBox(ALDialog, min=1, max=200)

        self.startlevelspinBox.setObjectName(u"startlevelspinBox")

        self.gridLayout.addWidget(self.startlevelspinBox, 2, 1, 1, 1)

        self.buttonBox = QGridLayout(ALDialog)
        self.gridLayout.addLayout(self.buttonBox, 2, 2, 1, 3)

        self.ALButton = QPushButton(ALDialog)
        self.ALButton.setObjectName(u"ALButton")
        self.ALButton.clicked.connect(lambda: self.return_value("al"))
        self.buttonBox.addWidget(self.ALButton, 0, 0, 1, 1)

        self.ALCButton = QPushButton(ALDialog)
        self.ALCButton.setObjectName(u"ALCButton")
        self.ALCButton.clicked.connect(lambda: self.return_value("alc"))
        self.buttonBox.addWidget(self.ALCButton, 0, 1, 1, 1)

        self.retranslateUi(ALDialog)

        QMetaObject.connectSlotsByName(ALDialog)

    # setupUi

    def retranslateUi(self, ALDialog):
        ALDialog.setWindowTitle(QCoreApplication.translate("ALDialog", u"卡层计算", None))
        self.MUlabel.setText(QCoreApplication.translate("ALDialog", u"木人", None))
        self.ZHUlabel.setText(QCoreApplication.translate("ALDialog", u"迅捷蛛", None))
        self.DENGlabel.setText(QCoreApplication.translate("ALDialog", u"魔灯", None))
        self.SHOUlabel.setText(QCoreApplication.translate("ALDialog", u"食铁兽", None))
        self.startlevellabel.setText(QCoreApplication.translate("ALDialog", u"起始层", None))
        self.ALButton.setText("AL")
        self.ALCButton.setText("ALC")

    def return_value(self, cmd):
        global startLevel, MUDifficulty, ZHUDifficulty, DENGDifficulty, SHOUDifficulty
        startLevel = self.startlevelspinBox.getValue()
        MUDifficulty = self.MUcomboBox.currentIndex()
        ZHUDifficulty = self.ZHUcomboBox.currentIndex()
        DENGDifficulty = self.DENGcomboBox.currentIndex()
        SHOUDifficulty = self.SHOUcomboBox.currentIndex()

        self.startLevel = startLevel
        self.MUDifficulty = MUDifficulty
        if self.MUDifficulty == 4:
            self.MUDifficulty = -1

        self.ZHUDifficulty = ZHUDifficulty
        if self.ZHUDifficulty == 4:
            self.ZHUDifficulty = -1

        self.DENGDifficulty = DENGDifficulty
        if self.DENGDifficulty == 4:
            self.DENGDifficulty = -1

        self.SHOUDifficulty = SHOUDifficulty
        if self.SHOUDifficulty == 4:
            self.SHOUDifficulty = -1

        self.cmd = cmd
        self.accept()


class Ui_ALWindow(Ui_ALDialog, QDialog):
    def __init__(self, parent=None):
        super(Ui_ALWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.valueInit()

    @staticmethod
    def launch(parent):
        dlg = Ui_ALWindow(parent)
        r = dlg.exec_()
        if r:
            return True, dlg.cmd, dlg.startLevel, (
            dlg.MUDifficulty, dlg.ZHUDifficulty, dlg.DENGDifficulty, dlg.SHOUDifficulty)
        return False, None, None, None

    def valueInit(self):
        self.MUcomboBox.setCurrentIndex(MUDifficulty)
        self.ZHUcomboBox.setCurrentIndex(ZHUDifficulty)
        self.DENGcomboBox.setCurrentIndex(DENGDifficulty)
        self.SHOUcomboBox.setCurrentIndex(SHOUDifficulty)
        self.startlevelspinBox.setValue(startLevel)
