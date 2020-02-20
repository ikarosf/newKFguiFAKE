from SystemClass import all_npc


class npc:
    def __init__(self, role, skillSet, level, highGain):
        self.role = role
        self.skillSet = skillSet
        self.level = level
        self.highGain = highGain

    def tostring(self):
        text = ''
        text += all_npc['name'][self.role]
        text += " LV:"
        text += self.level
        text += " 高收益："
        text += str(self.highGain)
        return text

    def make_gu_text(self):
        text = ""
        text += all_npc['data'][self.role]
        text += self.skillSet.make_gu_npc_text()
        text += " "
        text += self.level
        text += " "
        text += str(self.highGain)
        return text
