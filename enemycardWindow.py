import re

import global_env
from cardClass import enemyCard
from cardWindow import Ui_cardForm, QInputDialog


class Ui_enemycardForm(Ui_cardForm):
    def setupUi(self, Form):
        self.cardList = global_env.enemyCardList
        self.cardClass = enemyCard
        super().setupUi(Form)

    def retranslateUi(self, Form):
        super().retranslateUi(Form)
        Form.setWindowTitle("敌方卡片")
        self.cardlistlabel.setText("敌方卡片")
        self.toggleSTATButton.show()
        self.nicknamelabel.show()
        self.nicknamelineEdit.show()

    def cacloutputFun(self, text=None):
        if not self.ableCheck():
            return

        thiscard = self.makeMyCard()
        thistext = thiscard.make_gu_text()
        halo = thiscard.halo
        thistext = str(halo) + "\n" + thistext
        QInputDialog.getMultiLineText(self, '请复制', "", thistext)


'''    def allImportFun(self, text=None):
        if text is None:
            text, ok = QInputDialog.getMultiLineText(self, '导入光环、卡片、装备、技能', '咕咕镇计算器格式')
            if not (ok and text):
                return

        text = re.sub(r"\n\n", "\n", text)
        text = text.split("\n")
        text0 = text[0].split(" ")
        if (len(text0) == 1):
            self.halolineEdit.setText(text[0])
        else:
            text.insert(0, "")
        self.cardImportFun(text[1] + "\n" + text[2])
        self.equipImportFun(text[3] + "\n" + text[4] + "\n" + text[5] + "\n" + text[6])
        self.skillImportFun(text[7])'''


