import re

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, SIGNAL, Slot)
from PySide2.QtGui import QCursor
from PySide2.QtWidgets import *

import global_env
from Qclass import skillComboBox, skillSlotNum, cardCharacterComboBox, weaponChooseComboBox, gloveChooseComboBox, \
    ArmorChooseComboBox, helmetChooseComboBox, hasOrNotComboBox, intLineEdit, bigSpinBox, myComboBox, STATCardPanel, \
    cardSkillPanel
from SystemClass import cardAttr, skill, SKILLSet, weaponEquip, ArmorEquip, gloveEquip, helmetEquip, EQUIPSet, \
    all_character, all_skill, all_equip
from action_def import text_to_equipSet, whatCardClass
from cardClass import myCard
from equipChooseWindow import equipChooseWindow

QString = type("")


class Ui_cardForm(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        self.Form = Form
        Form.resize(575, 602)

        self.gridLayout_9 = QGridLayout(Form)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cardlistlabel = QLabel(Form)
        self.cardlistlabel.setObjectName(u"mycardlist")
        self.toggleSTATButton = QPushButton(Form)
        self.toggleSTATButton.clicked.connect(lambda: self.toggleSTAT())
        self.toggleSTATButton.hide()

        self.gridLayout_3.addWidget(self.cardlistlabel, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.toggleSTATButton, 0, 1, 1, 1)

        self.cardlistcomboBox = myComboBox(Form)
        self.myCardListUpdate()
        self.cardlistcomboBox.currentIndexChanged.connect(
            lambda: self.chooseMyCard(self.cardlistcomboBox.currentText()))
        self.cardlistcomboBox.setObjectName(u"mycardlist")

        self.gridLayout_3.addWidget(self.cardlistcomboBox, 0, 2, 1, 3)

        self.gridLayout_9.addLayout(self.gridLayout_3, 0, 0, 1, 2)
        self.stack = QStackedWidget(self)
        self.stack1 = QWidget()
        self.gridLayout_stack1 = QGridLayout(self.stack1)
        self.gridLayout_stack1.setObjectName(u"gridLayout_stack1")
        self.stack2 = QWidget()
        self.gridLayout_stack2 = QGridLayout(self.stack2)
        self.gridLayout_stack2.setObjectName(u"gridLayout_stack2")
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.gridLayout_9.addWidget(self.stack, 1, 0, 1, 2)

        self.stack1.setContextMenuPolicy(Qt.CustomContextMenu)
        self.stack1.customContextMenuRequested.connect(self.rightMenuShow)

        self.gridLayout = QGridLayout(self.stack1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.halolabel = QLabel(Form)
        self.halolabel.setObjectName(u"光环")

        self.gridLayout.addWidget(self.halolabel, 0, 0, 1, 1)

        self.halolineEdit = intLineEdit(parent=Form, max=200)  # 光环
        self.halolineEdit.setObjectName(u"光环")

        self.gridLayout.addWidget(self.halolineEdit, 0, 1, 1, 1)

        self.cardtypelabel = QLabel(Form)
        self.cardtypelabel.setObjectName(u"卡片类型")

        self.gridLayout.addWidget(self.cardtypelabel, 1, 0, 1, 1)

        self.cardtypecomboBox = cardCharacterComboBox(Form)
        self.cardtypecomboBox.setObjectName(u"卡片类型")

        self.gridLayout.addWidget(self.cardtypecomboBox, 1, 1, 1, 1)

        self.levellabel = QLabel(Form)
        self.levellabel.setObjectName(u"卡片等级")

        self.gridLayout.addWidget(self.levellabel, 2, 0, 1, 1)

        self.levellineEdit = intLineEdit(parent=Form, max=500)  # 等级
        self.levellineEdit.setObjectName(u"卡片等级")
        self.levellineEdit.textEdited.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.levellineEdit, 2, 1, 1, 1)

        self.remainder_point_text = QLabel(Form)
        self.remainder_point_text.setObjectName(u"点数文本")
        self.gridLayout.addWidget(self.remainder_point_text, 3, 0, 1, 1)
        self.remainder_point = QLabel(Form)
        self.remainder_point.setObjectName(u"点数")
        self.gridLayout.addWidget(self.remainder_point, 3, 1, 1, 1)

        self.STRlabel = QLabel(Form)
        self.STRlabel.setObjectName(u"力量")

        self.gridLayout.addWidget(self.STRlabel, 4, 0, 1, 1)

        self.STRspinBox = bigSpinBox(Form)
        self.STRspinBox.setObjectName(u"力量")
        self.STRspinBox.valueChanged.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.STRspinBox, 4, 1, 1, 1)

        self.AGIlabel = QLabel(Form)
        self.AGIlabel.setObjectName(u"敏捷")

        self.gridLayout.addWidget(self.AGIlabel, 5, 0, 1, 1)

        self.AGIspinBox = bigSpinBox(Form)
        self.AGIspinBox.setObjectName(u"敏捷")
        self.AGIspinBox.valueChanged.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.AGIspinBox, 5, 1, 1, 1)

        self.INTlabel = QLabel(Form)
        self.INTlabel.setObjectName(u"智力")

        self.gridLayout.addWidget(self.INTlabel, 6, 0, 1, 1)

        self.INTspinBox = bigSpinBox(Form)
        self.INTspinBox.setObjectName(u"智力")
        self.INTspinBox.valueChanged.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.INTspinBox, 6, 1, 1, 1)

        self.VITlabel = QLabel(Form)
        self.VITlabel.setObjectName(u"体魄")

        self.gridLayout.addWidget(self.VITlabel, 7, 0, 1, 1)

        self.VITspinBox = bigSpinBox(Form)
        self.VITspinBox.setObjectName(u"体魄")
        self.VITspinBox.valueChanged.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.VITspinBox, 7, 1, 1, 1)

        self.SPRlabel = QLabel(Form)
        self.SPRlabel.setObjectName(u"精神")

        self.gridLayout.addWidget(self.SPRlabel, 8, 0, 1, 1)

        self.SPRspinBox = bigSpinBox(Form)
        self.SPRspinBox.setObjectName(u"精神")
        self.SPRspinBox.valueChanged.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.SPRspinBox, 8, 1, 1, 1)

        self.RESlabel = QLabel(Form)
        self.RESlabel.setObjectName(u"意志")

        self.gridLayout.addWidget(self.RESlabel, 9, 0, 1, 1)

        self.RESspinBox = bigSpinBox(Form)
        self.RESspinBox.setObjectName(u"意志")
        self.RESspinBox.valueChanged.connect(self.set_remainder_point)
        self.gridLayout.addWidget(self.RESspinBox, 9, 1, 1, 1)

        self.gridLayout_stack1.addLayout(self.gridLayout, 1, 0, 2, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.weaponlabel = QLabel(Form)
        self.weaponlabel.setObjectName(u"武器类型")

        self.gridLayout_4.addWidget(self.weaponlabel, 0, 0, 1, 1)

        self.equipStorageButton = QPushButton(Form)
        self.equipStorageButton.setObjectName("装备仓库")
        self.equipStorageButton.clicked.connect(self.openEquipChooseWindow)
        self.gridLayout_4.addWidget(self.equipStorageButton, 0, 3, 1, 1)

        self.weaponToStorage = QPushButton(Form)
        self.weaponToStorage.setObjectName("武器加入仓库")
        self.weaponToStorage.clicked.connect(lambda: self.EquipToStorage("weapon"))
        self.gridLayout_4.addWidget(self.weaponToStorage, 0, 4, 1, 1)

        self.weaponattr2lineEdit = intLineEdit(Form, max=500)
        self.weaponattr2lineEdit.setObjectName(u"武器属性2")

        self.gridLayout_4.addWidget(self.weaponattr2lineEdit, 2, 2, 1, 1)

        self.weaponlevellabel = QLabel(Form)
        self.weaponlevellabel.setObjectName(u"等级")

        self.gridLayout_4.addWidget(self.weaponlevellabel, 1, 0, 1, 1)

        self.weaponattr1lineEdit = intLineEdit(Form, min=50, max=150)
        self.weaponattr1lineEdit.setObjectName(u"武器属性1")

        self.gridLayout_4.addWidget(self.weaponattr1lineEdit, 2, 1, 1, 1)

        self.weaponattr4lineEdit = intLineEdit(Form, min=50, max=150)
        self.weaponattr4lineEdit.setObjectName(u"武器属性4")

        self.gridLayout_4.addWidget(self.weaponattr4lineEdit, 2, 4, 1, 1)

        self.weaponattr3lineEdit = intLineEdit(Form, min=50, max=150)
        self.weaponattr3lineEdit.setObjectName(u"武器属性3")

        self.gridLayout_4.addWidget(self.weaponattr3lineEdit, 2, 3, 1, 1)

        self.weaponlevellineEdit = intLineEdit(Form, min=1, max=500)
        self.weaponlevellineEdit.setObjectName(u"武器等级")

        self.gridLayout_4.addWidget(self.weaponlevellineEdit, 1, 1, 1, 3)

        self.weapontypecomboBox = weaponChooseComboBox(Form)
        self.weapontypecomboBox.setObjectName(u"武器类型")

        self.gridLayout_4.addWidget(self.weapontypecomboBox, 0, 1, 1, 2)

        self.weaponmysticalcomboBox = hasOrNotComboBox(Form)
        self.weaponmysticalcomboBox.setObjectName(u"武器神秘")

        self.gridLayout_4.addWidget(self.weaponmysticalcomboBox, 3, 1, 1, 2)

        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"属性百分比")

        self.gridLayout_4.addWidget(self.label_15, 2, 0, 1, 1)

        self.weaponmysticallabel = QLabel(Form)
        self.weaponmysticallabel.setObjectName(u"武器神秘")

        self.gridLayout_4.addWidget(self.weaponmysticallabel, 3, 0, 1, 1)

        self.gridLayout_stack1.addLayout(self.gridLayout_4, 1, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gloveattr1lineEdit = intLineEdit(Form, min=50, max=150)
        self.gloveattr1lineEdit.setObjectName(u"手套属性1")

        self.gridLayout_5.addWidget(self.gloveattr1lineEdit, 2, 1, 1, 1)

        self.glovetypelabel = QLabel(Form)
        self.glovetypelabel.setObjectName(u"手套类型")

        self.gridLayout_5.addWidget(self.glovetypelabel, 0, 0, 1, 1)

        self.gloveToStorage = QPushButton(Form)
        self.gloveToStorage.setObjectName("手套加入仓库")
        self.gloveToStorage.clicked.connect(lambda: self.EquipToStorage("glove"))
        self.gridLayout_5.addWidget(self.gloveToStorage, 0, 4, 1, 1)

        self.gloveattr2lineEdit = intLineEdit(Form, min=50, max=150)
        self.gloveattr2lineEdit.setObjectName(u"手套属性2")

        self.gridLayout_5.addWidget(self.gloveattr2lineEdit, 2, 2, 1, 1)

        self.gloveattr4lineEdit = intLineEdit(Form, min=50, max=150)
        self.gloveattr4lineEdit.setObjectName(u"手套属性4")

        self.gridLayout_5.addWidget(self.gloveattr4lineEdit, 2, 4, 1, 1)

        self.gloveattr3lineEdit = intLineEdit(Form, min=50, max=150)
        self.gloveattr3lineEdit.setObjectName(u"手套属性3")

        self.gridLayout_5.addWidget(self.gloveattr3lineEdit, 2, 3, 1, 1)

        self.glovemysticallabel = QLabel(Form)
        self.glovemysticallabel.setObjectName(u"手套神秘")

        self.gridLayout_5.addWidget(self.glovemysticallabel, 3, 0, 1, 1)

        self.glovelevellineEdit = intLineEdit(Form, min=1, max=500)
        self.glovelevellineEdit.setObjectName(u"手套等级")

        self.gridLayout_5.addWidget(self.glovelevellineEdit, 1, 1, 1, 3)

        self.glovetypecomboBox = gloveChooseComboBox(Form)
        self.glovetypecomboBox.setObjectName(u"手套类型")

        self.gridLayout_5.addWidget(self.glovetypecomboBox, 0, 1, 1, 2)

        self.glovemysticalcomboBox = hasOrNotComboBox(Form)
        self.glovemysticalcomboBox.setObjectName(u"手套神秘")

        self.gridLayout_5.addWidget(self.glovemysticalcomboBox, 3, 1, 1, 2)

        self.gloveattrlabel = QLabel(Form)
        self.gloveattrlabel.setObjectName(u"手套属性")

        self.gridLayout_5.addWidget(self.gloveattrlabel, 2, 0, 1, 1)

        self.glovelevellabel = QLabel(Form)
        self.glovelevellabel.setObjectName(u"手套等级")

        self.gridLayout_5.addWidget(self.glovelevellabel, 1, 0, 1, 1)

        self.gridLayout_stack1.addLayout(self.gridLayout_5, 2, 1, 1, 1)

        # self.gridLayout_2 = QGridLayout()
        # self.gridLayout_2.setObjectName(u"技能组")
        # self.skillslotlabel = QLabel(Form)
        # self.skillslotlabel.setObjectName(u"技能位")
        #
        # self.gridLayout_2.addWidget(self.skillslotlabel, 0, 0, 1, 1)
        #
        # self.skillslotcomboBox = skillSlotNum(Form)
        # self.skillslotcomboBox.setObjectName(u"技能位")
        #
        # self.gridLayout_2.addWidget(self.skillslotcomboBox, 0, 1, 1, 1)
        #
        # self.skilllabel = QLabel(Form)
        # self.skilllabel.setObjectName(u"技能")
        #
        # self.gridLayout_2.addWidget(self.skilllabel, 1, 0, 1, 1)
        #
        # self.skill1comboBox = skillComboBox(Form)
        # self.skill1comboBox.setObjectName(u"技能1")
        #
        # self.gridLayout_2.addWidget(self.skill1comboBox, 1, 1, 1, 1)
        #
        # self.skill2comboBox = skillComboBox(Form)
        # self.skill2comboBox.setObjectName(u"技能2")
        #
        # self.gridLayout_2.addWidget(self.skill2comboBox, 2, 1, 1, 1)
        #
        # self.skill3comboBox = skillComboBox(Form)
        # self.skill3comboBox.setObjectName(u"技能3")
        #
        # self.gridLayout_2.addWidget(self.skill3comboBox, 3, 1, 1, 1)
        #
        # self.skill4comboBox = skillComboBox(Form)
        # self.skill4comboBox.setObjectName(u"技能4")
        #
        # self.gridLayout_2.addWidget(self.skill4comboBox, 4, 1, 1, 1)
        #
        # self.gridLayout_stack1.addLayout(self.gridLayout_2, 3, 0, 2, 1)
        self.cardSkillPanel = cardSkillPanel(Form);
        self.gridLayout_stack1.addWidget(self.cardSkillPanel, 3, 0, 2, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"护甲")
        self.armorattr1lineEdit = intLineEdit(Form, min=50, max=150)
        self.armorattr1lineEdit.setObjectName(u"护甲属性1")

        self.gridLayout_6.addWidget(self.armorattr1lineEdit, 2, 1, 1, 1)

        self.armortypelabel = QLabel(Form)
        self.armortypelabel.setObjectName(u"护甲类型")

        self.gridLayout_6.addWidget(self.armortypelabel, 0, 0, 1, 1)

        self.ArmorToStorage = QPushButton(Form)
        self.ArmorToStorage.setObjectName("护甲加入仓库")
        self.ArmorToStorage.clicked.connect(lambda: self.EquipToStorage("Armor"))
        self.gridLayout_6.addWidget(self.ArmorToStorage, 0, 4, 1, 1)

        self.armorattr2lineEdit = intLineEdit(Form, min=50, max=150)
        self.armorattr2lineEdit.setObjectName(u"护甲属性2")

        self.gridLayout_6.addWidget(self.armorattr2lineEdit, 2, 2, 1, 1)

        self.armorattr4lineEdit = intLineEdit(Form, min=50, max=150)
        self.armorattr4lineEdit.setObjectName(u"护甲属性4")

        self.gridLayout_6.addWidget(self.armorattr4lineEdit, 2, 4, 1, 1)

        self.armorattr3lineEdit = intLineEdit(Form, min=50, max=150)
        self.armorattr3lineEdit.setObjectName(u"护甲属性3")

        self.gridLayout_6.addWidget(self.armorattr3lineEdit, 2, 3, 1, 1)

        self.armormysticallabel = QLabel(Form)
        self.armormysticallabel.setObjectName(u"护甲神秘")

        self.gridLayout_6.addWidget(self.armormysticallabel, 3, 0, 1, 1)

        self.armorlevellineEdit = intLineEdit(Form, min=1, max=500)
        self.armorlevellineEdit.setObjectName(u"护甲等级")

        self.gridLayout_6.addWidget(self.armorlevellineEdit, 1, 1, 1, 3)

        self.armortypecomboBox = ArmorChooseComboBox(Form)
        self.armortypecomboBox.setObjectName(u"护甲类型")

        self.gridLayout_6.addWidget(self.armortypecomboBox, 0, 1, 1, 2)

        self.armormysticalcomboBox = hasOrNotComboBox(Form)
        self.armormysticalcomboBox.setObjectName(u"护甲神秘")

        self.gridLayout_6.addWidget(self.armormysticalcomboBox, 3, 1, 1, 2)

        self.label_23 = QLabel(Form)
        self.label_23.setObjectName(u"护甲属性百分比")

        self.gridLayout_6.addWidget(self.label_23, 2, 0, 1, 1)

        self.armorlevellabel = QLabel(Form)
        self.armorlevellabel.setObjectName(u"护甲等级")

        self.gridLayout_6.addWidget(self.armorlevellabel, 1, 0, 1, 1)

        self.gridLayout_stack1.addLayout(self.gridLayout_6, 3, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"头盔")
        self.helmetattr1lineEdit = intLineEdit(Form, min=50, max=150)
        self.helmetattr1lineEdit.setObjectName(u"头盔属性1")

        self.gridLayout_7.addWidget(self.helmetattr1lineEdit, 2, 1, 1, 1)

        self.helmettypelabel = QLabel(Form)
        self.helmettypelabel.setObjectName(u"头盔类型")

        self.gridLayout_7.addWidget(self.helmettypelabel, 0, 0, 1, 1)

        self.helmetToStorage = QPushButton(Form)
        self.helmetToStorage.setObjectName("头盔加入仓库")
        self.helmetToStorage.clicked.connect(lambda: self.EquipToStorage("helmet"))
        self.gridLayout_7.addWidget(self.helmetToStorage, 0, 4, 1, 1)

        self.helmetattr2lineEdit = intLineEdit(Form, min=50, max=150)
        self.helmetattr2lineEdit.setObjectName(u"头盔属性2")

        self.gridLayout_7.addWidget(self.helmetattr2lineEdit, 2, 2, 1, 1)

        self.helmetattr4lineEdit = intLineEdit(Form, min=50, max=150)
        self.helmetattr4lineEdit.setObjectName(u"头盔属性4")

        self.gridLayout_7.addWidget(self.helmetattr4lineEdit, 2, 4, 1, 1)

        self.helmetattr3lineEdit = intLineEdit(Form, min=50, max=150)
        self.helmetattr3lineEdit.setObjectName(u"头盔属性3")

        self.gridLayout_7.addWidget(self.helmetattr3lineEdit, 2, 3, 1, 1)

        self.helmetmysticallabel = QLabel(Form)
        self.helmetmysticallabel.setObjectName(u"头盔神秘")

        self.gridLayout_7.addWidget(self.helmetmysticallabel, 3, 0, 1, 1)

        self.helmetlevellineEdit = intLineEdit(Form, min=1, max=500)
        self.helmetlevellineEdit.setObjectName(u"头盔等级")

        self.gridLayout_7.addWidget(self.helmetlevellineEdit, 1, 1, 1, 3)

        self.helmettypecomboBox = helmetChooseComboBox(Form)
        self.helmettypecomboBox.setObjectName(u"头盔类型")

        self.gridLayout_7.addWidget(self.helmettypecomboBox, 0, 1, 1, 2)

        self.helmetmysticalcomboBox = hasOrNotComboBox(Form)
        self.helmetmysticalcomboBox.setObjectName(u"头盔神秘")

        self.gridLayout_7.addWidget(self.helmetmysticalcomboBox, 3, 1, 1, 2)

        self.label_27 = QLabel(Form)
        self.label_27.setObjectName(u"头盔属性百分比")

        self.gridLayout_7.addWidget(self.label_27, 2, 0, 1, 1)

        self.helmetlevellabel = QLabel(Form)
        self.helmetlevellabel.setObjectName(u"头盔等级")

        self.gridLayout_7.addWidget(self.helmetlevellabel, 1, 0, 1, 1)

        self.gridLayout_stack1.addLayout(self.gridLayout_7, 4, 1, 1, 1)

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

        # self.pushButton_4 = QPushButton(Form)
        # self.pushButton_4.clicked.connect(self.text_equipSet)
        # self.pushButton_4.setObjectName(u"快捷写入装备")
        # self.gridLayout_8.addWidget(self.pushButton_4, 1, 0, 1, 1)
        # self.pushButton_4.hide()

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.clicked.connect(lambda: self.accuracy_attr())
        self.pushButton_4.setObjectName(u"分配属性点")
        self.gridLayout_8.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.clicked.connect(self.percentage_attr)
        self.pushButton_5.setObjectName(u"比例分配属性")
        self.gridLayout_8.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.gridLayout_stack1.addLayout(self.gridLayout_8, 5, 0, 1, 2)

        self.STATCardForm = STATCardPanel(Form, cardList=self.cardList, cardlistcomboBox=self.cardlistcomboBox)
        self.gridLayout_stack2.addWidget(self.STATCardForm)

        self.rightMenuCreat()
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle("我的卡片")
        self.cardlistlabel.setText("卡片列表")
        self.halolabel.setText("光环百分比")
        self.cardtypelabel.setText("卡片类型")

        self.levellabel.setText("卡片等级")
        self.remainder_point_text.setText("可用点数")
        self.STRlabel.setText("力量")
        self.AGIlabel.setText("敏捷")
        self.INTlabel.setText("智力")
        self.VITlabel.setText("体魄")
        self.SPRlabel.setText("精神")
        self.RESlabel.setText("意志")
        self.weaponlabel.setText("武器类型")
        self.weaponlevellabel.setText("等级")

        self.label_15.setText("属性百分比")
        self.weaponmysticallabel.setText("神秘")
        self.glovetypelabel.setText("手套类型")
        self.glovemysticallabel.setText("神秘")

        self.gloveattrlabel.setText("属性百分比")
        self.glovelevellabel.setText("等级")
        # self.skillslotlabel.setText("技能位")
        # self.skilllabel.setText("技能")

        self.armortypelabel.setText("护甲类型")
        self.armormysticallabel.setText("神秘")

        self.label_23.setText("属性百分比")
        self.armorlevellabel.setText("等级")
        self.helmettypelabel.setText("头盔类型")
        self.helmetmysticallabel.setText("神秘")

        self.label_27.setText("属性百分比")
        self.helmetlevellabel.setText("等级")
        self.toggleSTATButton.setText("STAT")
        self.pushButton.setText("存储卡片")
        self.pushButton_2.setText("覆盖当前卡片")
        self.pushButton_3.setText("删除当前卡片")
        self.pushButton_4.setText("分配属性点")
        self.pushButton_5.setText("百分比分配属性")
        self.equipStorageButton.setText("装备仓库")
        self.weaponToStorage.setText("加入仓库")
        self.gloveToStorage.setText("加入仓库")
        self.ArmorToStorage.setText("加入仓库")
        self.helmetToStorage.setText("加入仓库")

    # retranslateUi

    def open(self):
        global_env.mainWin.hide()
        self.show()

    def closeEvent(self, event):
        global_env.mainWin.show()
        event.accept()

    def makeMyCard(self):
        if self.isSTAT():
            return self.STATCardForm.makeMyCard()
        halo = self.halolineEdit.text()
        character = self.cardtypecomboBox.currentIndex()
        level = self.levellineEdit.text()
        attrSTR = self.STRspinBox.getValue()
        attrAGI = self.AGIspinBox.getValue()
        attrINT = self.INTspinBox.getValue()
        attrVIT = self.VITspinBox.getValue()
        attrSPR = self.SPRspinBox.getValue()
        attrRES = self.RESspinBox.getValue()
        attrSet = cardAttr(attrSTR, attrAGI, attrINT, attrVIT, attrSPR, attrRES)

        sklSlot = self.cardSkillPanel.skillslotcomboBox.currentIndex()

        skillindexlist = self.cardSkillPanel.get4index()
        skill_1 = skill(skillindexlist[0])
        skill_2 = skill(skillindexlist[1])
        skill_3 = skill(skillindexlist[2])
        skill_4 = skill(skillindexlist[3])
        skillSet = SKILLSet(skill_1, skill_2, skill_3, skill_4)

        weaponType = self.weapontypecomboBox.currentIndex()
        weaponLevel = self.weaponlevellineEdit.text()
        weaponAttr1 = self.weaponattr1lineEdit.text()
        weaponAttr2 = self.weaponattr2lineEdit.text()
        weaponAttr3 = self.weaponattr3lineEdit.text()
        weaponAttr4 = self.weaponattr4lineEdit.text()
        weaponHasMystical = self.weaponmysticalcomboBox.currentIndex()
        weapon = weaponEquip(weaponLevel, weaponAttr1, weaponAttr2, weaponAttr3, weaponAttr4, weaponHasMystical,
                             weaponType)

        gloveType = self.glovetypecomboBox.currentIndex()
        gloveLevel = self.glovelevellineEdit.text()
        gloveAttr1 = self.gloveattr1lineEdit.text()
        gloveAttr2 = self.gloveattr2lineEdit.text()
        gloveAttr3 = self.gloveattr3lineEdit.text()
        gloveAttr4 = self.gloveattr4lineEdit.text()
        gloveHasMystical = self.glovemysticalcomboBox.currentIndex()
        glove = gloveEquip(gloveLevel, gloveAttr1, gloveAttr2, gloveAttr3, gloveAttr4, gloveHasMystical,
                           gloveType)

        ArmorType = self.armortypecomboBox.currentIndex()
        ArmorLevel = self.armorlevellineEdit.text()
        ArmorAttr1 = self.armorattr1lineEdit.text()
        ArmorAttr2 = self.armorattr2lineEdit.text()
        ArmorAttr3 = self.armorattr3lineEdit.text()
        ArmorAttr4 = self.armorattr4lineEdit.text()
        ArmorHasMystical = self.armormysticalcomboBox.currentIndex()
        Armor = ArmorEquip(ArmorLevel, ArmorAttr1, ArmorAttr2, ArmorAttr3, ArmorAttr4, ArmorHasMystical,
                           ArmorType)

        helmetType = self.helmettypecomboBox.currentIndex()
        helmetLevel = self.helmetlevellineEdit.text()
        helmetAttr1 = self.helmetattr1lineEdit.text()
        helmetAttr2 = self.helmetattr2lineEdit.text()
        helmetAttr3 = self.helmetattr3lineEdit.text()
        helmetAttr4 = self.helmetattr4lineEdit.text()
        helmetHasMystical = self.helmetmysticalcomboBox.currentIndex()
        helmet = helmetEquip(helmetLevel, helmetAttr1, helmetAttr2, helmetAttr3, helmetAttr4, helmetHasMystical,
                             helmetType)

        equipSet = EQUIPSet(weapon, glove, Armor, helmet)

        card = self.cardClass(halo, character, level, attrSet, sklSlot, skillSet, equipSet)

        return card

    def setMyCard(self, card):
        if self.isSTAT():
            self.STATCardForm.setMyCard(card)
            return
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

        self.halolineEdit.setText(halo)
        self.cardtypecomboBox.setCurrentIndex(character)
        self.levellineEdit.setText(level)
        self.STRspinBox.setValue(attrSTR)
        self.AGIspinBox.setValue(attrAGI)
        self.INTspinBox.setValue(attrINT)
        self.VITspinBox.setValue(attrVIT)
        self.SPRspinBox.setValue(attrSPR)
        self.RESspinBox.setValue(attrRES)

        self.cardSkillPanel.skillslotcomboBox.setCurrentIndex(sklSlot)

        skillindexlist = [skill_1.data, skill_2.data, skill_3.data, skill_4.data]
        self.cardSkillPanel.set4index(skillindexlist)

        self.weapontypecomboBox.setCurrentIndex(weapon.equipType)
        self.weaponlevellineEdit.setText(weapon.level)
        self.weaponattr1lineEdit.setText(weapon.attr0)
        self.weaponattr2lineEdit.setText(weapon.attr1)
        self.weaponattr3lineEdit.setText(weapon.attr2)
        self.weaponattr4lineEdit.setText(weapon.attr3)
        self.weaponmysticalcomboBox.setCurrentIndex(weapon.hasMystical)

        self.glovetypecomboBox.setCurrentIndex(glove.equipType)
        self.glovelevellineEdit.setText(glove.level)
        self.gloveattr1lineEdit.setText(glove.attr0)
        self.gloveattr2lineEdit.setText(glove.attr1)
        self.gloveattr3lineEdit.setText(glove.attr2)
        self.gloveattr4lineEdit.setText(glove.attr3)
        self.glovemysticalcomboBox.setCurrentIndex(glove.hasMystical)

        self.armortypecomboBox.setCurrentIndex(Armor.equipType)
        self.armorlevellineEdit.setText(Armor.level)
        self.armorattr1lineEdit.setText(Armor.attr0)
        self.armorattr2lineEdit.setText(Armor.attr1)
        self.armorattr3lineEdit.setText(Armor.attr2)
        self.armorattr4lineEdit.setText(Armor.attr3)
        self.armormysticalcomboBox.setCurrentIndex(Armor.hasMystical)

        self.helmettypecomboBox.setCurrentIndex(helmet.equipType)
        self.helmetlevellineEdit.setText(helmet.level)
        self.helmetattr1lineEdit.setText(helmet.attr0)
        self.helmetattr2lineEdit.setText(helmet.attr1)
        self.helmetattr3lineEdit.setText(helmet.attr2)
        self.helmetattr4lineEdit.setText(helmet.attr3)
        self.helmetmysticalcomboBox.setCurrentIndex(helmet.hasMystical)

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

        self.halolineEdit.setText(halo)
        self.cardtypecomboBox.setCurrentIndex(character)
        self.levellineEdit.setText(level)
        self.STRspinBox.setValue(attrSTR)
        self.AGIspinBox.setValue(attrAGI)
        self.INTspinBox.setValue(attrINT)
        self.VITspinBox.setValue(attrVIT)
        self.SPRspinBox.setValue(attrSPR)
        self.RESspinBox.setValue(attrRES)

        self.cardSkillPanel.skillslotcomboBox.setCurrentIndex(sklSlot)

        self.cardSkillPanel.set4index([0, 0, 0, 0])

        self.weapontypecomboBox.setCurrentIndex(weapon.equipType)
        self.weaponlevellineEdit.setText(weapon.level)
        self.weaponattr1lineEdit.setText(weapon.attr0)
        self.weaponattr2lineEdit.setText(weapon.attr1)
        self.weaponattr3lineEdit.setText(weapon.attr2)
        self.weaponattr4lineEdit.setText(weapon.attr3)
        self.weaponmysticalcomboBox.setCurrentIndex(weapon.hasMystical)

        self.glovetypecomboBox.setCurrentIndex(glove.equipType)
        self.glovelevellineEdit.setText(glove.level)
        self.gloveattr1lineEdit.setText(glove.attr0)
        self.gloveattr2lineEdit.setText(glove.attr1)
        self.gloveattr3lineEdit.setText(glove.attr2)
        self.gloveattr4lineEdit.setText(glove.attr3)
        self.glovemysticalcomboBox.setCurrentIndex(glove.hasMystical)

        self.armortypecomboBox.setCurrentIndex(Armor.equipType)
        self.armorlevellineEdit.setText(Armor.level)
        self.armorattr1lineEdit.setText(Armor.attr0)
        self.armorattr2lineEdit.setText(Armor.attr1)
        self.armorattr3lineEdit.setText(Armor.attr2)
        self.armorattr4lineEdit.setText(Armor.attr3)
        self.armormysticalcomboBox.setCurrentIndex(Armor.hasMystical)

        self.helmettypecomboBox.setCurrentIndex(helmet.equipType)
        self.helmetlevellineEdit.setText(helmet.level)
        self.helmetattr1lineEdit.setText(helmet.attr0)
        self.helmetattr2lineEdit.setText(helmet.attr1)
        self.helmetattr3lineEdit.setText(helmet.attr2)
        self.helmetattr4lineEdit.setText(helmet.attr3)
        self.helmetmysticalcomboBox.setCurrentIndex(helmet.hasMystical)

        self.STATCardForm.newMyCard()

    def myCardListUpdate(self):
        myCardList = self.cardList
        currentIndex = self.cardlistcomboBox.currentIndex()
        self.cardlistcomboBox.clear()
        for k, v in myCardList.items():
            self.cardlistcomboBox.addItem(k)
        self.cardlistcomboBox.setCurrentIndex(currentIndex)

    def saveMyCard(self):
        if self.isSTAT():
            self.STATCardForm.saveMyCard()
            return
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
            self.cardlistcomboBox.setCurrentText(text)

    def editMyCard(self):
        if self.isSTAT():
            self.STATCardForm.editMyCard()
            return
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
        if self.isSTAT():
            self.STATCardForm.delMyCard()
            return
        # index = self.comboBox.currentIndex()
        text = self.cardlistcomboBox.currentText()
        if text == "新卡片":
            QMessageBox.critical(self, "错误", "模板不可删除", QMessageBox.Yes)
            return
        yes = QMessageBox.question(self, "提问对话框", "确认删除？", QMessageBox.Yes | QMessageBox.No)
        if yes == QMessageBox.Yes:
            del (self.cardList[text])

    def chooseMyCard(self, tag):  # combobox点击事件
        if tag not in self.cardList.keys():
            return
        card = self.cardList[tag]
        if card is None:
            self.newMyCard()
        else:
            try:
                if whatCardClass(card) == 1:
                    self.toggleSTAT(False)
                    self.STATCardForm.setMyCard(card)
                    return
                elif whatCardClass(card) == 0:
                    self.toggleSTAT(True)
                    self.setMyCard(card)
                else:
                    return
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

        level = self.levellineEdit.getValue()
        STR = self.STRspinBox.getValue()
        AGI = self.AGIspinBox.getValue()
        INT = self.INTspinBox.getValue()
        VIT = self.VITspinBox.getValue()
        SPR = self.SPRspinBox.getValue()
        RES = self.RESspinBox.getValue()

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
        halo = self.halolineEdit.getValue()
        # if halo > 200:
        #     return False, "光环不能大于200!"
        sklSlotNum = self.cardSkillPanel.skillslotcomboBox.currentIndex() + 1
        sklList = self.cardSkillPanel.getshortindex()

        if len(sklList) > sklSlotNum:
            return False, "技能数量大于技能位!"
        used_halo = 0
        for skl in sklList:
            used_halo += all_skill["cost"][skl - 1]
        if used_halo > halo:
            return False, "技能所需点数超过光环！"
        # self.comboBox_8.setObjectName(u"武器类型")
        # self.lineEdit_3.setObjectName(u"武器等级")
        # self.lineEdit_4.setObjectName(u"武器属性1")
        # self.lineEdit_5.setObjectName(u"武器属性2")
        # self.lineEdit_6.setObjectName(u"武器属性3")
        # self.lineEdit_7.setObjectName(u"武器属性4")
        if self.weapontypecomboBox.currentIndex() != 0:
            if self.weaponlevellineEdit.getValue() > 500:
                return False, "装备等级不能大于500!"
            if self.weaponattr1lineEdit.getValue() < 50 or self.weaponattr2lineEdit.getValue() < 50 or self.weaponattr3lineEdit.getValue() < 50 or self.weaponattr4lineEdit.getValue() < 50:
                return False, "装备属性不能小于50!"
            if self.weaponattr1lineEdit.getValue() > 150 or self.weaponattr2lineEdit.getValue() > 150 or self.weaponattr3lineEdit.getValue() > 150 or self.weaponattr4lineEdit.getValue() > 150:
                return False, "装备属性不能大于150!"

        # self.comboBox_10.setObjectName(u"手套类型")
        # self.lineEdit_12.setObjectName(u"手套等级")
        # self.lineEdit_8.setObjectName(u"手套属性1")
        # self.lineEdit_9.setObjectName(u"手套属性2")
        # self.lineEdit_11.setObjectName(u"手套属性3")
        # self.lineEdit_10.setObjectName(u"手套属性4")
        if self.glovetypecomboBox.currentIndex() != 0:
            if self.glovelevellineEdit.getValue() > 500:
                return False, "装备等级不能大于500!"
            if self.gloveattr1lineEdit.getValue() < 50 or self.gloveattr2lineEdit.getValue() < 50 or self.gloveattr3lineEdit.getValue() < 50 or self.gloveattr4lineEdit.getValue() < 50:
                return False, "装备属性不能小于50!"
            if self.gloveattr1lineEdit.getValue() > 150 or self.gloveattr2lineEdit.getValue() > 150 or self.gloveattr3lineEdit.getValue() > 150 or self.gloveattr4lineEdit.getValue() > 150:
                return False, "装备属性不能大于150!"

        # self.comboBox_12.setObjectName(u"护甲类型")
        # self.lineEdit_17.setObjectName(u"护甲等级")
        # self.lineEdit_13.setObjectName(u"护甲属性1")
        # self.lineEdit_14.setObjectName(u"护甲属性2")
        # self.lineEdit_16.setObjectName(u"护甲属性3")
        # self.lineEdit_15.setObjectName(u"护甲属性4")
        if self.armortypecomboBox.currentIndex() != 0:
            if self.armorlevellineEdit.getValue() > 500:
                return False, "装备等级不能大于500!"
            if self.armorattr1lineEdit.getValue() < 50 or self.armorattr2lineEdit.getValue() < 50 or self.armorattr3lineEdit.getValue() < 50 or self.armorattr4lineEdit.getValue() < 50:
                return False, "装备属性不能小于50!"
            if self.armorattr1lineEdit.getValue() > 150 or self.armorattr2lineEdit.getValue() > 150 or self.armorattr3lineEdit.getValue() > 150 or self.armorattr4lineEdit.getValue() > 150:
                return False, "装备属性不能大于150!"

        # self.comboBox_14.setObjectName(u"头盔类型")
        # self.lineEdit_22.setObjectName(u"头盔等级")
        # self.lineEdit_18.setObjectName(u"头盔属性1")
        # self.lineEdit_19.setObjectName(u"头盔属性2")
        # self.lineEdit_21.setObjectName(u"头盔属性3")
        # self.lineEdit_20.setObjectName(u"头盔属性4")
        if self.helmettypecomboBox.currentIndex() != 0:
            if self.helmetlevellineEdit.getValue() > 500:
                return False, "装备等级不能大于500!"
            if self.helmetattr1lineEdit.getValue() < 50 or self.helmetattr2lineEdit.getValue() < 50 or self.helmetattr3lineEdit.getValue() < 50 or self.helmetattr4lineEdit.getValue() < 50:
                return False, "装备属性不能小于50!"
            if self.helmetattr1lineEdit.getValue() > 150 or self.helmetattr2lineEdit.getValue() > 150 or self.helmetattr3lineEdit.getValue() > 150 or self.helmetattr4lineEdit.getValue() > 150:
                return False, "装备属性不能大于150!"

        return True, "无错误"

    def text_equipSet(self):
        text, ok = QInputDialog.getMultiLineText(self, '快捷复制导入套装', '必须以武器为首行：')
        if not (ok and text):
            return
        mySet = text_to_equipSet(text)
        self.equipSetImport(mySet)

    def equipSetImport(self, mySet):
        if mySet.weapon is not None:
            self.weapontypecomboBox.setCurrentIndex(mySet.weapon.equipType)
            self.weaponlevellineEdit.setText(mySet.weapon.level)
            self.weaponattr1lineEdit.setText(mySet.weapon.attr0)
            self.weaponattr2lineEdit.setText(mySet.weapon.attr1)
            self.weaponattr3lineEdit.setText(mySet.weapon.attr2)
            self.weaponattr4lineEdit.setText(mySet.weapon.attr3)
            self.weaponmysticalcomboBox.setCurrentIndex(mySet.weapon.hasMystical)
        if mySet.glove is not None:
            self.glovetypecomboBox.setCurrentIndex(mySet.glove.equipType)
            self.glovelevellineEdit.setText(mySet.glove.level)
            self.gloveattr1lineEdit.setText(mySet.glove.attr0)
            self.gloveattr2lineEdit.setText(mySet.glove.attr1)
            self.gloveattr3lineEdit.setText(mySet.glove.attr2)
            self.gloveattr4lineEdit.setText(mySet.glove.attr3)
            self.glovemysticalcomboBox.setCurrentIndex(mySet.glove.hasMystical)
        if mySet.Armor is not None:
            self.armortypecomboBox.setCurrentIndex(mySet.Armor.equipType)
            self.armorlevellineEdit.setText(mySet.Armor.level)
            self.armorattr1lineEdit.setText(mySet.Armor.attr0)
            self.armorattr2lineEdit.setText(mySet.Armor.attr1)
            self.armorattr3lineEdit.setText(mySet.Armor.attr2)
            self.armorattr4lineEdit.setText(mySet.Armor.attr3)
            self.armormysticalcomboBox.setCurrentIndex(mySet.Armor.hasMystical)
        if mySet.helmet is not None:
            self.helmettypecomboBox.setCurrentIndex(mySet.helmet.equipType)
            self.helmetlevellineEdit.setText(mySet.helmet.level)
            self.helmetattr1lineEdit.setText(mySet.helmet.attr0)
            self.helmetattr2lineEdit.setText(mySet.helmet.attr1)
            self.helmetattr3lineEdit.setText(mySet.helmet.attr2)
            self.helmetattr4lineEdit.setText(mySet.helmet.attr3)
            self.helmetmysticalcomboBox.setCurrentIndex(mySet.helmet.hasMystical)

    def set_remainder_point(self):
        level = self.levellineEdit.getValue()
        STR = self.STRspinBox.getValue()
        AGI = self.AGIspinBox.getValue()
        INT = self.INTspinBox.getValue()
        VIT = self.VITspinBox.getValue()
        SPR = self.SPRspinBox.getValue()
        RES = self.RESspinBox.getValue()

        maxPoint = level * 3 + 6
        remainder_point = maxPoint - (STR + AGI + INT + VIT + SPR + RES)
        self.remainder_point.setText(str(remainder_point))

    def percentage_attr(self):
        text, ok = QInputDialog.getText(self, '百分比分配属性', '输入6个整数，空格分割')
        if ok and text:
            percentage_text = text.split()
            attr_list = []
            level = self.levellineEdit.getValue()
            point = level * 3
            for i in range(6):
                attr_list.append(int(point * int(percentage_text[i]) / 100 + 1))
            self.STRspinBox.setValue(attr_list[0])
            self.AGIspinBox.setValue(attr_list[1])
            self.INTspinBox.setValue(attr_list[2])
            self.VITspinBox.setValue(attr_list[3])
            self.SPRspinBox.setValue(attr_list[4])
            self.RESspinBox.setValue(attr_list[5])
            self.set_remainder_point()

    def accuracy_attr(self, text=None):
        if text is None:
            text, ok = QInputDialog.getText(self, '直接分配属性', '输入6个整数，空格分割')
            if not (ok and text):
                return

        accuracy_text = text.split()
        attr_list = []
        for i in range(6):
            attr_list.append(int(accuracy_text[i]))
        self.STRspinBox.setValue(attr_list[0])
        self.AGIspinBox.setValue(attr_list[1])
        self.INTspinBox.setValue(attr_list[2])
        self.VITspinBox.setValue(attr_list[3])
        self.SPRspinBox.setValue(attr_list[4])
        self.RESspinBox.setValue(attr_list[5])
        self.set_remainder_point()

    def openEquipChooseWindow(self):
        ecw = equipChooseWindow(self)
        ecw.setWindowModality(Qt.ApplicationModal)
        ecw.Signal_OneParameter.connect(self.equipSetImport)
        ecw.open()

    def EquipToStorage(self, equipParts):
        result0, result1 = self.preEquipToStorage(equipParts)
        if not result0:
            QMessageBox.critical(self, "错误", result1, QMessageBox.Yes)
            return
        text, ok = QInputDialog.getText(self, '设置装备显示名', '输入名称：', text=result1.toSimpleString())
        if ok and text:
            if text in global_env.equipStorageDict[equipParts].keys():
                QMessageBox.critical(self, "错误", "保存失败，与已有配置重名", QMessageBox.Yes)
                return
            global_env.equipStorageDict[equipParts][text] = result1

    def preEquipToStorage(self, equipParts):
        if equipParts == "weapon":
            equipClass = weaponEquip
            equipType = self.weapontypecomboBox.currentIndex()
            level = self.weaponlevellineEdit.text()
            attr0 = self.weaponattr1lineEdit.text()
            attr1 = self.weaponattr2lineEdit.text()
            attr2 = self.weaponattr3lineEdit.text()
            attr3 = self.weaponattr4lineEdit.text()
            hasMystical = self.weaponmysticalcomboBox.currentIndex()
        elif equipParts == "glove":
            equipClass = gloveEquip
            equipType = self.glovetypecomboBox.currentIndex()
            level = self.glovelevellineEdit.text()
            attr0 = self.gloveattr1lineEdit.text()
            attr1 = self.gloveattr2lineEdit.text()
            attr2 = self.gloveattr3lineEdit.text()
            attr3 = self.gloveattr4lineEdit.text()
            hasMystical = self.glovemysticalcomboBox.currentIndex()
        elif equipParts == "Armor":
            equipClass = ArmorEquip
            equipType = self.armortypecomboBox.currentIndex()
            level = self.armorlevellineEdit.text()
            attr0 = self.armorattr1lineEdit.text()
            attr1 = self.armorattr2lineEdit.text()
            attr2 = self.armorattr3lineEdit.text()
            attr3 = self.armorattr4lineEdit.text()
            hasMystical = self.armormysticalcomboBox.currentIndex()
        elif equipParts == "helmet":
            equipClass = helmetEquip
            equipType = self.helmettypecomboBox.currentIndex()
            level = self.helmetlevellineEdit.text()
            attr0 = self.helmetattr1lineEdit.text()
            attr1 = self.helmetattr2lineEdit.text()
            attr2 = self.helmetattr3lineEdit.text()
            attr3 = self.helmetattr4lineEdit.text()
            hasMystical = self.helmetmysticalcomboBox.currentIndex()
        else:
            return False, ""
        if equipType == 0:
            return False, "无类型装备无法添加!"
        if not global_env.test_mode:
            if int(level) > 500:
                return False, "装备等级不能大于500!"
            if int(attr0) < 50 or int(attr1) < 50 or int(attr2) < 50 or int(attr3) < 50:
                return False, "装备属性不能小于50!"
            if int(attr0) > 150 or int(attr1) > 150 or int(attr2) > 150 or int(attr3) > 150:
                return False, "装备属性不能大于150!"

        result = equipClass(level, attr0, attr1, attr2, attr3, hasMystical, equipType)
        return True, result

    def rightMenuCreat(self):
        self.contextMenu = QMenu(self)
        self.cardImport = self.contextMenu.addAction(u'卡片导入')
        self.skillImport = self.contextMenu.addAction(u'技能导入')
        self.equipImport = self.contextMenu.addAction(u'装备导入')
        self.caclImport = self.contextMenu.addAction(u'结果导入')
        self.allImport = self.contextMenu.addAction(u'全部导入')
        self.cacloutput = self.contextMenu.addAction(u'全部导出')
        self.cardImport.triggered.connect(lambda: self.cardImportFun())
        self.skillImport.triggered.connect(lambda: self.skillImportFun())
        self.equipImport.triggered.connect(lambda: self.equipImportFun())
        self.allImport.triggered.connect(lambda: self.allImportFun())
        self.caclImport.triggered.connect(lambda: self.caclImportFun())
        self.cacloutput.triggered.connect(lambda: self.cacloutputFun())

    def rightMenuShow(self):
        self.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
        self.contextMenu.show()

    def cardImportFun(self, text=None):
        if text is None:
            text, ok = QInputDialog.getMultiLineText(self, '导入卡片', '咕咕镇计算器格式')
            if not (ok and text):
                return
        data = text.split()
        for i in range(len(all_character['data'])):
            if data[0] == all_character['data'][i]:
                self.cardtypecomboBox.setCurrentIndex(i)
                break
        self.levellineEdit.setText(data[1])
        self.cardSkillPanel.skillslotcomboBox.setCurrentText(data[2])
        self.STRspinBox.setValue(int(data[3]))
        self.AGIspinBox.setValue(int(data[4]))
        self.INTspinBox.setValue(int(data[5]))
        self.VITspinBox.setValue(int(data[6]))
        self.SPRspinBox.setValue(int(data[7]))
        self.RESspinBox.setValue(int(data[8]))

    def skillImportFun(self, text=None):
        if text is None:
            text, ok = QInputDialog.getMultiLineText(self, '导入技能', '咕咕镇计算器格式')
            if not (ok and text):
                return
        self.cardSkillPanel.setFromCaclText(text)
        # data = text.split()
        # sklBoxList = [self.skill1comboBox, self.skill2comboBox, self.skill3comboBox, self.skill4comboBox]
        # index = 0
        # for i in range(1, len(data)):
        #     for j in range(len(all_skill['data'])):
        #         if data[i] == all_skill['data'][j]:
        #             sklBoxList[index].setCurrentIndex(j + 1)
        #             index += 1
        #             break
        # for i in range(index, 4):
        #     sklBoxList[i].setCurrentIndex(0)

    def equipImportFun(self, text=None):
        if text is None:
            text, ok = QInputDialog.getMultiLineText(self, '导入装备', '咕咕镇计算器格式,')
            if not (ok and text):
                return
        if text.startswith("武器"):
            mySet = text_to_equipSet(text)
            self.equipSetImport(mySet)
            return
        data = text.split("\n")
        for i in range(4):
            data[i] = data[i].split()
        for i in range(len(all_equip['data']["weapon"])):
            if data[0][0] == all_equip['data']["weapon"][i]:
                self.weapontypecomboBox.setCurrentIndex(i + 1)
                self.weaponlevellineEdit.setText(data[0][1])
                self.weaponattr1lineEdit.setText(data[0][2])
                self.weaponattr2lineEdit.setText(data[0][3])
                self.weaponattr3lineEdit.setText(data[0][4])
                self.weaponattr4lineEdit.setText(data[0][5])
                self.weaponmysticalcomboBox.setCurrentIndex(int(data[0][6]))
                break
            elif data[0][0] == "NONE":
                self.weapontypecomboBox.setCurrentIndex(0)
                break
        for i in range(len(all_equip['data']["glove"])):
            if data[1][0] == all_equip['data']["glove"][i]:
                self.glovetypecomboBox.setCurrentIndex(i + 1)
                self.glovelevellineEdit.setText(data[1][1])
                self.gloveattr1lineEdit.setText(data[1][2])
                self.gloveattr2lineEdit.setText(data[1][3])
                self.gloveattr3lineEdit.setText(data[1][4])
                self.gloveattr4lineEdit.setText(data[1][5])
                self.glovemysticalcomboBox.setCurrentIndex(int(data[1][6]))
                break
            elif data[1][0] == "NONE":
                self.glovetypecomboBox.setCurrentIndex(0)
                break
        for i in range(len(all_equip['data']["Armor"])):
            if data[2][0] == all_equip['data']["Armor"][i]:
                self.armortypecomboBox.setCurrentIndex(i + 1)
                self.armorlevellineEdit.setText(data[2][1])
                self.armorattr1lineEdit.setText(data[2][2])
                self.armorattr2lineEdit.setText(data[2][3])
                self.armorattr3lineEdit.setText(data[2][4])
                self.armorattr4lineEdit.setText(data[2][5])
                self.armormysticalcomboBox.setCurrentIndex(int(data[2][6]))
                break
            elif data[2][0] == "NONE":
                self.armortypecomboBox.setCurrentIndex(0)
                break
        for i in range(len(all_equip['data']["helmet"])):
            if data[3][0] == all_equip['data']["helmet"][i]:
                self.helmettypecomboBox.setCurrentIndex(i + 1)
                self.helmetlevellineEdit.setText(data[3][1])
                self.helmetattr1lineEdit.setText(data[3][2])
                self.helmetattr2lineEdit.setText(data[3][3])
                self.helmetattr3lineEdit.setText(data[3][4])
                self.helmetattr4lineEdit.setText(data[3][5])
                self.helmetmysticalcomboBox.setCurrentIndex(int(data[3][6]))
                break
            elif data[3][0] == "NONE":
                self.helmettypecomboBox.setCurrentIndex(0)
                break

    def allImportFun(self, text=None):
        if text is None:
            text, ok = QInputDialog.getMultiLineText(self, '导入光环、卡片、装备、技能', '咕咕镇计算器格式')
            if not (ok and text):
                return

        text = re.sub(r"\n\n", "\n", text)
        text = text.split("\n")
        self.halolineEdit.setText(text[0])
        self.cardImportFun(text[1] + "\n" + text[2])
        self.equipImportFun(text[3] + "\n" + text[4] + "\n" + text[5] + "\n" + text[6])
        self.skillImportFun(text[7])

    def caclImportFun(self, text=None):
        if text is None:
            text, ok = QInputDialog.getMultiLineText(self, '导入、加点、装备、技能', '咕咕镇计算器结果')
            if not (ok and text):
                return

        text = re.sub(r"\n\n", "\n", text)
        text = text.split("\n")
        myindex = 0
        for num in range(len(text)):
            if re.match(r"\d+ \d+ \d+ \d+ \d+ \d+", text[num]):
                myindex = num
                break
            if num + 1 == len(text):
                QMessageBox.critical(self, "错误", "格式错误", QMessageBox.Yes)
                return

        self.accuracy_attr(text[myindex])
        self.equipImportFun(
            text[myindex + 1] + "\n" + text[myindex + 2] + "\n" + text[myindex + 3] + "\n" + text[myindex + 4])
        self.skillImportFun(text[myindex + 5])

    def cacloutputFun(self, text=None):
        if not self.ableCheck():
            return

        thiscard = self.makeMyCard()
        thistext = thiscard.make_gu_text()
        QInputDialog.getMultiLineText(self, '请复制', "", thistext)

    def toggleSTAT(self, flag=None):
        if flag is None:
            flag = self.isSTAT()
        if flag:
            self.stack.setCurrentIndex(0)
        else:
            self.stack.setCurrentIndex(1)

    def isSTAT(self):
        return self.stack.currentIndex() == 1
