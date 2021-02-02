from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *


class Ui_wishSetDialog(object):
    def __init__(self, *args, **kwargs):
        super(Ui_wishSetDialog, self).__init__(*args, **kwargs)
        self.wishLevelList = []
        self.wishLabelList = []
        self.wishSpinList = []

    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 200)
        self.vBoxLayout = QVBoxLayout(Dialog)

        for i in range(7):
            ilabel = QLabel(self)
            ispin = QSpinBox(self)
            self.wishLabelList.append(ilabel)
            self.wishSpinList.append(ispin)
            ihbox = QHBoxLayout()
            ihbox.addWidget(ilabel)
            ihbox.addWidget(ispin)
            self.vBoxLayout.addLayout(ihbox)

        self.wishLabelList[0].setText("生命药水")
        self.wishLabelList[1].setText("护盾药水")
        self.wishLabelList[2].setText("启程之誓")
        self.wishLabelList[3].setText("启程之心")
        self.wishLabelList[4].setText("启程之风")
        self.wishLabelList[5].setText("野怪伤害增强")
        self.wishLabelList[6].setText("野怪生命增强")


        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.vBoxLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("选择祝福")

    def return_value(self):
        for i in range(len(self.wishSpinList)):
            self.wishLevelList[i] = self.wishSpinList[i].value()


class wishSetWindow(Ui_wishSetDialog, QDialog):
    def __init__(self, parent=None):
        super(wishSetWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)
        self.wishLevelList = parent.wishLevelList
        self.setWindowModality(Qt.ApplicationModal)
        self.valueInit()

    @staticmethod
    def launch(parent):
        dlg = wishSetWindow(parent)
        r = dlg.exec_()
        if r:
            return True, dlg.wishLevelList
        return False, None,

    def accept(self):
        self.return_value()
        QDialog.accept(self)

    def valueInit(self):
        for i in range(len(self.wishSpinList)):
            self.wishSpinList[i].setValue(self.wishLevelList[i])
