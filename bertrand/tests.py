from bertrand import views
from ._builtin import Bot


class PlayerBot(Bot):

    def play_round(self):
        yield (views.MyPage)
        yield (views.Results)
