import re

from PySide2.QtGui import QIntValidator, QDoubleValidator, QCursor
from PySide2.QtWidgets import QComboBox, QLineEdit, QSpinBox, QWidget, QGridLayout, QLabel, QCheckBox, QMenu, \
    QInputDialog, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, SIGNAL, Slot)
from SystemClass import all_skill, all_character, all_equip, all_npc, all_amulet, getSkillIndexOfName, \
    getSkillIndexOfData, WishSet, \
    amuletClass
from cardClass import STATCard
import global_env
from skillChooseDialog import skillChooseWindow
from wishSetDialog import wishSetWindow
from amuletSetDialog import amuletSetWindow


class myComboBox(QComboBox):
    def __init__(self, parent=None):
        super(myComboBox, self).__init__(parent)

    def setCurrentIndex(self, index: int):
        if index >= self.count():
            index = self.count() - 1
        if index < 0:
            index = 0
        super(myComboBox, self).setCurrentIndex(index)


class skillComboBox(myComboBox):
    def __init__(self, parent=None):
        super(skillComboBox, self).__init__(parent)
        self.addItem("")
        self.setItemText(0, "无")
        for i in range(len(all_skill["name"])):
            self.addItem("")
            self.setItemText(i + 1, all_skill["name"][i])

    def currentValue(self):
        if self.currentIndex() == 0:
            return ""
        return all_skill["data"][self.currentIndex() - 1]


class npcSkillComboBox(skillComboBox):
    def __init__(self, parent=None):
        super(npcSkillComboBox, self).__init__(parent)
        self.addItem("随机技能")


class skillSlotNum(myComboBox):
    def __init__(self, parent=None):
        super(skillSlotNum, self).__init__(parent)
        self.addItem("")
        self.addItem("")
        self.addItem("")
        self.addItem("")
        self.setItemText(0, "1")
        self.setItemText(1, "2")
        self.setItemText(2, "3")
        self.setItemText(3, "4")


class npcTypeComboBox(myComboBox):
    def __init__(self, parent=None):
        super(npcTypeComboBox, self).__init__(parent)
        for i in range(4):
            self.addItem("")
            self.setItemText(i, all_npc["name"][i])


class npcHighGainComboBox(myComboBox):
    def __init__(self, parent=None):
        super(npcHighGainComboBox, self).__init__(parent)
        self.addItem("")
        self.addItem("")
        self.addItem("")
        self.addItem("")
        self.setItemText(0, "无")
        self.setItemText(1, "+30%")
        self.setItemText(2, "+70%")
        self.setItemText(3, "超级加倍")


class cardCharacterComboBox(myComboBox):
    def __init__(self, parent=None):
        super(cardCharacterComboBox, self).__init__(parent)
        for i in range(len(all_character["name"])):
            self.addItem("")
            self.setItemText(i, all_character["name"][i])

    def currentValue(self):
        return all_character["data"][self.currentIndex()]


class equipChooseComboBox(myComboBox):
    def __init__(self, parent=None):
        super(equipChooseComboBox, self).__init__(parent)
        name = self.name
        mylist = all_equip["name"][name]
        length = len(mylist)
        self.addItem("")
        self.setItemText(0, "无")
        for i in range(length):
            self.addItem("")
            self.setItemText(i + 1, mylist[i])

    def currentValue(self):
        return all_equip["data"][self.name][self.currentIndex()]


class weaponChooseComboBox(equipChooseComboBox):
    def __init__(self, parent=None):
        self.name = "weapon"
        super(weaponChooseComboBox, self).__init__(parent)


class gloveChooseComboBox(equipChooseComboBox):
    def __init__(self, parent=None):
        self.name = "glove"
        super(gloveChooseComboBox, self).__init__(parent)


class ArmorChooseComboBox(equipChooseComboBox):
    def __init__(self, parent=None):
        self.name = "Armor"
        super(ArmorChooseComboBox, self).__init__(parent)


class helmetChooseComboBox(equipChooseComboBox):
    def __init__(self, parent=None):
        self.name = "helmet"
        super(helmetChooseComboBox, self).__init__(parent)


class hasOrNotComboBox(myComboBox):
    def __init__(self, parent=None):
        super(hasOrNotComboBox, self).__init__(parent)
        self.addItem("")
        self.addItem("")
        self.setItemText(0, "无")
        self.setItemText(1, "有")

    def currentValue(self):
        if self.currentIndex() == 0:
            return False
        else:
            return True


