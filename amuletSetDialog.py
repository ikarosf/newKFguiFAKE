from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
from SystemClass import all_amulet
import math


class Ui_amuletSetDialog(object):
    def __init__(self, *args, **kwargs):
        super(Ui_amuletSetDialog, self).__init__(*args, **kwargs)
        self.amuletLevelList = []
        self.amuletLabelList = []
        self.amuletSpinList = []

    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 200)
        self.vBoxLayout = QVBoxLayout(Dialog)

        for i in range(math.ceil(len(all_amulet["data"]) / 3)):
            hboxLayout = QHBoxLayout()
            self.vBoxLayout.addLayout(hboxLayout)
            for j in range(3):
                index = i * 3 + j
                if index >= len(all_amulet["data"]):
                    break
                name = all_amulet["name"][index]
                ilabel = QLabel(self)
                ispin = QSpinBox(self)
                self.amuletLabelList.append(ilabel)
                self.amuletSpinList.append(ispin)
                ihbox = QHBoxLayout()
                ihbox.addWidget(ilabel)
                ihbox.addWidget(ispin)
                hboxLayout.addLayout(ihbox)

                ilabel.setText(name)

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
        Dialog.setWindowTitle("设置护符")

    def return_value(self):
        for i in range(len(self.amuletSpinList)):
            self.amuletLevelList[i] = self.amuletSpinList[i].value()


class amuletSetWindow(Ui_amuletSetDialog, QDialog):
    def __init__(self, parent=None):
        super(amuletSetWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)
        self.amuletLevelList = parent.amuletLevelList
        self.setWindowModality(Qt.ApplicationModal)
        self.valueInit()

    @staticmethod
    def launch(parent):
        dlg = amuletSetWindow(parent)
        r = dlg.exec_()
        if r:
            return True, dlg.amuletLevelList
        return False, None,

    def accept(self):
        self.return_value()
        QDialog.accept(self)

    def valueInit(self):
        for i in range(len(self.amuletLevelList)):
            self.amuletSpinList[i].setValue(self.amuletLevelList[i])
