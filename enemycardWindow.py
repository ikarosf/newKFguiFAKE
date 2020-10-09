import global_env
from cardClass import enemyCard
from cardWindow import Ui_cardForm


class Ui_enemycardForm(Ui_cardForm):
    def setupUi(self, Form):
        self.cardList = global_env.enemyCardList
        self.cardClass = enemyCard
        super().setupUi(Form)

    def retranslateUi(self,Form):
        super().retranslateUi(Form)
        Form.setWindowTitle("敌方卡片")
        self.cardlistlabel.setText("敌方卡片")
        self.toggleSTATButton.show()
        self.nicknamelabel.show()
        self.nicknamelineEdit.show()