class intLineEdit(QLineEdit):
    def __init__(self, parent=None, min=0, max=999999):
        super(intLineEdit, self).__init__(parent)
        self.min = min
        self.max = max
        qiv = QIntValidator()
        qiv.setRange(min, max)
        self.setValidator(qiv)

    def getValue(self):
        return int(self.text())

    def text(self) -> str:
        text = super(intLineEdit, self).text()
        if text == '':
            text = str(self.min)
        return text

    def setText(self, arg__1):
        super(intLineEdit, self).setText(str(arg__1))


class doubleLineEdit(QLineEdit):
    def __init__(self, parent=None, min=0, max=999999):
        super(doubleLineEdit, self).__init__(parent)
        qiv = QDoubleValidator()
        qiv.setRange(min, max)
        self.setValidator(qiv)


class bigSpinBox(QSpinBox):
    def __init__(self, parent=None, min=1, max=999999):
        super(bigSpinBox, self).__init__(parent)
        self.setRange(min, max)

    def getValue(self):
        return int(self.value())


class STATSkillCheckBox(QCheckBox):
    def __init__(self, text, ATTR, parent=None):
        super(STATSkillCheckBox, self).__init__(text, parent)
        self.ATTR = ATTR
        self.name = text

    def currentValue(self):
        return self.ATTR


