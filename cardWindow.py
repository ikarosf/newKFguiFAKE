from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtWidgets import *

import global_env
from Qclass import skillComboBox, skillSlotNum, cardCharacterComboBox, weaponChooseComboBox, gloveChooseComboBox, \
    ArmorChooseComboBox, helmetChooseComboBox, hasOrNotComboBox, intLineEdit, bigSpinBox, myComboBox
from SystemClass import cardAttr, skill, SKILLSet, weaponEquip, ArmorEquip, gloveEquip, helmetEquip, EQUIPSet
from action_def import text_to_equipSet
from cardClass import myCard

QString = type("")


class Ui_cardForm(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(575, 602)
        self.gridLayout_9 = QGridLayout(Form)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"mycardlist")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox = myComboBox(Form)
        self.myCardListUpdate()
        self.comboBox.currentIndexChanged.connect(lambda: self.chooseMyCard(self.comboBox.currentText()))
        self.comboBox.setObjectName(u"mycardlist")

        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 3)

        self.gridLayout_9.addLayout(self.gridLayout_3, 0, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"光环")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit = intLineEdit(parent=Form, max=200)  # 光环
        self.lineEdit.setObjectName(u"光环")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"卡片类型")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.comboBox_7 = cardCharacterComboBox(Form)
        self.comboBox_7.setObjectName(u"卡片类型")

        self.gridLayout.addWidget(self.comboBox_7, 1, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"卡片等级")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.lineEdit_2 = intLineEdit(parent=Form, max=500)  # 等级
        self.lineEdit_2.setObjectName(u"卡片等级")
        self.lineEdit_2.textEdited.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.remainder_point_text = QLabel(Form)
        self.remainder_point_text.setObjectName(u"点数文本")
        self.gridLayout.addWidget(self.remainder_point_text, 3, 0, 1, 1)
        self.remainder_point = QLabel(Form)
        self.remainder_point.setObjectName(u"点数")
        self.gridLayout.addWidget(self.remainder_point, 3, 1, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"力量")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.spinBox = bigSpinBox(Form)
        self.spinBox.setObjectName(u"力量")
        self.spinBox.valueChanged.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.spinBox, 4, 1, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"敏捷")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.spinBox_2 = bigSpinBox(Form)
        self.spinBox_2.setObjectName(u"敏捷")
        self.spinBox_2.valueChanged.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.spinBox_2, 5, 1, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"智力")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.spinBox_3 = bigSpinBox(Form)
        self.spinBox_3.setObjectName(u"智力")
        self.spinBox_3.valueChanged.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.spinBox_3, 6, 1, 1, 1)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"体魄")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.spinBox_4 = bigSpinBox(Form)
        self.spinBox_4.setObjectName(u"体魄")
        self.spinBox_4.valueChanged.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.spinBox_4, 7, 1, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"精神")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.spinBox_5 = bigSpinBox(Form)
        self.spinBox_5.setObjectName(u"精神")
        self.spinBox_5.valueChanged.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.spinBox_5, 8, 1, 1, 1)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"意志")

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.spinBox_6 = bigSpinBox(Form)
        self.spinBox_6.setObjectName(u"意志")
        self.spinBox_6.valueChanged.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.spinBox_6, 9, 1, 1, 1)

        self.gridLayout_9.addLayout(self.gridLayout, 1, 0, 2, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"武器类型")

        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)

        self.lineEdit_5 = intLineEdit(Form, max=500)
        self.lineEdit_5.setObjectName(u"武器属性2")

        self.gridLayout_4.addWidget(self.lineEdit_5, 2, 2, 1, 1)

        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"等级")

        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)

        self.lineEdit_4 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_4.setObjectName(u"武器属性1")

        self.gridLayout_4.addWidget(self.lineEdit_4, 2, 1, 1, 1)

        self.lineEdit_7 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_7.setObjectName(u"武器属性4")

        self.gridLayout_4.addWidget(self.lineEdit_7, 2, 4, 1, 1)

        self.lineEdit_6 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_6.setObjectName(u"武器属性3")

        self.gridLayout_4.addWidget(self.lineEdit_6, 2, 3, 1, 1)

        self.lineEdit_3 = intLineEdit(Form, min=1, max=500)
        self.lineEdit_3.setObjectName(u"武器等级")

        self.gridLayout_4.addWidget(self.lineEdit_3, 1, 1, 1, 3)

        self.comboBox_8 = weaponChooseComboBox(Form)
        self.comboBox_8.setObjectName(u"武器类型")

        self.gridLayout_4.addWidget(self.comboBox_8, 0, 1, 1, 2)

        self.comboBox_9 = hasOrNotComboBox(Form)
        self.comboBox_9.setObjectName(u"武器神秘")

        self.gridLayout_4.addWidget(self.comboBox_9, 3, 1, 1, 2)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"属性百分比")

        self.gridLayout_4.addWidget(self.label_15, 2, 0, 1, 1)

        self.label_16 = QLabel(Form)
        self.label_16.setObjectName(u"武器神秘")

        self.gridLayout_4.addWidget(self.label_16, 3, 0, 1, 1)

        self.gridLayout_9.addLayout(self.gridLayout_4, 1, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit_8 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_8.setObjectName(u"手套属性1")

        self.gridLayout_5.addWidget(self.lineEdit_8, 2, 1, 1, 1)

        self.label_17 = QLabel(Form)
        self.label_17.setObjectName(u"手套类型")

        self.gridLayout_5.addWidget(self.label_17, 0, 0, 1, 1)

        self.lineEdit_9 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_9.setObjectName(u"手套属性2")

        self.gridLayout_5.addWidget(self.lineEdit_9, 2, 2, 1, 1)

        self.lineEdit_10 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_10.setObjectName(u"手套属性4")

        self.gridLayout_5.addWidget(self.lineEdit_10, 2, 4, 1, 1)

        self.lineEdit_11 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_11.setObjectName(u"手套属性3")

        self.gridLayout_5.addWidget(self.lineEdit_11, 2, 3, 1, 1)

        self.label_18 = QLabel(Form)
        self.label_18.setObjectName(u"手套神秘")

        self.gridLayout_5.addWidget(self.label_18, 3, 0, 1, 1)

        self.lineEdit_12 = intLineEdit(Form, min=1, max=500)
        self.lineEdit_12.setObjectName(u"手套等级")

        self.gridLayout_5.addWidget(self.lineEdit_12, 1, 1, 1, 3)

        self.comboBox_10 = gloveChooseComboBox(Form)
        self.comboBox_10.setObjectName(u"手套类型")

        self.gridLayout_5.addWidget(self.comboBox_10, 0, 1, 1, 2)

        self.comboBox_11 = hasOrNotComboBox(Form)
        self.comboBox_11.setObjectName(u"手套神秘")

        self.gridLayout_5.addWidget(self.comboBox_11, 3, 1, 1, 2)

        self.label_19 = QLabel(Form)
        self.label_19.setObjectName(u"手套属性")

        self.gridLayout_5.addWidget(self.label_19, 2, 0, 1, 1)

        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"手套等级")

        self.gridLayout_5.addWidget(self.label_20, 1, 0, 1, 1)

        self.gridLayout_9.addLayout(self.gridLayout_5, 2, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"技能组")
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"技能位")

        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)

        self.comboBox_2 = skillSlotNum(Form)
        self.comboBox_2.setObjectName(u"技能位")

        self.gridLayout_2.addWidget(self.comboBox_2, 0, 1, 1, 1)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"技能")

        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)

        self.comboBox_3 = skillComboBox(Form)
        self.comboBox_3.setObjectName(u"技能1")

        self.gridLayout_2.addWidget(self.comboBox_3, 1, 1, 1, 1)

        self.comboBox_4 = skillComboBox(Form)
        self.comboBox_4.setObjectName(u"技能2")

        self.gridLayout_2.addWidget(self.comboBox_4, 2, 1, 1, 1)

        self.comboBox_5 = skillComboBox(Form)
        self.comboBox_5.setObjectName(u"技能3")

        self.gridLayout_2.addWidget(self.comboBox_5, 3, 1, 1, 1)

        self.comboBox_6 = skillComboBox(Form)
        self.comboBox_6.setObjectName(u"技能4")

        self.gridLayout_2.addWidget(self.comboBox_6, 4, 1, 1, 1)

        self.gridLayout_9.addLayout(self.gridLayout_2, 3, 0, 2, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"护甲")
        self.lineEdit_13 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_13.setObjectName(u"护甲属性1")

        self.gridLayout_6.addWidget(self.lineEdit_13, 2, 1, 1, 1)

        self.label_21 = QLabel(Form)
        self.label_21.setObjectName(u"护甲类型")

        self.gridLayout_6.addWidget(self.label_21, 0, 0, 1, 1)

        self.lineEdit_14 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_14.setObjectName(u"护甲属性2")

        self.gridLayout_6.addWidget(self.lineEdit_14, 2, 2, 1, 1)

        self.lineEdit_15 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_15.setObjectName(u"护甲属性4")

        self.gridLayout_6.addWidget(self.lineEdit_15, 2, 4, 1, 1)

        self.lineEdit_16 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_16.setObjectName(u"护甲属性3")

        self.gridLayout_6.addWidget(self.lineEdit_16, 2, 3, 1, 1)

        self.label_22 = QLabel(Form)
        self.label_22.setObjectName(u"护甲神秘")

        self.gridLayout_6.addWidget(self.label_22, 3, 0, 1, 1)

        self.lineEdit_17 = intLineEdit(Form, min=1, max=500)
        self.lineEdit_17.setObjectName(u"护甲等级")

        self.gridLayout_6.addWidget(self.lineEdit_17, 1, 1, 1, 3)

        self.comboBox_12 = ArmorChooseComboBox(Form)
        self.comboBox_12.setObjectName(u"护甲类型")

        self.gridLayout_6.addWidget(self.comboBox_12, 0, 1, 1, 2)

        self.comboBox_13 = hasOrNotComboBox(Form)
        self.comboBox_13.setObjectName(u"护甲神秘")

        self.gridLayout_6.addWidget(self.comboBox_13, 3, 1, 1, 2)

        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"护甲属性百分比")

        self.gridLayout_6.addWidget(self.label_23, 2, 0, 1, 1)

        self.label_24 = QLabel(Form)
        self.label_24.setObjectName(u"护甲等级")

        self.gridLayout_6.addWidget(self.label_24, 1, 0, 1, 1)

        self.gridLayout_9.addLayout(self.gridLayout_6, 3, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"头盔")
        self.lineEdit_18 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_18.setObjectName(u"头盔属性1")

        self.gridLayout_7.addWidget(self.lineEdit_18, 2, 1, 1, 1)

        self.label_25 = QLabel(Form)
        self.label_25.setObjectName(u"头盔类型")

        self.gridLayout_7.addWidget(self.label_25, 0, 0, 1, 1)

        self.lineEdit_19 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_19.setObjectName(u"头盔属性2")

        self.gridLayout_7.addWidget(self.lineEdit_19, 2, 2, 1, 1)

        self.lineEdit_20 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_20.setObjectName(u"头盔属性4")

        self.gridLayout_7.addWidget(self.lineEdit_20, 2, 4, 1, 1)

        self.lineEdit_21 = intLineEdit(Form, min=50, max=150)
        self.lineEdit_21.setObjectName(u"头盔属性3")

        self.gridLayout_7.addWidget(self.lineEdit_21, 2, 3, 1, 1)

        self.label_26 = QLabel(Form)
        self.label_26.setObjectName(u"头盔神秘")

        self.gridLayout_7.addWidget(self.label_26, 3, 0, 1, 1)

        self.lineEdit_22 = intLineEdit(Form, min=1, max=500)
        self.lineEdit_22.setObjectName(u"头盔等级")

        self.gridLayout_7.addWidget(self.lineEdit_22, 1, 1, 1, 3)

        self.comboBox_14 = helmetChooseComboBox(Form)
        self.comboBox_14.setObjectName(u"头盔类型")

        self.gridLayout_7.addWidget(self.comboBox_14, 0, 1, 1, 2)

        self.comboBox_15 = hasOrNotComboBox(Form)
        self.comboBox_15.setObjectName(u"头盔神秘")

        self.gridLayout_7.addWidget(self.comboBox_15, 3, 1, 1, 2)

        self.label_27 = QLabel(Form)
        self.label_27.setObjectName(u"头盔属性百分比")

        self.gridLayout_7.addWidget(self.label_27, 2, 0, 1, 1)

        self.label_28 = QLabel(Form)
        self.label_28.setObjectName(u"头盔等级")

        self.gridLayout_7.addWidget(self.label_28, 1, 0, 1, 1)

        self.gridLayout_9.addLayout(self.gridLayout_7, 4, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"按钮")

        self.pushButton = QPushButton(Form)
        self.pushButton.clicked.connect(self.saveMyCard)
        self.pushButton.setObjectName(u"保存卡片")
        self.gridLayout_8.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.clicked.connect(self.editMyCard)
        self.pushButton_2.setObjectName(u"修改卡片")
        self.gridLayout_8.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.clicked.connect(self.delMyCard)
        self.pushButton_3.setObjectName(u"删除卡片")
        self.gridLayout_8.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.clicked.connect(self.text_equipSet)
        self.pushButton_4.setObjectName(u"快捷写入装备")
        self.gridLayout_8.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.clicked.connect(self.percentage_attr)
        self.pushButton_5.setObjectName(u"比例分配属性")
        self.gridLayout_8.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.gridLayout_9.addLayout(self.gridLayout_8, 5, 0, 1, 2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle("我的卡片")
        self.label.setText("卡片列表")
        self.label_2.setText("光环百分比")
        self.label_3.setText("卡片类型")

        self.label_4.setText("卡片等级")
        self.remainder_point_text.setText("可用点数")
        self.label_5.setText("力量")
        self.label_6.setText("敏捷")
        self.label_7.setText("智力")
        self.label_8.setText("体魄")
        self.label_9.setText("精神")
        self.label_10.setText("意志")
        self.label_13.setText("武器类型")
        self.label_14.setText("等级")

        self.label_15.setText("属性百分比")
        self.label_16.setText("神秘")
        self.label_17.setText("手套类型")
        self.label_18.setText("神秘")

        self.label_19.setText("属性百分比")
        self.label_20.setText("等级")
        self.label_11.setText("技能位")
        self.label_12.setText("技能")

        self.label_21.setText("护甲类型")
        self.label_22.setText("神秘")

        self.label_23.setText("属性百分比")
        self.label_24.setText("等级")
        self.label_25.setText("头盔类型")
        self.label_26.setText("神秘")

        self.label_27.setText("属性百分比")
        self.label_28.setText("等级")
        self.pushButton.setText("存储卡片")
        self.pushButton_2.setText("覆盖当前卡片")
        self.pushButton_3.setText("删除当前卡片")
        self.pushButton_4.setText("装备导入")
        self.pushButton_5.setText("百分比分配属性")

    # retranslateUi

    def open(self):
        global_env.mainWin.hide()
        self.show()

    def closeEvent(self, event):
        global_env.mainWin.show()
        event.accept()

    def makeMyCard(self):
        halo = self.lineEdit.text()
        character = self.comboBox_7.currentIndex()
        level = self.lineEdit_2.text()
        attrSTR = self.spinBox.getValue()
        attrAGI = self.spinBox_2.getValue()
        attrINT = self.spinBox_3.getValue()
        attrVIT = self.spinBox_4.getValue()
        attrSPR = self.spinBox_5.getValue()
        attrRES = self.spinBox_6.getValue()
        attrSet = cardAttr(attrSTR, attrAGI, attrINT, attrVIT, attrSPR, attrRES)

        sklSlot = self.comboBox_2.currentIndex()

        skill_1 = skill(self.comboBox_3.currentIndex())
        skill_2 = skill(self.comboBox_4.currentIndex())
        skill_3 = skill(self.comboBox_5.currentIndex())
        skill_4 = skill(self.comboBox_6.currentIndex())
        skillSet = SKILLSet(skill_1, skill_2, skill_3, skill_4)

        weaponType = self.comboBox_8.currentIndex()
        weaponLevel = self.lineEdit_3.text()
        weaponAttr1 = self.lineEdit_4.text()
        weaponAttr2 = self.lineEdit_5.text()
        weaponAttr3 = self.lineEdit_6.text()
        weaponAttr4 = self.lineEdit_7.text()
        weaponHasMystical = self.comboBox_9.currentIndex()
        weapon = weaponEquip(weaponLevel, weaponAttr1, weaponAttr2, weaponAttr3, weaponAttr4, weaponHasMystical,
                             weaponType)

        gloveType = self.comboBox_10.currentIndex()
        gloveLevel = self.lineEdit_12.text()
        gloveAttr1 = self.lineEdit_8.text()
        gloveAttr2 = self.lineEdit_9.text()
        gloveAttr3 = self.lineEdit_11.text()
        gloveAttr4 = self.lineEdit_10.text()
        gloveHasMystical = self.comboBox_11.currentIndex()
        glove = gloveEquip(gloveLevel, gloveAttr1, gloveAttr2, gloveAttr3, gloveAttr4, gloveHasMystical,
                           gloveType)

        ArmorType = self.comboBox_12.currentIndex()
        ArmorLevel = self.lineEdit_17.text()
        ArmorAttr1 = self.lineEdit_13.text()
        ArmorAttr2 = self.lineEdit_14.text()
        ArmorAttr3 = self.lineEdit_16.text()
        ArmorAttr4 = self.lineEdit_15.text()
        ArmorHasMystical = self.comboBox_13.currentIndex()
        Armor = ArmorEquip(ArmorLevel, ArmorAttr1, ArmorAttr2, ArmorAttr3, ArmorAttr4, ArmorHasMystical,
                           ArmorType)

        helmetType = self.comboBox_14.currentIndex()
        helmetLevel = self.lineEdit_22.text()
        helmetAttr1 = self.lineEdit_18.text()
        helmetAttr2 = self.lineEdit_19.text()
        helmetAttr3 = self.lineEdit_21.text()
        helmetAttr4 = self.lineEdit_20.text()
        helmetHasMystical = self.comboBox_15.currentIndex()
        helmet = helmetEquip(helmetLevel, helmetAttr1, helmetAttr2, helmetAttr3, helmetAttr4, helmetHasMystical,
                             helmetType)

        equipSet = EQUIPSet(weapon, glove, Armor, helmet)

        card = self.cardClass(halo, character, level, attrSet, sklSlot, skillSet, equipSet)

        return card

    def setMyCard(self, card):
        halo = card.halo
        character = card.character
        level = card.level
        attrSet = card.attrSet
        sklSlot = card.sklSlot
        skillSet = card.skillSet
        equipSet = card.equipSet

        attrSTR = attrSet.STR
        attrAGI = attrSet.AGI
        attrINT = attrSet.INT
        attrVIT = attrSet.VIT
        attrSPR = attrSet.SPR
        attrRES = attrSet.RES

        skill_1 = skillSet.skill_1
        skill_2 = skillSet.skill_2
        skill_3 = skillSet.skill_3
        skill_4 = skillSet.skill_4

        weapon = equipSet.weapon
        glove = equipSet.glove
        Armor = equipSet.Armor
        helmet = equipSet.helmet

        self.lineEdit.setText(halo)
        self.comboBox_7.setCurrentIndex(character)
        self.lineEdit_2.setText(level)
        self.spinBox.setValue(attrSTR)
        self.spinBox_2.setValue(attrAGI)
        self.spinBox_3.setValue(attrINT)
        self.spinBox_4.setValue(attrVIT)
        self.spinBox_5.setValue(attrSPR)
        self.spinBox_6.setValue(attrRES)

        self.comboBox_2.setCurrentIndex(sklSlot)

        self.comboBox_3.setCurrentIndex(skill_1.data)
        self.comboBox_4.setCurrentIndex(skill_2.data)
        self.comboBox_5.setCurrentIndex(skill_3.data)
        self.comboBox_6.setCurrentIndex(skill_4.data)

        self.comboBox_8.setCurrentIndex(weapon.equipType)
        self.lineEdit_3.setText(weapon.level)
        self.lineEdit_4.setText(weapon.attr0)
        self.lineEdit_5.setText(weapon.attr1)
        self.lineEdit_6.setText(weapon.attr2)
        self.lineEdit_7.setText(weapon.attr3)
        self.comboBox_9.setCurrentIndex(weapon.hasMystical)

        self.comboBox_10.setCurrentIndex(glove.equipType)
        self.lineEdit_12.setText(glove.level)
        self.lineEdit_8.setText(glove.attr0)
        self.lineEdit_9.setText(glove.attr1)
        self.lineEdit_11.setText(glove.attr2)
        self.lineEdit_10.setText(glove.attr3)
        self.comboBox_11.setCurrentIndex(glove.hasMystical)

        self.comboBox_12.setCurrentIndex(Armor.equipType)
        self.lineEdit_17.setText(Armor.level)
        self.lineEdit_13.setText(Armor.attr0)
        self.lineEdit_14.setText(Armor.attr1)
        self.lineEdit_16.setText(Armor.attr2)
        self.lineEdit_15.setText(Armor.attr3)
        self.comboBox_13.setCurrentIndex(Armor.hasMystical)

        self.comboBox_14.setCurrentIndex(helmet.equipType)
        self.lineEdit_22.setText(helmet.level)
        self.lineEdit_18.setText(helmet.attr0)
        self.lineEdit_19.setText(helmet.attr1)
        self.lineEdit_21.setText(helmet.attr2)
        self.lineEdit_20.setText(helmet.attr3)
        self.comboBox_15.setCurrentIndex(helmet.hasMystical)

    def newMyCard(self):
        halo = "0"
        character = 0
        level = "0"
        attrSet = cardAttr(0, 0, 0, 0, 0, 0)
        sklSlot = 4
        # skillSet = card.skillSet
        # equipSet = card.equipSet

        attrSTR = attrSet.STR
        attrAGI = attrSet.AGI
        attrINT = attrSet.INT
        attrVIT = attrSet.VIT
        attrSPR = attrSet.SPR
        attrRES = attrSet.RES

        skill_1 = 0
        skill_2 = 0
        skill_3 = 0
        skill_4 = 0

        weapon = weaponEquip("0", "0", "0", "0", "0", 0, 0)
        glove = gloveEquip("0", "0", "0", "0", "0", 0, 0)
        Armor = ArmorEquip("0", "0", "0", "0", "0", 0, 0)
        helmet = helmetEquip("0", "0", "0", "0", "0", 0, 0)

        self.lineEdit.setText(halo)
        self.comboBox_7.setCurrentIndex(character)
        self.lineEdit_2.setText(level)
        self.spinBox.setValue(attrSTR)
        self.spinBox_2.setValue(attrAGI)
        self.spinBox_3.setValue(attrINT)
        self.spinBox_4.setValue(attrVIT)
        self.spinBox_5.setValue(attrSPR)
        self.spinBox_6.setValue(attrRES)

        self.comboBox_2.setCurrentIndex(sklSlot)

        self.comboBox_3.setCurrentIndex(skill_1)
        self.comboBox_4.setCurrentIndex(skill_2)
        self.comboBox_5.setCurrentIndex(skill_3)
        self.comboBox_6.setCurrentIndex(skill_4)

        self.comboBox_8.setCurrentIndex(weapon.equipType)
        self.lineEdit_3.setText(weapon.level)
        self.lineEdit_4.setText(weapon.attr0)
        self.lineEdit_5.setText(weapon.attr1)
        self.lineEdit_6.setText(weapon.attr2)
        self.lineEdit_7.setText(weapon.attr3)
        self.comboBox_9.setCurrentIndex(weapon.hasMystical)

        self.comboBox_10.setCurrentIndex(glove.equipType)
        self.lineEdit_12.setText(glove.level)
        self.lineEdit_8.setText(glove.attr0)
        self.lineEdit_9.setText(glove.attr1)
        self.lineEdit_11.setText(glove.attr2)
        self.lineEdit_10.setText(glove.attr3)
        self.comboBox_11.setCurrentIndex(glove.hasMystical)

        self.comboBox_12.setCurrentIndex(Armor.equipType)
        self.lineEdit_17.setText(Armor.level)
        self.lineEdit_13.setText(Armor.attr0)
        self.lineEdit_14.setText(Armor.attr1)
        self.lineEdit_16.setText(Armor.attr2)
        self.lineEdit_15.setText(Armor.attr3)
        self.comboBox_13.setCurrentIndex(Armor.hasMystical)

        self.comboBox_14.setCurrentIndex(helmet.equipType)
        self.lineEdit_22.setText(helmet.level)
        self.lineEdit_18.setText(helmet.attr0)
        self.lineEdit_19.setText(helmet.attr1)
        self.lineEdit_21.setText(helmet.attr2)
        self.lineEdit_20.setText(helmet.attr3)
        self.comboBox_15.setCurrentIndex(helmet.hasMystical)

    def myCardListUpdate(self):
        myCardList = self.cardList
        currentIndex = self.comboBox.currentIndex()
        self.comboBox.clear()
        for k, v in myCardList.items():
            self.comboBox.addItem(k)
        self.comboBox.setCurrentIndex(currentIndex)

    def saveMyCard(self):
        (result, message) = self.ableCheck()
        if not result:
            QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
            return
        newCard = self.makeMyCard()
        text, ok = QInputDialog.getText(self, '设置卡片显示名', '输入名称：', text=newCard.tostring())
        if ok and text:
            if text in self.cardList.keys():
                QMessageBox.critical(self, "错误", "保存失败，与已有配置重名", QMessageBox.Yes)
                return
            self.cardList[text] = newCard
            self.comboBox.setCurrentText(text)

    def editMyCard(self):
        (result, message) = self.ableCheck()
        if not result:
            QMessageBox.critical(self, "错误", message, QMessageBox.Yes)
            return
        newCard = self.makeMyCard()
        # index = self.comboBox.currentIndex()
        text = self.comboBox.currentText()
        if text == "":
            QMessageBox.critical(self, "错误", "修改失败，空名称", QMessageBox.Yes)
            return
        if text == "新卡片":
            QMessageBox.critical(self, "错误", "模板不可修改", QMessageBox.Yes)
            return
        yes = QMessageBox.question(self, "提问对话框", "确认修改？", QMessageBox.Yes | QMessageBox.No)
        if yes:
            self.cardList[text] = newCard

    def delMyCard(self):
        # index = self.comboBox.currentIndex()
        text = self.comboBox.currentText()
        if text == "新卡片":
            QMessageBox.critical(self, "错误", "模板不可删除", QMessageBox.Yes)
            return
        yes = QMessageBox.question(self, "提问对话框", "确认删除？", QMessageBox.Yes | QMessageBox.No)
        if yes:
            del (self.cardList[text])

    def chooseMyCard(self, tag):  # combobox点击事件
        if tag not in self.cardList.keys():
            return
        card = self.cardList[tag]
        if card is None:
            self.newMyCard()
        else:
            try:
                self.setMyCard(card)
            except:
                QMessageBox.critical(self, "错误", "该配置出错不可用", QMessageBox.Yes)
        self.set_remainder_point()

    def ableCheck(self):
        # self.lineEdit_2.setObjectName(u"卡片等级")
        # self.spinBox.setObjectName(u"力量")
        # self.spinBox_2.setObjectName(u"敏捷")
        # self.spinBox_3.setObjectName(u"智力")
        # self.spinBox_4.setObjectName(u"体魄")
        # self.spinBox_5.setObjectName(u"精神")
        # self.spinBox_6.setObjectName(u"意志")
        if global_env.test_mode:
            return True, "测试模式"

        level = self.lineEdit_2.getValue()
        STR = self.spinBox.getValue()
        AGI = self.spinBox_2.getValue()
        INT = self.spinBox_3.getValue()
        VIT = self.spinBox_4.getValue()
        SPR = self.spinBox_5.getValue()
        RES = self.spinBox_6.getValue()

        if level > 500:
            return False, "卡片不能超过500级"
        maxPoint = level * 3 + 6
        if maxPoint < STR + AGI + INT + VIT + SPR + RES:
            return False, "属性点分配超过等级上限！"

        # self.comboBox_2.setObjectName(u"技能位")
        # self.comboBox_3.setObjectName(u"技能1")
        # self.comboBox_4.setObjectName(u"技能2")
        # self.comboBox_5.setObjectName(u"技能3")
        # self.comboBox_6.setObjectName(u"技能4")
        halo = self.lineEdit.getValue()
        if halo > 200:
            return False, "光环不能大于200!"
        sklSlotNum = self.comboBox_2.currentIndex() + 1
        sklList = []
        skl_1 = self.comboBox_3.currentIndex()
        skl_2 = self.comboBox_4.currentIndex()
        skl_3 = self.comboBox_5.currentIndex()
        skl_4 = self.comboBox_6.currentIndex()
        if skl_1 != 0:
            sklList.append(skl_1)
        if skl_2 != 0:
            if skl_2 in sklList:
                return False, "技能重复！"
            sklList.append(skl_2)
        if skl_3 != 0:
            if skl_3 in sklList:
                return False, "技能重复！"
            sklList.append(skl_3)
        if skl_4 != 0:
            if skl_4 in sklList:
                return False, "技能重复！"
            sklList.append(skl_4)
        if len(sklList) > sklSlotNum:
            return False, "技能数量大于技能位!"
        used_halo = 0
        for skl in sklList:
            if skl <= 3:
                used_halo += 10
            elif skl <= 5:
                used_halo += 30
            elif skl <= 8:
                used_halo += 50
            elif skl <= 11:
                used_halo += 100
        if used_halo > halo:
            return False, "技能所需点数超过光环！"
        # self.comboBox_8.setObjectName(u"武器类型")
        # self.lineEdit_3.setObjectName(u"武器等级")
        # self.lineEdit_4.setObjectName(u"武器属性1")
        # self.lineEdit_5.setObjectName(u"武器属性2")
        # self.lineEdit_6.setObjectName(u"武器属性3")
        # self.lineEdit_7.setObjectName(u"武器属性4")
        if self.comboBox_8.currentIndex() != 0:
            if self.lineEdit_3.getValue() > 500:
                return False, "装备等级不能大于500!"
            if self.lineEdit_4.getValue() < 50 or self.lineEdit_5.getValue() < 50 or self.lineEdit_6.getValue() < 50 or self.lineEdit_7.getValue() < 50:
                return False, "装备属性不能小于50!"
            if self.lineEdit_4.getValue() > 150 or self.lineEdit_5.getValue() > 150 or self.lineEdit_6.getValue() > 150 or self.lineEdit_7.getValue() > 150:
                return False, "装备属性不能大于150!"

        # self.comboBox_10.setObjectName(u"手套类型")
        # self.lineEdit_12.setObjectName(u"手套等级")
        # self.lineEdit_8.setObjectName(u"手套属性1")
        # self.lineEdit_9.setObjectName(u"手套属性2")
        # self.lineEdit_11.setObjectName(u"手套属性3")
        # self.lineEdit_10.setObjectName(u"手套属性4")
        if self.comboBox_10.currentIndex() != 0:
            if self.lineEdit_12.getValue() > 500:
                return False, "装备等级不能大于500!"
            if self.lineEdit_8.getValue() < 50 or self.lineEdit_9.getValue() < 50 or self.lineEdit_11.getValue() < 50 or self.lineEdit_10.getValue() < 50:
                return False, "装备属性不能小于50!"
            if self.lineEdit_8.getValue() > 150 or self.lineEdit_9.getValue() > 150 or self.lineEdit_11.getValue() > 150 or self.lineEdit_10.getValue() > 150:
                return False, "装备属性不能大于150!"

        # self.comboBox_12.setObjectName(u"护甲类型")
        # self.lineEdit_17.setObjectName(u"护甲等级")
        # self.lineEdit_13.setObjectName(u"护甲属性1")
        # self.lineEdit_14.setObjectName(u"护甲属性2")
        # self.lineEdit_16.setObjectName(u"护甲属性3")
        # self.lineEdit_15.setObjectName(u"护甲属性4")
        if self.comboBox_12.currentIndex() != 0:
            if self.lineEdit_17.getValue() > 500:
                return False, "装备等级不能大于500!"
            if self.lineEdit_13.getValue() < 50 or self.lineEdit_14.getValue() < 50 or self.lineEdit_16.getValue() < 50 or self.lineEdit_15.getValue() < 50:
                return False, "装备属性不能小于50!"
            if self.lineEdit_13.getValue() > 150 or self.lineEdit_14.getValue() > 150 or self.lineEdit_16.getValue() > 150 or self.lineEdit_15.getValue() > 150:
                return False, "装备属性不能大于150!"

        # self.comboBox_14.setObjectName(u"头盔类型")
        # self.lineEdit_22.setObjectName(u"头盔等级")
        # self.lineEdit_18.setObjectName(u"头盔属性1")
        # self.lineEdit_19.setObjectName(u"头盔属性2")
        # self.lineEdit_21.setObjectName(u"头盔属性3")
        # self.lineEdit_20.setObjectName(u"头盔属性4")
        if self.comboBox_14.currentIndex() != 0:
            if self.lineEdit_22.getValue() > 500:
                return False, "装备等级不能大于500!"
            if self.lineEdit_18.getValue() < 50 or self.lineEdit_19.getValue() < 50 or self.lineEdit_21.getValue() < 50 or self.lineEdit_20.getValue() < 50:
                return False, "装备属性不能小于50!"
            if self.lineEdit_18.getValue() > 150 or self.lineEdit_19.getValue() > 150 or self.lineEdit_21.getValue() > 150 or self.lineEdit_20.getValue() > 150:
                return False, "装备属性不能大于150!"

        return True, "无错误"

    def text_equipSet(self):
        text, ok = QInputDialog.getMultiLineText(self, '快捷复制导入套装', '必须以武器为首行：')
        if not (ok and text):
            return
        mySet = text_to_equipSet(text)
        self.comboBox_8.setCurrentIndex(mySet.weapon.equipType)
        self.lineEdit_3.setText(mySet.weapon.level)
        self.lineEdit_4.setText(mySet.weapon.attr0)
        self.lineEdit_5.setText(mySet.weapon.attr1)
        self.lineEdit_6.setText(mySet.weapon.attr2)
        self.lineEdit_7.setText(mySet.weapon.attr3)
        self.comboBox_9.setCurrentIndex(mySet.weapon.hasMystical)

        self.comboBox_10.setCurrentIndex(mySet.glove.equipType)
        self.lineEdit_12.setText(mySet.glove.level)
        self.lineEdit_8.setText(mySet.glove.attr0)
        self.lineEdit_9.setText(mySet.glove.attr1)
        self.lineEdit_11.setText(mySet.glove.attr2)
        self.lineEdit_10.setText(mySet.glove.attr3)
        self.comboBox_11.setCurrentIndex(mySet.glove.hasMystical)

        self.comboBox_12.setCurrentIndex(mySet.Armor.equipType)
        self.lineEdit_17.setText(mySet.Armor.level)
        self.lineEdit_13.setText(mySet.Armor.attr0)
        self.lineEdit_14.setText(mySet.Armor.attr1)
        self.lineEdit_16.setText(mySet.Armor.attr2)
        self.lineEdit_15.setText(mySet.Armor.attr3)
        self.comboBox_13.setCurrentIndex(mySet.Armor.hasMystical)

        self.comboBox_14.setCurrentIndex(mySet.helmet.equipType)
        self.lineEdit_22.setText(mySet.helmet.level)
        self.lineEdit_18.setText(mySet.helmet.attr0)
        self.lineEdit_19.setText(mySet.helmet.attr1)
        self.lineEdit_21.setText(mySet.helmet.attr2)
        self.lineEdit_20.setText(mySet.helmet.attr3)
        self.comboBox_15.setCurrentIndex(mySet.helmet.hasMystical)

    def set_remainder_point(self):
        level = self.lineEdit_2.getValue()
        STR = self.spinBox.getValue()
        AGI = self.spinBox_2.getValue()
        INT = self.spinBox_3.getValue()
        VIT = self.spinBox_4.getValue()
        SPR = self.spinBox_5.getValue()
        RES = self.spinBox_6.getValue()

        maxPoint = level * 3 + 6
        remainder_point = maxPoint - (STR + AGI + INT + VIT + SPR + RES)
        self.remainder_point.setText(str(remainder_point))

    def percentage_attr(self):
        text, ok = QInputDialog.getText(self, '分配属性', '输入6个整数，空格分割')
        if ok and text:
            percentage_text = text.split()
            attr_list = []
            level = self.lineEdit_2.getValue()
            point = level * 3
            for i in range(6):
                attr_list.append(int(point * int(percentage_text[i]) / 100 + 1))
            self.spinBox.setValue(attr_list[0])
            self.spinBox_2.setValue(attr_list[1])
            self.spinBox_3.setValue(attr_list[2])
            self.spinBox_4.setValue(attr_list[3])
            self.spinBox_5.setValue(attr_list[4])
            self.spinBox_6.setValue(attr_list[5])
            self.set_remainder_point()