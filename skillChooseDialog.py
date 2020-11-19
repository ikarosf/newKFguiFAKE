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
            thisCombobox.setWhatsThis(str(i + 1))
            self.comboBoxList.append(thisCombobox)
        j = 0
        k = 0
        n = 0
        m = 0
        for i in range(len(all_skill["name"])):
            if all_skill["cost"][i] == 10:
                self.gridLayout5.addWidget(self.comboBoxList[i], 0, j, 1, 1)
                j += 1
            elif all_skill["cost"][i] == 30:
                self.gridLayout5.addWidget(self.comboBoxList[i], 1, k, 1, 1)
                k += 1
            elif all_skill["cost"][i] == 50:
                self.gridLayout5.addWidget(self.comboBoxList[i], 2, n, 1, 1)
                n += 1
            elif all_skill["cost"][i] == 100:
                self.gridLayout5.addWidget(self.comboBoxList[i], 3, m, 1, 1)
                m += 1

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
            self.comboBoxList[i - 1].setChecked(True)
