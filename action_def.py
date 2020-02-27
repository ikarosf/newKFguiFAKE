import os
import subprocess
import re

from PySide2.QtCore import QThread, Signal

import global_env
from SystemClass import all_equip, weaponEquip, gloveEquip, ArmorEquip, helmetEquip, EQUIPSet


# def execCmd(userarg="bnpc\nbpc"):
#     userarg = bytes(userarg, encoding="utf8")
#     # cmd = os.path.join(".", "newkf.exe")
#     cmd = global_env.saveData["setting"]["exeDir"]
#     if cmd == None:
#         cmd = os.path.join(".", "newkf.exe")
#     if not os.path.isfile(cmd):
#         return ["找不到newkf.exe"]
#     p1 = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     # p2=subprocess.Popen('bnpc',shell=True,stdin=p1.stdout,stdout=subprocess.PIPE)
#     (stdoutdata, stderrdata) = p1.communicate(userarg)
#     p1.wait()
#     mystr = str(stdoutdata, encoding="utf8")
#     result_list = re.findall(r'<NPCType> <Level> <Power>(.*?)Number of threads', mystr, re.S)
#     if len(result_list) == 0:
#         return [mystr]
#     # print(mystr)
#     # writeFile("mylog", mystr)
#     # return stdoutdata
#     return result_list


def execCmdReturn(userarg="bnpc\nbpc"):
    userarg = bytes(userarg, encoding="utf8")
    # cmd = os.path.join(".", "newkf.exe")
    cmd = global_env.saveData["setting"]["exeDir"]
    if cmd == None:
        cmd = os.path.join(".", "newkf.exe")
    if not os.path.isfile(cmd):
        return ["找不到newkf.exe"]

    p1 = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # p2=subprocess.Popen('bnpc',shell=True,stdin=p1.stdout,stdout=subprocess.PIPE)
    (stdoutdata, stderrdata) = p1.communicate(userarg)
    # p1.wait()
    mystr = str(stdoutdata, encoding="utf8")
    result_list = re.findall(r'<NPCType> <Level> <Power>(.*?)Number of threads', mystr, re.S)
    if len(result_list) == 0:
        return False, mystr
    # print(mystr)
    # writeFile("mylog", mystr)
    # return stdoutdata
    return True, result_list


class execCmdWorker(QThread):
    my_signal = Signal(str)

    def __init__(self, parent=None, item=None):
        super().__init__(parent)
        self.item = item

    def run(self):
        result, text = execCmdReturn(self.item)
        if not result:
            self.my_signal.emit(text)
        else:
            thisText = ""
            for i in text:
                thisText += i
            self.my_signal.emit(thisText)


def after_calculate(text):
    global_env.mainWin.textBrowser.setText(text)
    global_env.mainWin.enable_all_button()


def before_calculate():
    global_env.mainWin.textBrowser.setText("计算中")
    global_env.mainWin.disable_all_button()


def text_to_equipSet(text):
    text = re.sub(r"\t+(\n|$)", "\n", text)
    text = re.sub(r"\n\n", "\n", text)
    equip_set_list = re.findall(r"(武器|手套|护甲|头盔)\n(.*?)\n(.*?)\n(.*?)(\n\[神秘属性\].*)?(\n|$)", text)
    equip_list = []
    for index, equipClass in enumerate([weaponEquip, gloveEquip, ArmorEquip, helmetEquip]):
        level_text = equip_set_list[index][2]
        level = re.match(r"Lv\.(\d+)", level_text).group(1)
        attr_text = equip_set_list[index][3]
        attrSet = re.findall(r"(\d+)%\s\w+\s\d+%?", attr_text)
        typeText = equip_set_list[index][1]
        hasMystical = 0
        if equip_set_list[index][4] != "":
            hasMystical = 1
        equipType = 0
        for i in range(len(all_equip['name'][equipClass.partsText])):
            if all_equip['name'][equipClass.partsText][i] in typeText:
                equipType = i + 1
        thisEquip = equipClass(level, attrSet[0], attrSet[1], attrSet[2], attrSet[3], hasMystical, equipType)
        equip_list.append(thisEquip)
    return EQUIPSet(equip_list[0], equip_list[1], equip_list[2], equip_list[3])


def make_full_gu_text(myCard, npcList=[], enemyCardList=[], gearList=[]):
    # gearList = []
    # gearList.append(global_env.equipStorageDict["weapon"]["短杖 LV.500"])
    text = ""
    text += myCard.make_gu_text()
    text += "\n"
    text += "NPC\n"
    for i in npcList:
        text += i.make_gu_text()
        text += "\n"
    text += "ENDNPC\n"
    text += "\n"

    text += "PC\n"
    for i in enemyCardList:
        text += i.make_gu_text()
        text += '\n'
    text += "ENDPC\n"

    text += "GEAR\n"
    for i in gearList:
        text += i.make_gu_text()
        text += '\n'
    text += "ENDGEAR\n"

    text += "THREADS " + str(global_env.threads) + "\n"
    text += "TESTS " + str(global_env.tests) + "\n"
    return text
