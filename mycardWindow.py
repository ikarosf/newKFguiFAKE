import global_env
from cardClass import myCard
from cardWindow import Ui_cardForm


class Ui_mycardForm(Ui_cardForm):
    def setupUi(self, Form):
        self.cardList = global_env.myCardList
        self.cardClass = myCard
        super().setupUi(Form)


