from PySide2.QtGui import QIntValidator, QDoubleValidator
from PySide2.QtWidgets import QComboBox, QLineEdit, QSpinBox
from SystemClass import all_skill, all_character, all_equip, all_npc


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
        for i in range(11):
            self.addItem("")
            self.setItemText(i + 1, all_skill["name"][i])

    def currentValue(self):
        if self.currentIndex() == 0:
            return ""
        return all_skill["data"][self.currentIndex() - 1]


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
        for i in range(4):
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
    def __init__(self, parent=None, min=0, max=9999):
        super(intLineEdit, self).__init__(parent)
        qiv = QIntValidator()
        qiv.setRange(min, max)
        self.setValidator(qiv)

    def getValue(self):
        return int(self.text())

    def text(self) -> str:
        text = super(intLineEdit, self).text()
        if text == '':
            text = '0'
        return text


class doubleLineEdit(QLineEdit):
    def __init__(self, parent=None, min=0, max=9999):
        super(doubleLineEdit, self).__init__(parent)
        qiv = QDoubleValidator()
        qiv.setRange(min, max)
        self.setValidator(qiv)


class bigSpinBox(QSpinBox):
    def __init__(self, parent=None, min=1, max=9999):
        super(bigSpinBox, self).__init__(parent)
        self.setRange(min, max)

    def getValue(self):
        return int(self.value())
