from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class FirstDecision(Page):
    form_model= models.Player
    form_fields = ['Menu_1']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class SecondDecision(Page):
    form_model= models.Player
    form_fields = ['Menu_2']


class Results(Page):
    pass

class ThirdDecision(Page):
    form_model = models.Player
    form_fields = ['Menu_3']

class FourthDecision(Page):
    form_model = models.Player
    form_fields = ['Menu_4']

class FifthDecision(Page):
    form_model = models.Player
    form_fields = ['Menu_5']

class SixthDecision(Page):
    form_model = models.Player
    form_fields = ['Menu_6']

class SeventhDecision(Page):
    form_model = models.Player
    form_fields = ['Menu_7']

class EighthDecision(Page):
    form_model = models.Player
    form_fields = ['Menu_8']

class ThankYou(Page):
    form_model = models.Player

page_sequence = [
    FirstDecision,
    SecondDecision,
    ThirdDecision,
    FourthDecision,
    FifthDecision,
    SixthDecision,
    SeventhDecision,
    EighthDecision,
    ThankYou
]
