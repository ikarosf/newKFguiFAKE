from SystemClass import all_character


class card:
    def __init__(self, halo, character, level, attrSet, sklSlot, skillSet, equipSet, nickname, quality):
        self.halo = halo
        self.character = character
        self.level = level
        self.attrSet = attrSet
        self.sklSlot = sklSlot
        self.skillSet = skillSet
        self.equipSet = equipSet
        self.quality = quality

    def tostring(self):
        text = ''
        text += all_character['name'][self.character]
        text += " LV:"
        text += self.level
        text += " "
        text += self.attrSet.tostring()
        return text


class myCard(card):
    def __init__(self, halo, character, level, attrSet, sklSlot, skillSet, equipSet, nickname, quality):
        super(myCard, self).__init__(halo, character, level, attrSet, sklSlot, skillSet, equipSet, nickname, quality)

    def make_gu_text(self):
        text = ''
        text += self.halo
        text += "\n"
        text += all_character['data'][self.character]
        text += " "
        text += self.level
        text += " "
        text += str(self.sklSlot + 1)
        text += " "
        text += str(self.quality)
        text += "\n"
        text += self.attrSet.make_gu_text()
        text += "\n"
        text += self.equipSet.make_gu_text()
        text += "\n"
        text += self.skillSet.make_gu_text()
        return text


class enemyCard(card):
    def __init__(self, halo, character, level, attrSet, sklSlot, skillSet, equipSet, nickname, quality):
        super(enemyCard, self).__init__(halo, character, level, attrSet, sklSlot, skillSet, equipSet, nickname, quality)
        self.nickname = nickname

    def make_gu_text(self):
        text = ''
        text += all_character['data'][self.character]
        if self.nickname != "":
            text += "_" + self.nickname
        text += " "
        text += self.level
        text += " "
        text += str(self.sklSlot + 1)
        text += " "
        text += str(self.quality)
        text += "\n"
        text += self.attrSet.make_gu_text()
        text += "\n"
        text += self.equipSet.make_gu_text()
        text += "\n"
        text += self.skillSet.make_gu_text()
        return text

    def tostring(self):
        if self.nickname != "":
            return self.nickname
        else:
            text = super(enemyCard, self).tostring()
            return text


class STATCard:
    def __init__(self, cardType, attrs1, attrs2, attrs3, attrs4, attrs5, nickname):
        self.cardType = cardType
        self.attrs1 = attrs1
        self.attrs2 = attrs2
        self.attrs3 = attrs3
        self.attrs4 = attrs4
        self.attrs5 = attrs5
        self.nickname = nickname

    def make_gu_text(self):
        text = ''
        text += all_character['data'][self.cardType]
        if self.nickname != "":
            text += "_" + self.nickname
        text += " "
        text += "STAT"
        text += "\n"
        text += " ".join(str(i) for i in self.attrs1)
        text += "\n"
        text += " ".join(str(i) for i in self.attrs2)
        text += "\n"
        text += " ".join(str(i) for i in self.attrs3)
        text += "\n"
        text += " ".join(str(i) for i in self.attrs4)
        text += "\n"
        text += " ".join(str(i) for i in self.attrs5)
        return text

    def tostring(self):
        if self.nickname != "":
            return self.nickname
        text = ''
        text += all_character['name'][self.cardType]
        text += " STAT "
        text += " AD:"
        text += str(self.attrs1[0])
        text += " SPEED:"
        text += str(self.attrs2[0])
        text += " SHIED:"
        text += str(self.attrs3[3])
        text += " MAXHP:"
        text += str(self.attrs3[0])
        return text
