from SystemClass import all_character


class card:
    def __init__(self, halo, character, level, attrSet, sklSlot, skillSet, equipSet):
        self.halo = halo
        self.character = character
        self.level = level
        self.attrSet = attrSet
        self.sklSlot = sklSlot
        self.skillSet = skillSet
        self.equipSet = equipSet

    def tostring(self):
        text = ''
        text += all_character['name'][self.character]
        text += " LV:"
        text += self.level
        text += " "
        text += self.attrSet.tostring()
        return text


class myCard(card):
    def __init__(self, halo, character, level, attrSet, sklSlot, skillSet, equipSet):
        super(myCard, self).__init__(halo, character, level, attrSet, sklSlot, skillSet, equipSet)

    def make_gu_text(self):
        text = ''
        text += self.halo
        text += "\n"
        text += all_character['data'][self.character]
        text += " "
        text += self.level
        text += " "
        text += str(self.sklSlot+1)
        text += "\n"
        text += self.attrSet.make_gu_text()
        text += "\n"
        text += self.equipSet.make_gu_text()
        text += "\n"
        text += self.skillSet.make_gu_text()
        return text


class enemyCard(card):
    def __init__(self, halo, character, level, attrSet, sklSlot, skillSet, equipSet):
        super(enemyCard, self).__init__(halo, character, level, attrSet, sklSlot, skillSet, equipSet)

    def make_gu_text(self):
        text = ''
        text += all_character['data'][self.character]
        text += " "
        text += self.level
        text += " "
        text += str(self.sklSlot+1)
        text += "\n"
        text += self.attrSet.make_gu_text()
        text += "\n"
        text += self.equipSet.make_gu_text()
        text += "\n"
        text += self.skillSet.make_gu_text()
        return text