class STATCardPanel(QWidget):
    def __init__(self, parent=None, cardList=None, cardlistcomboBox=None):
        super(STATCardPanel, self).__init__(parent)
        self.cardList = cardList
        self.cardlistcomboBox = cardlistcomboBox
        self.gridLayout = QGridLayout(self)

        self.nicknamelabel = QLabel(self)
        self.nicknamelabel.setText("卡片别名")

        self.nicknamelineedit = QLineEdit(self)

        self.cardtypelabel = QLabel(self)
        self.cardtypelabel.setText("卡片类型")

        self.cardtypecomboBox = cardCharacterComboBox(self)

        self.wishpanel = wishPanel()
        self.amuletpanel = amuletPanel()

        # gridLayout1__________________________

        self.gridLayout1 = QGridLayout()

        self.ADlabel = QLabel(self)
        self.ADlabel.setText("物攻")
        self.gridLayout1.addWidget(self.ADlabel, 0, 0, 1, 1)

        self.ADLineEdit = intLineEdit(self)
        self.gridLayout1.addWidget(self.ADLineEdit, 0, 1, 1, 1)

        self.APlabel = QLabel(self)
        self.APlabel.setText("魔攻")
        self.gridLayout1.addWidget(self.APlabel, 1, 0, 1, 1)

        self.APLineEdit = intLineEdit(self)
        self.gridLayout1.addWidget(self.APLineEdit, 1, 1, 1, 1)

        self.ADClabel = QLabel(self)
        self.ADClabel.setText("物穿")
        self.gridLayout1.addWidget(self.ADClabel, 2, 0, 1, 1)

        self.ADCLineEdit = intLineEdit(self)
        self.gridLayout1.addWidget(self.ADCLineEdit, 2, 1, 1, 1)

        self.ADCALineEdit = intLineEdit(self)
        self.gridLayout1.addWidget(self.ADCALineEdit, 2, 2, 1, 1)

        self.APClabel = QLabel(self)
        self.APClabel.setText("魔穿")
        self.gridLayout1.addWidget(self.APClabel, 3, 0, 1, 1)

        self.APCLineEdit = intLineEdit(self)
        self.gridLayout1.addWidget(self.APCLineEdit, 3, 1, 1, 1)

        self.APCALineEdit = intLineEdit(self)
        self.gridLayout1.addWidget(self.APCALineEdit, 3, 2, 1, 1)

        # gridLayout2__________________________

        self.gridLayout2 = QGridLayout()

        self.RTKlabel = QLabel(self)
        self.RTKlabel.setText("绝对攻击")
        self.gridLayout2.addWidget(self.RTKlabel, 0, 0, 1, 1)

        self.RTKLineEdit = intLineEdit(self)
        self.gridLayout2.addWidget(self.RTKLineEdit, 0, 1, 1, 1)

        self.CRITClabel = QLabel(self)
        self.CRITClabel.setText("暴击穿透")
        self.gridLayout2.addWidget(self.CRITClabel, 1, 0, 1, 1)

        self.CRITCLineEdit = intLineEdit(self)
        self.gridLayout2.addWidget(self.CRITCLineEdit, 1, 1, 1, 1)

        self.SPEEDlabel = QLabel(self)
        self.SPEEDlabel.setText("速度")
        self.gridLayout2.addWidget(self.SPEEDlabel, 2, 0, 1, 1)

        self.SPEEDLineEdit = intLineEdit(self)
        self.gridLayout2.addWidget(self.SPEEDLineEdit, 2, 1, 1, 1)

        self.WDEFlabel = QLabel(self)
        self.WDEFlabel.setText("物防")
        self.gridLayout2.addWidget(self.WDEFlabel, 3, 0, 1, 1)

        self.WDEFLineEdit = intLineEdit(self)
        self.gridLayout2.addWidget(self.WDEFLineEdit, 3, 1, 1, 1)

        self.WDEFALineEdit = intLineEdit(self)
        self.gridLayout2.addWidget(self.WDEFALineEdit, 3, 2, 1, 1)

        self.MDEFlabel = QLabel(self)
        self.MDEFlabel.setText("魔防")
        self.gridLayout2.addWidget(self.MDEFlabel, 4, 0, 1, 1)

        self.MDEFLineEdit = intLineEdit(self)
        self.gridLayout2.addWidget(self.MDEFLineEdit, 4, 1, 1, 1)

        self.MDEFALineEdit = intLineEdit(self)
        self.gridLayout2.addWidget(self.MDEFALineEdit, 4, 2, 1, 1)

        # gridLayout3__________________________

        self.gridLayout3 = QGridLayout()

        self.HEALTHlabel = QLabel(self)
        self.HEALTHlabel.setText("生命")
        self.gridLayout3.addWidget(self.HEALTHlabel, 0, 0, 1, 1)

        self.HEALTHLineEdit = intLineEdit(self)
        self.gridLayout3.addWidget(self.HEALTHLineEdit, 0, 1, 1, 1)

        self.RECOVERlabel = QLabel(self)
        self.RECOVERlabel.setText("回血")
        self.gridLayout3.addWidget(self.RECOVERlabel, 1, 0, 1, 1)

        self.RECOVERLineEdit = intLineEdit(self)
        self.gridLayout3.addWidget(self.RECOVERLineEdit, 1, 1, 1, 1)

        self.RECOVERALineEdit = intLineEdit(self)
        self.gridLayout3.addWidget(self.RECOVERALineEdit, 1, 2, 1, 1)

        self.SHIELDlabel = QLabel(self)
        self.SHIELDlabel.setText("护盾")
        self.gridLayout3.addWidget(self.SHIELDlabel, 2, 0, 1, 1)

        self.SHIELDLineEdit = intLineEdit(self)
        self.gridLayout3.addWidget(self.SHIELDLineEdit, 2, 1, 1, 1)

        self.SHIELDRECOVERlabel = QLabel(self)
        self.SHIELDRECOVERlabel.setText("回盾")
        self.gridLayout3.addWidget(self.SHIELDRECOVERlabel, 3, 0, 1, 1)

        self.SHIELDRECOVERLineEdit = intLineEdit(self)
        self.gridLayout3.addWidget(self.SHIELDRECOVERLineEdit, 3, 1, 1, 1)

        self.SHIELDRECOVERALineEdit = intLineEdit(self)
        self.gridLayout3.addWidget(self.SHIELDRECOVERALineEdit, 3, 2, 1, 1)

        # gridLayout4__________________________

        self.gridLayout4 = QGridLayout()

        self.CRITlabel = QLabel(self)
        self.CRITlabel.setText("暴击")
        self.gridLayout4.addWidget(self.CRITlabel, 0, 0, 1, 1)

        self.CRITLineEdit = intLineEdit(self)
        self.gridLayout4.addWidget(self.CRITLineEdit, 0, 1, 1, 1)

        self.SKILLlabel = QLabel(self)
        self.SKILLlabel.setText("技能")
        self.gridLayout4.addWidget(self.SKILLlabel, 1, 0, 1, 1)

        self.SKILLLineEdit = intLineEdit(self)
        self.gridLayout4.addWidget(self.SKILLLineEdit, 1, 1, 1, 1)

        self.REFLECTlabel = QLabel(self)
        self.REFLECTlabel.setText("反弹")
        self.gridLayout4.addWidget(self.REFLECTlabel, 2, 0, 1, 1)

        self.REFLECTLineEdit = intLineEdit(self)
        self.gridLayout4.addWidget(self.REFLECTLineEdit, 2, 1, 1, 1)

        self.VAMPIRElabel = QLabel(self)
        self.VAMPIRElabel.setText("吸血")
        self.gridLayout4.addWidget(self.VAMPIRElabel, 3, 0, 1, 1)

        self.VAMPIRELineEdit = intLineEdit(self)
        self.gridLayout4.addWidget(self.VAMPIRELineEdit, 3, 1, 1, 1)

        # gridLayout5__________________________

        self.gridLayout5 = QGridLayout()

        self.comboBoxList = []
        for i in range(5, len(all_skill["name"])):
            name = all_skill["name"][i]
            attr = all_skill["data"][i]
            if attr == "XUE":
                continue
            thisCombobox = STATSkillCheckBox(name, attr, self)
            self.comboBoxList.append(thisCombobox)

        thisCombobox = STATSkillCheckBox("荣誉之刃", "BLADE", self)
        self.comboBoxList.append(thisCombobox)
        thisCombobox = STATSkillCheckBox("刺杀弓", "ASSBOW", self)
        self.comboBoxList.append(thisCombobox)
        thisCombobox = STATSkillCheckBox("手环", "BRACELET", self)
        self.comboBoxList.append(thisCombobox)
        thisCombobox = STATSkillCheckBox("秃鹫手套", "VULTURE", self)
        self.comboBoxList.append(thisCombobox)
        thisCombobox = STATSkillCheckBox("发饰", "TIARA", self)
        self.comboBoxList.append(thisCombobox)
        thisCombobox = STATSkillCheckBox("幽梦匕首", "DAGGER", self)
        self.comboBoxList.append(thisCombobox)
        thisCombobox = STATSkillCheckBox("光辉法杖", "WAND", self)
        self.comboBoxList.append(thisCombobox)
        thisCombobox = STATSkillCheckBox("荆棘剑盾", "SHIELD", self)
        self.comboBoxList.append(thisCombobox)
        thisCombobox = STATSkillCheckBox("天使缎带", "RIBBON", self)
        self.comboBoxList.append(thisCombobox)
        thisCombobox = STATSkillCheckBox("陨铁重剑", "CLAYMORE", self)
        self.comboBoxList.append(thisCombobox)

        try:
            for i in range(5):
                for j in range(5):
                    self.gridLayout5.addWidget(self.comboBoxList[i * 5 + j], i, j, 1, 1)
        except:
            pass

        # gridLayout6__________________________

        self.gridLayout6 = QGridLayout()

        self.savepushButton = QPushButton()
        self.savepushButton.clicked.connect(self.saveMyCard)
        self.savepushButton.setText(u"保存卡片")
        self.gridLayout6.addWidget(self.savepushButton, 0, 0, 1, 1)

        self.editpushButton = QPushButton()
        self.editpushButton.clicked.connect(self.editMyCard)
        self.editpushButton.setText(u"修改卡片")
        self.gridLayout6.addWidget(self.editpushButton, 0, 1, 1, 1)

        self.deletepushButton = QPushButton()
        self.deletepushButton.clicked.connect(self.delMyCard)
        self.deletepushButton.setText(u"删除卡片")
        self.gridLayout6.addWidget(self.deletepushButton, 0, 2, 1, 1)

        # final

        self.rightMenuCreat()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)

        self.gridLayout.addWidget(self.nicknamelabel, 0, 0, 1, 1)  # 卡片别名
        self.gridLayout.addWidget(self.nicknamelineedit, 0, 1, 1, 1)  # 卡片别名QLineEdit
        self.gridLayout.addWidget(self.cardtypelabel, 1, 0, 1, 1)  # 卡片类型
        self.gridLayout.addWidget(self.cardtypecomboBox, 1, 1, 1, 1)  # 卡片类型comboBox
        self.gridLayout.addWidget(self.wishpanel, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.amuletpanel, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout1, 3, 0, 2, 1)  # 物攻
        self.gridLayout.addLayout(self.gridLayout2, 3, 1, 2, 1)  # 绝对攻击
        self.gridLayout.addLayout(self.gridLayout3, 5, 0, 2, 1)  # 生命
        self.gridLayout.addLayout(self.gridLayout4, 5, 1, 2, 1)  # 暴击
        self.gridLayout.addLayout(self.gridLayout5, 7, 0, 2, 2)  # 神秘
        self.gridLayout.addLayout(self.gridLayout6, 9, 0, 1, 2)  # 按钮

    def makeMyCard(self):
        nickname = self.nicknamelineedit.text()
        cardType = self.cardtypecomboBox.currentIndex()

        wishSet = WishSet(self.wishpanel.getWishLevelList())
        amuletclass = amuletClass(self.amuletpanel.getAmuletLevelList())

        attrs1 = []
        attrs1.append(self.ADLineEdit.getValue())
        attrs1.append(self.APLineEdit.getValue())
        attrs1.append(self.RTKLineEdit.getValue())
        attrs1.append(self.ADCLineEdit.getValue())
        attrs1.append(self.ADCALineEdit.getValue())
        attrs1.append(self.APCLineEdit.getValue())
        attrs1.append(self.APCALineEdit.getValue())
        attrs1.append(self.CRITCLineEdit.getValue())

        attrs2 = []
        attrs2.append(self.SPEEDLineEdit.getValue())
        attrs2.append(self.WDEFLineEdit.getValue())
        attrs2.append(self.WDEFALineEdit.getValue())
        attrs2.append(self.MDEFLineEdit.getValue())
        attrs2.append(self.MDEFALineEdit.getValue())

        attrs3 = []
        attrs3.append(self.HEALTHLineEdit.getValue())
        attrs3.append(self.RECOVERLineEdit.getValue())
        attrs3.append(self.RECOVERALineEdit.getValue())
        attrs3.append(self.SHIELDLineEdit.getValue())
        attrs3.append(self.SHIELDRECOVERLineEdit.getValue())
        attrs3.append(self.SHIELDRECOVERALineEdit.getValue())

        attrs4 = []
        attrs4.append(self.CRITLineEdit.getValue())
        attrs4.append(self.SKILLLineEdit.getValue())
        attrs4.append(self.REFLECTLineEdit.getValue())
        attrs4.append(self.VAMPIRELineEdit.getValue())

        attrs5 = [0]
        for i in self.comboBoxList:
            if i.isChecked():
                attrs5[0] += 1
                attrs5.append(i.currentValue())

        return STATCard(cardType, attrs1, attrs2, attrs3, attrs4, attrs5, nickname, wishSet, amuletclass)

    def ableCheck(self):
        return True, ""

    def saveMyCard(self):
        (result, message) = self.ableCheck()
        if not result:
            QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
            return
        try:
            newCard = self.makeMyCard()
            text, ok = QInputDialog.getText(self, '设置卡片显示名', '输入名称：', text=newCard.tostring())
            if ok and text:
                if text in self.cardList.keys():
                    QMessageBox.critical(self, "错误", "保存失败，与已有配置重名", QMessageBox.Yes)
                    return
                self.cardList[text] = newCard
                self.cardlistcomboBox.setCurrentText(text)
        except Exception as err:
            print(err)
            QMessageBox.critical(self, "错误", err.__str__(), QMessageBox.Yes)

    def editMyCard(self):
        (result, message) = self.ableCheck()
        if not result:
            QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
            return
        newCard = self.makeMyCard()
        # index = self.comboBox.currentIndex()
        text = self.cardlistcomboBox.currentText()
        if text == "":
            QMessageBox.critical(self, "错误", "修改失败，空名称", QMessageBox.Yes)
            return
        if text == "新卡片":
            QMessageBox.critical(self, "错误", "模板不可修改", QMessageBox.Yes)
            return
        yes = QMessageBox.question(self, "提问对话框", "确认修改？", QMessageBox.Yes | QMessageBox.No)
        if yes == QMessageBox.Yes:
            self.cardList[text] = newCard

    def delMyCard(self):
        text = self.cardlistcomboBox.currentText()
        if text == "新卡片":
            QMessageBox.critical(self, "错误", "模板不可删除", QMessageBox.Yes)
            return
        yes = QMessageBox.question(self, "提问对话框", "确认删除？", QMessageBox.Yes | QMessageBox.No)
        if yes == QMessageBox.Yes:
            del (self.cardList[text])

    def newMyCard(self):
        self.nicknamelineedit.setText("")
        self.cardtypecomboBox.setCurrentIndex(0)

        wishLevelList = [0, 0, 0, 0, 0, 0, 0]
        self.wishpanel.wishLevelList = wishLevelList
        self.amuletpanel.resetList()

        self.ADLineEdit.setText("")
        self.APLineEdit.setText("")
        self.RTKLineEdit.setText("")
        self.ADCLineEdit.setText("")
        self.ADCALineEdit.setText("")
        self.APCLineEdit.setText("")
        self.APCALineEdit.setText("")
        self.CRITCLineEdit.setText("")

        self.SPEEDLineEdit.setText("")
        self.WDEFLineEdit.setText("")
        self.WDEFALineEdit.setText("")
        self.MDEFLineEdit.setText("")
        self.MDEFALineEdit.setText("")

        self.HEALTHLineEdit.setText("")
        self.RECOVERLineEdit.setText("")
        self.RECOVERALineEdit.setText("")
        self.SHIELDLineEdit.setText("")
        self.SHIELDRECOVERLineEdit.setText("")
        self.SHIELDRECOVERALineEdit.setText("")

        self.CRITLineEdit.setText("")
        self.SKILLLineEdit.setText("")
        self.REFLECTLineEdit.setText("")
        self.VAMPIRELineEdit.setText("")

        for i in self.comboBoxList:
            i.setChecked(False)

    def setMyCard(self, card):
        cardtype = card.cardType
        attrs1 = card.attrs1
        attrs2 = card.attrs2
        attrs3 = card.attrs3
        attrs4 = card.attrs4
        attrs5 = card.attrs5
        if hasattr(card, "nickname"):
            nickname = card.nickname
            self.nicknamelineedit.setText(nickname)
        else:
            self.nicknamelineedit.setText("")

        self.cardtypecomboBox.setCurrentIndex(cardtype)

        if hasattr(card, "wishSet"):
            wishSet = card.wishSet
        else:
            wishSet = WishSet([0, 0, 0, 0, 0, 0, 0])

        if hasattr(card, "amuletclass"):
            amuletclass = card.amuletclass
        else:
            amuletclass = amuletClass([])

        self.wishpanel.wishLevelList = wishSet.getWishLevelList()
        self.amuletpanel.amuletLevelList = amuletclass.getAmuletLevelList()

        self.ADLineEdit.setText(attrs1[0])
        self.APLineEdit.setText(attrs1[1])
        self.RTKLineEdit.setText(attrs1[2])
        self.ADCLineEdit.setText(attrs1[3])
        self.ADCALineEdit.setText(attrs1[4])
        self.APCLineEdit.setText(attrs1[5])
        self.APCALineEdit.setText(attrs1[6])
        self.CRITCLineEdit.setText(attrs1[7])

        self.SPEEDLineEdit.setText(attrs2[0])
        self.WDEFLineEdit.setText(attrs2[1])
        self.WDEFALineEdit.setText(attrs2[2])
        self.MDEFLineEdit.setText(attrs2[3])
        self.MDEFALineEdit.setText(attrs2[4])

        self.HEALTHLineEdit.setText(attrs3[0])
        self.RECOVERLineEdit.setText(attrs3[1])
        self.RECOVERALineEdit.setText(attrs3[2])
        self.SHIELDLineEdit.setText(attrs3[3])
        self.SHIELDRECOVERLineEdit.setText(attrs3[4])
        self.SHIELDRECOVERALineEdit.setText(attrs3[5])

        self.CRITLineEdit.setText(attrs4[0])
        self.SKILLLineEdit.setText(attrs4[1])
        self.REFLECTLineEdit.setText(attrs4[2])
        self.VAMPIRELineEdit.setText(attrs4[3])

        for i in self.comboBoxList:
            if i.ATTR in attrs5:
                i.setChecked(True)
            else:
                i.setChecked(False)

    def rightMenuCreat(self):
        self.contextMenu = QMenu(self)
        self.cardImport = self.contextMenu.addAction(u'全部导入')
        self.cardImport.triggered.connect(lambda: self.cardImportFun())

        self.cardOutput = self.contextMenu.addAction(u'全部导出')
        self.cardOutput.triggered.connect(lambda: self.cardOutputFun())

    def rightMenuShow(self):
        self.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
        self.contextMenu.show()

    def wishImportFun(self, text=None):
        if text is None:
            text, ok = QInputDialog.getMultiLineText(self, '导入祝福', 'WISH 开头')
            if not (ok and text):
                return

        text = text.split(" ")
        if text[0] != "WISH":
            return
        else:
            wishLevelList = []
            for i in range(len(text) - 1):
                try:
                    wishLevelList.append(int(text[i + 1]))
                except:
                    pass
            self.wishpanel.wishLevelList = wishLevelList.copy()

    def amuletImportFun(self, text=None):
        if text is None:
            text, ok = QInputDialog.getMultiLineText(self, '导入护符', 'AMULET 开头,ENDAMULET结束')
            if not (ok and text):
                return

        text = text.split(" ")
        if text[0] != "AMULET":
            return
        else:
            amuletLevelList = [0] * len(all_amulet["data"])
            for i in range(1, len(text) - 2, 2):
                try:
                    name = text[i]
                    level = text[i + 1]
                    for j in range(len(all_amulet["data"])):
                        if all_amulet["data"][j] == name:
                            amuletLevelList[j] = int(level)
                except:
                    pass
            self.amuletpanel.amuletLevelList = amuletLevelList.copy()

    def cardImportFun(self, text=None):
        if text is None:
            text, ok = QInputDialog.getMultiLineText(self, '导入卡片', '计算器格式')
            if not (ok and text):
                return

        text = re.sub(r"\n\n", "\n", text)
        text = text.split("\n")

        attrs1 = text[0].split()
        if (len(attrs1) == 2):
            cardtype, nickname = attrs1[0].split("_")
            for i in range(len(all_character['data'])):
                if cardtype == all_character['data'][i]:
                    self.cardtypecomboBox.setCurrentIndex(i)
                    break
            self.nicknamelineedit.setText(nickname)
            text.pop(0)
            attrs1 = text[0].split()

        if attrs1[0] == "WISH":
            self.wishImportFun(text[0])
            text.pop(0)
            attrs1 = text[0].split()

        if attrs1[0] == "AMULET":
            self.amuletImportFun(text[0])
            text.pop(0)
            attrs1 = text[0].split()

        self.ADLineEdit.setText(attrs1[0])
        self.APLineEdit.setText(attrs1[1])
        self.RTKLineEdit.setText(attrs1[2])
        self.ADCLineEdit.setText(attrs1[3])
        self.ADCALineEdit.setText(attrs1[4])
        self.APCLineEdit.setText(attrs1[5])
        self.APCALineEdit.setText(attrs1[6])
        self.CRITCLineEdit.setText(attrs1[7])

        attrs2 = text[1].split()
        self.SPEEDLineEdit.setText(attrs2[0])
        self.WDEFLineEdit.setText(attrs2[1])
        self.WDEFALineEdit.setText(attrs2[2])
        self.MDEFLineEdit.setText(attrs2[3])
        self.MDEFALineEdit.setText(attrs2[4])

        attrs3 = text[2].split()
        self.HEALTHLineEdit.setText(attrs3[0])
        self.RECOVERLineEdit.setText(attrs3[1])
        self.RECOVERALineEdit.setText(attrs3[2])
        self.SHIELDLineEdit.setText(attrs3[3])
        self.SHIELDRECOVERLineEdit.setText(attrs3[4])
        self.SHIELDRECOVERALineEdit.setText(attrs3[5])

        attrs4 = text[3].split()
        self.CRITLineEdit.setText(attrs4[0])
        self.SKILLLineEdit.setText(attrs4[1])
        self.REFLECTLineEdit.setText(attrs4[2])
        self.VAMPIRELineEdit.setText(attrs4[3])

        others = text[4].split()
        for i in range(len(self.comboBoxList)):
            self.comboBoxList[i].setChecked(False)
            for j in range(1,len(others)):
                if others[j] == self.comboBoxList[i].ATTR:
                    self.comboBoxList[i].setChecked(True)

    def cardOutputFun(self, text=None):
        if not self.ableCheck():
            return

        thiscard = self.makeMyCard()
        thistext = thiscard.make_gu_text()
        QInputDialog.getMultiLineText(self, '请复制', "", thistext)


