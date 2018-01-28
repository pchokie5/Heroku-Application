from bertrand import pages
from ._builtin import Bot


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.MyPage)
        yield (pages.Results)
