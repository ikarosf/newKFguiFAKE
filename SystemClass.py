# all_skill = {
#     "name": [["启程之誓", "启程之心", "启程之风"],
#              ["破壁之心", "破魔之心"],
#              ["伤口恶化", "精神创伤", "铁甲尖刺"],
#              ["沸血之志", "波澜不惊", "飓风之力"]],
#
#     "data": [["SHI", "XIN", "FENG"],
#              ["BI", "MO"],
#              ["SHANG", "SHEN", "CI"],
#              ["FEI", "BO", "JU"]
#              ]
# }

all_skill = {
    "name": ["启程之誓", "启程之心", "启程之风",
             "破壁之心", "破魔之心", "复合护盾", "鲜血渴望", "削骨之痛",
             "伤口恶化", "精神创伤", "铁甲尖刺", "忍无可忍", "热血战魂",
             "沸血之志", "波澜不惊", "飓风之力", "红蓝双刺", "绝对护盾", "后发制人"
             ],

    "data": ["SHI", "XIN", "FENG",
             "BI", "MO", "DUN", "XUE", "XIAO",
             "SHANG", "SHEN", "CI", "REN", "RE",
             "FEI", "BO", "JU", "HONG", "JUE", "HOU"
             ],
    "cost": [10, 10, 10,
             30, 30, 30, 30, 30,
             50, 50, 50, 50, 50,
             100, 100, 100, 100, 100, 100
             ]
}


def getSkillDataOfName(name):
    for i in range(len(all_skill["name"])):
        if all_skill["name"][i] == name:
            return all_skill["data"][i]


def getSkillCostOfName(name):
    for i in range(len(all_skill["name"])):
        if all_skill["name"][i] == name:
            return all_skill["cost"][i]


def getSkillIndexOfName(name):
    for i in range(len(all_skill["name"])):
        if all_skill["name"][i] == name:
            return i


def getSkillIndexOfData(data):
    for i in range(len(all_skill["data"])):
        if all_skill["data"][i] == data:
            return i


all_character = {
    "name": ["琳", "默", "艾", "梦", "薇", "伊"],
    "data": ["LIN", "MO", "AI", "MENG", "WEI", "YI"]
}

all_npc = {
    "name": ["木人", "迅捷蛛", "魔灯", "食铁兽"],
    "data": ["MU", "ZHU", "DENG", "SHOU"]
}

all_equip = {
    "name": {
        "weapon": ["剑", "短弓", "短杖", "荣誉之刃", "刺杀弓", "幽梦匕首", "光辉法杖", "荆棘剑盾", "陨铁重剑"],
        "glove": ["手套", "手环", "秃鹫手套"],
        "Armor": ["铁甲", "皮甲", "布甲", "灵光袍", "荆棘重甲"],
        "helmet": ["头巾", "发饰", "天使缎带"],
    },
    "data": {
        "weapon": ["SWORD", "BOW", "STAFF", "BLADE", "ASSBOW", "DAGGER", "WAND", "SHIELD", "CLAYMORE"],
        "glove": ["GLOVES", "BRACELET", "VULTURE"],
        "Armor": ["PLATE", "LEATHER", "CLOTH", "CLOAK", "THORN"],
        "helmet": ["SCARF", "TIARA", "RIBBON"],
    }
}

all_amulet = {
    "name": [
        "力量", "敏捷", "智力", "体魄", "精神", "意志", "物理攻击", "魔法攻击", "攻击速度", "回复效果", "最大生命", "最大护盾", "生命偷取", "伤害反弹", "暴击几率",
        "技能几率", "物理防御", "魔法防御"
    ],
    "data": [
        "STR", "AGI", "INT", "VIT", "SPR", "MND", "PATK", "MATK", "SPD", "REC", "HP", "SLD", "LCH", "RFL", "CRT", "SKL",
        "PDEF", "MDEF"
    ]
}


class cardAttr:
    def __init__(self, mystr, myagi, myint, myvit, myspr, myres):
        self.STR = mystr
        self.AGI = myagi  # 敏捷
        self.INT = myint  # 智力
        self.VIT = myvit  # 体魄
        self.SPR = myspr  # 精神
        self.RES = myres  # 意志

    def tostring(self):
        text = " STR:"
        text += str(self.STR)
        text += " AGI:"
        text += str(self.AGI)
        text += " INT:"
        text += str(self.INT)
        text += " VIT:"
        text += str(self.VIT)
        text += " SPR:"
        text += str(self.SPR)
        text += " RES:"
        text += str(self.RES)
        return text

    def make_gu_text(self):
        text = ''
        text += str(self.STR)
        text += " "
        text += str(self.AGI)
        text += " "
        text += str(self.INT)
        text += " "
        text += str(self.VIT)
        text += " "
        text += str(self.SPR)
        text += " "
        text += str(self.RES)
        return text