class cardSkillPanel(QWidget):
    def __init__(self, parent=None):
        super(cardSkillPanel, self).__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.skilllabels = []
        self.skillList = []

        self.skillslotcomboBox = skillSlotNum()
        self.skillslotcomboBox.setObjectName(u"技能位")
        self.vBoxLayout.addWidget(self.skillslotcomboBox)

        for i in range(4):
            tempskilllabel = QLabel(self)
            tempskilllabel.setText("无技能")
            self.skilllabels.append(tempskilllabel)
            self.vBoxLayout.addWidget(tempskilllabel)

        self.selectSkillButton = QPushButton()
        # self.selectSkillButton.clicked.connect(self.delMyCard)
        self.selectSkillButton.setText(u"选择天赋")
        self.vBoxLayout.addWidget(self.selectSkillButton)
        self.selectSkillButton.clicked.connect(lambda: self.runSkillChooseDialog())

    def setSkillFromList(self):
        skillList = self.skillList
        for i in range(4):
            if i < len(skillList):
                self.skilllabels[i].setText(all_skill['name'][skillList[i] - 1])
            else:
                self.skilllabels[i].setText("无技能")

    def runSkillChooseDialog(self):
        scw, skillList = skillChooseWindow.launch(self)
        if scw:
            self.skillList = skillList
            self.setSkillFromList()

    def get4index(self):
        indexlist = []
        for i in range(4):
            if i < len(self.skillList):
                indexlist.append(self.skillList[i])
            else:
                indexlist.append(0)
        return indexlist

    def getshortindex(self):
        return self.skillList.copy()

    def set4index(self, indexlist):
        skillList = []
        for i in range(4):
            if indexlist[i] == 0:
                break
            skillList.append(indexlist[i])
        self.skillList = skillList
        self.setSkillFromList()

    def setFromCaclText(self, text):
        skillList = []
        data = text.split()
        for i in range(1, len(data)):
            thisindex = getSkillIndexOfData(data[i])
            skillList.append(thisindex + 1)
        self.skillList = skillList
        self.setSkillFromList()

    def ablecheck(self):
        pass


