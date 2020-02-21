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
             "破壁之心", "破魔之心",
             "伤口恶化", "精神创伤", "铁甲尖刺",
             "沸血之志", "波澜不惊", "飓风之力"],

    "data": ["SHI", "XIN", "FENG",
             "BI", "MO",
             "SHANG", "SHEN", "CI",
             "FEI", "BO", "JU"
             ]
}

all_character = {
    "name": ["琳", "默", "艾", "梦"],
    "data": ["LIN", "MO", "AI", "MENG"]
}

all_npc = {
    "name": ["木人", "迅捷蛛", "魔灯", "食铁兽"],
    "data": ["MU", "ZHU", "DENG", "SHOU"]
}

all_equip = {
    "name": {
        "weapon": ["剑", "短弓", "短杖", "荣誉之刃"],
        "glove": ["手套", "手环"],
        "Armor": ["铁甲", "皮甲", "布甲", "灵光袍", "荆棘重甲"],
        "helmet": ["头巾"],
    },
    "data": {
        "weapon": ["SWORD", "BOW", "STAFF", "BLADE"],
        "glove": ["GLOVES", "BRACELET"],
        "Armor": ["PLATE", "LEATHER", "CLOTH", "CLOAK", "THORN"],
        "helmet": ["SCARF"],
    }
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


class weaponEquip(equip):
    partsText = "weapon"

    def __init__(self, level, attr0, attr1, attr2, attr3, hasMystical, weaponType):
        super(weaponEquip, self).__init__(level, attr0, attr1, attr2, attr3, hasMystical, weaponType)
        self.weaponType = weaponType

    def make_gu_text(self):
        text = ''
        if self.weaponType == 0:
            text += "NONE"
            return text
        text += all_equip["data"]["weapon"][self.weaponType - 1]
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


class gloveEquip(equip):
    partsText = "glove"

    def __init__(self, level, attr0, attr1, attr2, attr3, hasMystical, gloveType):
        super(gloveEquip, self).__init__(level, attr0, attr1, attr2, attr3, hasMystical, gloveType)
        self.gloveType = gloveType

    def make_gu_text(self):
        text = ''
        if self.gloveType == 0:
            text += "NONE"
            return text
        text += all_equip["data"]["glove"][self.gloveType - 1]
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


class ArmorEquip(equip):
    partsText = "Armor"

    def __init__(self, level, attr0, attr1, attr2, attr3, hasMystical, ArmorType):
        super(ArmorEquip, self).__init__(level, attr0, attr1, attr2, attr3, hasMystical, ArmorType)
        self.ArmorType = ArmorType

    def make_gu_text(self):
        text = ''
        if self.ArmorType == 0:
            text += "NONE"
            return text
        text += all_equip["data"]["Armor"][self.ArmorType - 1]
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


class helmetEquip(equip):
    partsText = "helmet"

    def __init__(self, level, attr0, attr1, attr2, attr3, hasMystical, helmetType):
        super(helmetEquip, self).__init__(level, attr0, attr1, attr2, attr3, hasMystical, helmetType)
        self.helmetType = helmetType

    def make_gu_text(self):
        text = ''
        if self.helmetType == 0:
            text += "NONE"
            return text
        text += all_equip["data"]["helmet"][self.helmetType - 1]
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
        if self.skill_4.data != 0:
            text += "_"
            text += all_skill["data"][self.skill_4.data - 1]
        return text
