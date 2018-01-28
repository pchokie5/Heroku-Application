
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
author = 'Peter Coiley'

doc = """
Survey Questions for the Experiment
"""


class Constants(BaseConstants):
    name_in_url = 'survey_two_decoy'
    players_per_group = None
    num_rounds = 1
    num_choices = 8
    

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.reward_field = random.randint(1, 8)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    reward_field = models.IntegerField()
    reward_answer = models.StringField()

    Menu_1 = models.StringField(
        initial = None,
        choices = ['4 dollars, 6 godiva chocolates',
                '6 dollars, 3 godiva chocolates'],
        verbose_name= '1st Round',
        widget= widgets.RadioSelect()
    )

    Menu_2 = models.StringField(
        initial = None,
        choices = ['6 dollars, 3 godiva chocolates',
                   '4 dollars, 6 godiva chocolates',
               '4 dollars and 5 godiva chocolates'],
        verbose_name= '2nd Round',
        widget = widgets.RadioSelect()
    )
    Menu_3 = models.StringField(
        initial = None,
        choices = ['4 dollars, 6 godiva chocolates',
                   '6 dollars, 3 godiva chocolates',
                   '5 dollars, 3 godiva chocolates'],
        verbose_name = '3rd Round',
        widget = widgets.RadioSelect()

    )
    Menu_4 = models.StringField(
        initial = None,
        choices = ['4 dollars, 6 godiva chocolates',
                   '0 dollars, 10 godiva chocolates',
                   '6 dollars, 3 godiva chocolates'],
        verbose_name= '4th Round',
        widget = widgets.RadioSelect
    )
    Menu_5 = models.StringField(
        initial = None,
        choices = ['4 dollars, 6 godiva chocolates',
                   '6 dollars, 3 godiva chocolates',
                   '7 dollars, 0 godiva chocolates'],
        verbose_name= '5th Round',
        widget = widgets.RadioSelect
    )
    Menu_6 = models.StringField(
        initial= None,
        choices = ['4 dollars, 6 godiva chocolates',
                   '4 dollars, 5 godiva chocolates',
                   '6 dollars, 3 godiva chocolates',
                   '5 dollars, 3 godiva chocolates'],
        verbose_name = '6th Round',
        widget = widgets.RadioSelect()
    )
    Menu_7 = models.StringField(
        initial = None,
        choices = ['4 dollars, 6 godiva chocolates',
                   '0 dollars, 10 godiva chocolates',
                   '6 dollars, 3 godiva chocolates',
                   '7 dollars, 0 godiva chocolates'],
        verbose_name = '7th Round',
        widget = widgets.RadioSelect()
    )
    Menu_8 = models.StringField(
        initial= None,
        choices= ['4 dollars, 6 godiva chocolates',
                  '6 dollars, 3 godiva chocolates',
                  '4 dollars, 3 godiva chocolates'],
        verbose_name='8th Round',
        widget = widgets.RadioSelect()

    )