class wishPanel(QWidget):
    def __init__(self, parent=None):
        super(wishPanel, self).__init__(parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.selectButton = QPushButton("选择许愿池系数")
        self.wishLevelList = [0, 0, 0, 0, 0, 0, 0]

        self.hBoxLayout.addWidget(self.selectButton)

        self.selectButton.clicked.connect(lambda: self.runwishSetDialog())

    def runwishSetDialog(self):
        scw, wishLevelList = wishSetWindow.launch(self)
        if scw:
            self.wishLevelList = wishLevelList

    def getWishLevelList(self):
        return self.wishLevelList.copy()


class amuletPanel(QWidget):
    def __init__(self, parent=None):
        super(amuletPanel, self).__init__(parent)
        self.hBoxLayout = QHBoxLayout(self)
        self.selectButton = QPushButton("设置护符")
        self.amuletLevelList = [0] * len(all_amulet["data"])

        self.hBoxLayout.addWidget(self.selectButton)
        self.selectButton.clicked.connect(lambda: self.runAmuletSetDialog())

    def runAmuletSetDialog(self):
        scw, amuletLevelList = amuletSetWindow.launch(self)
        if scw:
            self.amuletLevelList = amuletLevelList

    def getAmuletLevelList(self):
        return self.amuletLevelList.copy()

    def resetList(self):
        self.amuletLevelList = [0] * len(all_amulet["data"])


class excludeSkillPanel(cardSkillPanel):
    def __init__(self, parent=None):
        super(excludeSkillPanel, self).__init__(parent)
        self.skillslotcomboBox.hide()
        self.selectSkillButton.setText("排除天赋")

    def getExcludeSkills(self):
        text = ""
        for i in self.skillList:
            if text != "":
                text += "_"
            text += all_skill["data"][i - 1]
        return text

    def setExcludeSkills(self, text):
        data = text.split("_")
        skillList = []
        for i in data:
            if i != "":
                skillList.append(getSkillIndexOfData(i) + 1)
        self.skillList = skillList
        self.setSkillFromList()
