from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

from SystemClass import all_skill


class Ui_skillChooseDialog(object):
    def __init__(self, *args, **kwargs):
        super(Ui_skillChooseDialog, self).__init__(*args, **kwargs)
        self.skilllist = []

    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 200)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayout5 = QGridLayout()
        self.gridLayout.addLayout(self.gridLayout5, 0, 0, 1, 4)

        self.comboBoxList = []
        for i in range(len(all_skill["name"])):
            name = all_skill["name"][i]
            thisCombobox = QCheckBox(name)
            thisCombobox.setWhatsThis(str(i+1))
            self.comboBoxList.append(thisCombobox)
        for i in range(3):
            self.gridLayout5.addWidget(self.comboBoxList[i], 0, i, 1, 1)
        for i in range(3, 6):
            self.gridLayout5.addWidget(self.comboBoxList[i], 1, i - 3, 1, 1)
        for i in range(6, 10):
            self.gridLayout5.addWidget(self.comboBoxList[i], 2, i - 6, 1, 1)
        for i in range(10, 13):
            self.gridLayout5.addWidget(self.comboBoxList[i], 3, i - 10, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 4)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("选择天赋")

    def return_value(self):
        self.skilllist = []
        for i in self.comboBoxList:
            if i.isChecked():
                self.skilllist.append(int(i.whatsThis()))


class skillChooseWindow(Ui_skillChooseDialog, QDialog):
    def __init__(self, parent=None):
        super(skillChooseWindow, self).__init__(parent)
        # self.setAcceptDrops(True)
        self.setupUi(self)
        self.skillList = parent.skillList
        self.setWindowModality(Qt.ApplicationModal)
        self.valueInit()

    @staticmethod
    def launch(parent):
        dlg = skillChooseWindow(parent)
        r = dlg.exec_()
        if r:
            return True, dlg.skilllist
        return False, None,

    def accept(self):
        self.return_value()
        QDialog.accept(self)

    def valueInit(self):
        for i in self.skillList:
            self.comboBoxList[i-1].setChecked(True)