class equip:
    def __init__(self, level, attr0, attr1, attr2, attr3, hasMystical, equipType):
        self.level = level
        self.attr0 = attr0
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
        self.hasMystical = hasMystical
        self.equipType = equipType

    def toString(self):
        text = all_equip["name"][self.partsText][self.equipType - 1]
        text += "\n"
        text += " LV."
        text += self.level
        text += "\n"
        text += self.attr0
        text += "% "
        text += self.attr1
        text += "% "
        text += self.attr2
        text += "% "
        text += self.attr3
        text += "% "
        text += "\n"
        if self.hasMystical:
            text += " 神秘"
        return text

    def toSimpleString(self):
        text = all_equip["name"][self.partsText][self.equipType - 1]
        text += " LV."
        text += self.level
        if self.hasMystical:
            text += " 神秘"
        return text

    def make_gu_text(self):
        text = ''
        if self.equipType == 0:
            text += "NONE"
            return text
        text += all_equip["data"][self.partsText][self.equipType - 1]
        text += " "
        text += self.level
        text += " "
        text += self.attr0
        text += " "
        text += self.attr1
        text += " "
        text += self.attr2
        text += " "
        text += self.attr3
        text += " "
        text += str(self.hasMystical)
        return text


class weaponEquip(equip):
    partsText = "weapon"

    def __init__(self, level, attr0, attr1, attr2, attr3, hasMystical, weaponType):
        super(weaponEquip, self).__init__(level, attr0, attr1, attr2, attr3, hasMystical, weaponType)


class gloveEquip(equip):
    partsText = "glove"

    def __init__(self, level, attr0, attr1, attr2, attr3, hasMystical, gloveType):
        super(gloveEquip, self).__init__(level, attr0, attr1, attr2, attr3, hasMystical, gloveType)


class ArmorEquip(equip):
    partsText = "Armor"

    def __init__(self, level, attr0, attr1, attr2, attr3, hasMystical, ArmorType):
        super(ArmorEquip, self).__init__(level, attr0, attr1, attr2, attr3, hasMystical, ArmorType)


class helmetEquip(equip):
    partsText = "helmet"

    def __init__(self, level, attr0, attr1, attr2, attr3, hasMystical, helmetType):
        super(helmetEquip, self).__init__(level, attr0, attr1, attr2, attr3, hasMystical, helmetType)


class EQUIPSet:
    def __init__(self, weapon=None, glove=None, Armor=None, helmet=None):
        self.weapon = weapon
        self.glove = glove
        self.Armor = Armor
        self.helmet = helmet

    def make_gu_text(self):
        text = ''
        text += self.weapon.make_gu_text()
        text += "\n"
        text += self.glove.make_gu_text()
        text += "\n"
        text += self.Armor.make_gu_text()
        text += "\n"
        text += self.helmet.make_gu_text()
        return text


class skill:
    def __init__(self, data):
        self.data = data


class SKILLSet:
    def __init__(self, skill_1, skill_2, skill_3, skill_4):
        self.skill_1 = skill_1
        self.skill_2 = skill_2
        self.skill_3 = skill_3
        self.skill_4 = skill_4

    def make_gu_text(self):
        text = ""
        num = 0
        if self.skill_1.data != 0:
            text += all_skill["data"][self.skill_1.data - 1]
            text += " "
            num += 1
        if self.skill_2.data != 0:
            text += all_skill["data"][self.skill_2.data - 1]
            text += " "
            num += 1
        if self.skill_3.data != 0:
            text += all_skill["data"][self.skill_3.data - 1]
            text += " "
            num += 1
        if self.skill_4.data != 0:
            text += all_skill["data"][self.skill_4.data - 1]
            num += 1
        text = str(num) + " " + text
        return text

    def make_gu_npc_text(self):
        text = ""
        if self.skill_1.data != 0:
            text += "_"
            text += all_skill["data"][self.skill_1.data - 1]
        if self.skill_2.data != 0:
            text += "_"
            text += all_skill["data"][self.skill_2.data - 1]
        if self.skill_3.data != 0:
            text += "_"
            text += all_skill["data"][self.skill_3.data - 1]
        if self.skill_4.data == len(all_skill["name"]) + 1:
            text += "_"
            text += "RAND"
        elif self.skill_4.data != 0:
            text += "_"
            text += all_skill["data"][self.skill_4.data - 1]
        return text

    def toString(self):
        text = ""
        if self.skill_1.data != 0:
            text += "_"
            text += all_skill["name"][self.skill_1.data - 1]
        if self.skill_2.data != 0:
            text += "_"
            text += all_skill["name"][self.skill_2.data - 1]
        if self.skill_3.data != 0:
            text += "_"
            text += all_skill["name"][self.skill_3.data - 1]
        if self.skill_4.data != 0:
            text += "_"
            text += all_skill["name"][self.skill_4.data - 1]
        return text


class WishSet:
    def __init__(self, wishLevelList):
        self.wishLevelList = wishLevelList

    def make_gu_text(self):
        text = "WISH "
        for i in range(len(self.wishLevelList)):
            text += str(self.wishLevelList[i]) + " "
        return text

    def getWishLevelList(self):
        return self.wishLevelList.copy()


class amuletClass:
    def __init__(self, amuletLevelList):
        if len(amuletLevelList) != len(all_amulet["data"]):
            self.amuletLevelList = [0] * len(all_amulet["data"])
        else:
            self.amuletLevelList = amuletLevelList

    def make_gu_text(self):
        text = "AMULET "
        for i in range(len(self.amuletLevelList)):
            if self.amuletLevelList[i] > 0:
                name = all_amulet["data"][i]
                text += name + " " + str(self.amuletLevelList[i]) + " "
        return text + "ENDAMULET"

    def getAmuletLevelList(self):
        return self.amuletLevelList.copy()
