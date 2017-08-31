from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Zach Gilbert'

doc = """
Survey Questions for the Experiment
"""


class Constants(BaseConstants):
    name_in_url = 'survey_two_decoy'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):


    Menu_1 = models.CharField(
        initial = None,
        choices = ['4 dollars, 6 godiva chocolates',
                '6 dollars, 3 godiva chocolates'],
        verbose_name = 'Menu 1',
        widget= widgets.RadioSelect()
    )

    Menu_2 = models.CharField(
        initial = None,
        choices = ['6 dollars, 3 godiva chocolates',
                   '4 dollars, 6 godiva chocolates',
               '4 dollars and 5 godiva chocolates'],
        verbose_name= 'Menu 2',
        widget = widgets.RadioSelect()
    )
    Menu_3 = models.CharField(
        initial = None,
        choices = ['4 dollars, 6 godiva chocolates',
                   '6 dollars, 3 godiva chocolates',
                   '5 dollars, 3 godiva chocolates'],
        verbose_name = 'Menu 3',
        widget = widgets.RadioSelect()

    )
    Menu_4 = models.CharField(
        initial = None,
        choices = ['4 dollars, 6 godiva chocolates',
                   '0 dollars, 10 godiva chocolates',
                   '6 dollars, 3 godiva chocolates'],
        verbose_name= 'Menu 4',
        widget = widgets.RadioSelect
    )
    Menu_5 = models.CharField(
        initial = None,
        choices = ['4 dollars, 6 godiva chocolates',
                   '6 dollars, 3 godiva chocolates',
                   '7 dollars, 0 godiva chocolates'],
        verbose_name= 'Menu 5',
        widget = widgets.RadioSelect
    )
    Menu_6 = models.CharField(
        initial= None,
        choices = ['4 dollars, 6 godiva chocolates',
                   '4 dollars, 5 godiva chocolates',
                   '6 dollars, 3 godiva chocolates',
                   '5 dollars, 3 godiva chocolates'],
        verbose_name = 'Menu 6',
        widget = widgets.RadioSelect()
    )
    Menu_7 = models.CharField(
        initial = None,
        choices = ['4 dollars, 6 godiva chocolates',
                   '0 dollars, 10 godiva chocolates',
                   '6 dollars, 3 godiva chocolates',
                   '7 dollars, 0 godiva chocolates'],
        verbose_name = 'Menu 7',
        widget = widgets.RadioSelect()
    )
    Menu_8 = models.CharField(
        initial=None,
        choices= ['4 dollars, 6 godiva chocolates',
                  '6 dollars, 3 godiva chocolates',
                  '4 dollars, 3 godiva chocolates'],
        verbose_name='Menu 8',
        widget = widgets.RadioSelect()

    )