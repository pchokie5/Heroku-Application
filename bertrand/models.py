from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Peter Duersch'

doc = """
Your app description
"""
import random
random.seed()

class Constants(BaseConstants):
    name_in_url = 'cogload1'
    players_per_group = None
    num_rounds = 1
    cpayoff = c(100)  # base payoff for choice tasks
    Dcpayoff = cpayoff * 2  # Double payoff for choice tasks, should be set to cpayoff*2
    mpayoff = c(10)  # payoff for memory tasks
    zeropayoff = c(0)  # zero payoff/alt payoff for choice tasks
    markuppayoff = c(0.1)  # markup payoff for second choice
    cog1DEF = random.randint(10,99)  # memorystring 1
    cog2DEF = random.randint(10,99)
    cog3DEF = random.randint(10,99)
    cog4DEF = random.randint(10,99)
    cog5DEF = random.randint(10,99)
    cog6DEF = random.randint(10,99)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    amb1A_WIN = models.PositiveIntegerField(
        widget=widgets.Slider(),
        verbose_name="Did the draw for amb1A win?",
        min=0,
        max=1)
    amb1B_WIN = models.PositiveIntegerField(
        widget=widgets.Slider(),
        verbose_name="Did the draw for amb1B win?",
        min=0,
        max=1)
    amb2A_WIN = models.PositiveIntegerField(
        widget=widgets.Slider(),
        verbose_name="Did the draw for amb2A win?",
        min=0,
        max=1)
    amb2B_WIN = models.PositiveIntegerField(
        widget=widgets.Slider(),
        verbose_name="Did the draw for amb2B win?",
        min=0,
        max=1)
    red1A_WIN = models.PositiveIntegerField(
        widget=widgets.Slider(),
        verbose_name="Did the draw for red1A win?",
        min=0,
        max=1)
    red1B_WIN = models.PositiveIntegerField(
        widget=widgets.Slider(),
        verbose_name="Did the draw for red1B win?",
        min=0,
        max=1)
    amb1mA_WIN = models.PositiveIntegerField(
        widget=widgets.Slider(),
        verbose_name="Did the draw for amb1mA win?",
        min=0,
        max=1)
    amb1mB_WIN = models.PositiveIntegerField(
        widget=widgets.Slider(),
        verbose_name="Did the draw for amb1mB win?",
        min=0,
        max=1)
    amb2mA_WIN = models.PositiveIntegerField(
        widget=widgets.Slider(),
        verbose_name="Did the draw for amb2mA win?",
        min=0,
        max=1)
    amb2mB_WIN = models.PositiveIntegerField(
        widget=widgets.Slider(),
        verbose_name="Did the draw for amb2mB win?",
        min=0,
        max=1)
    red1mA_WIN = models.PositiveIntegerField(
        widget=widgets.Slider(),
        verbose_name="Did the draw for red1mA win?",
        min=0,
        max=1)
    red1mB_WIN = models.PositiveIntegerField(
        widget=widgets.Slider(),
        verbose_name="Did the draw for red1mB win?",
        min=0,
        max=1)


class Player(BasePlayer):
    ambiguity1 = models.StringField(
        choices=["A", "B"],
        # blank=True,
        widget=widgets.RadioSelect(),
        verbose_name="Which option do you choose?",
        doc="ambiguity 1 A or B"
    )
    ambiguity2 = models.StringField(
        choices=["A", "B"],
        # blank=True,
        widget=widgets.RadioSelect(),
        verbose_name="Which option do you choose?",
        doc="ambiguity 2 A or B"
    )
    reduction1 = models.StringField(
        choices=["A", "B"],
        # blank=True,
        widget=widgets.RadioSelect(),
        verbose_name="Which option do you choose?",
        doc="reduction1 1 A or B"
    )
    ambiguity1m = models.StringField(
        choices=["A", "B"],
        # blank=True,
        widget=widgets.RadioSelect(),
        verbose_name="Which option do you choose?",
        doc="ambiguity 1m A or B"
    )
    ambiguity2m = models.StringField(
        choices=["A", "B"],
        # blank=True,
        widget=widgets.RadioSelect(),
        verbose_name="Which option do you choose?",
        doc="ambiguity 2m A or B"
    )
    reduction1m = models.StringField(
        choices=["A", "B"],
        # blank=True,
        widget=widgets.RadioSelect(),
        verbose_name="Which option do you choose?",
        doc="reduction 1m A or B"
    )
    cog1 = models.StringField(
        verbose_name="What was the sequence you had to remember?",
        doc="cognitive entry 1"
    )
    cog2 = models.StringField(
        verbose_name="What was the sequence you had to remember?",
        doc="cognitive entry 2"
    )
    cog3 = models.StringField(
        verbose_name="What was the sequence you had to remember?",
        doc="cognitive entry 3"
    )
    cog4 = models.StringField(
        verbose_name="What was the sequence you had to remember?",
        doc="cognitive entry 4"
    )
    cog5 = models.StringField(
        verbose_name="What was the sequence you had to remember?",
        doc="cognitive entry 5"
    )
    cog6 = models.StringField(
        verbose_name="What was the sequence you had to remember?",
        doc="cognitive entry 6"
    )
    amb1A_chosen = models.PositiveIntegerField()
    amb2A_chosen = models.PositiveIntegerField()
    red1A_chosen = models.PositiveIntegerField()
    red1mA_chosen = models.PositiveIntegerField()
    amb1B_chosen = models.PositiveIntegerField()
    amb2B_chosen = models.PositiveIntegerField()
    red1B_chosen = models.PositiveIntegerField()
    red1mB_chosen = models.PositiveIntegerField()
    amb1mA_chosen = models.PositiveIntegerField()
    amb2mA_chosen = models.PositiveIntegerField()
    amb1mB_chosen = models.PositiveIntegerField()
    amb2mB_chosen = models.PositiveIntegerField()
    cog1right = models.PositiveIntegerField()
    cog2right = models.PositiveIntegerField()
    cog3right = models.PositiveIntegerField()
    cog4right = models.PositiveIntegerField()
    cog5right = models.PositiveIntegerField()
    cog6right = models.PositiveIntegerField()
    payout = models.FloatField()

    def role(self):  # defines player role
        if self.id_in_group == 1:
            return "experimenter"
        else:
            return "subject"

    def check_cog(self):  # Checks for correctly remembered memory task 1
        if self.cog1 == Constants.cog1DEF:
            self.cog1right = 1
        else:
            self.cog1right = 0
        if self.cog2 == Constants.cog2DEF:
            self.cog2right = 1
        else:
            self.cog2right = 0
        if self.cog3 == Constants.cog3DEF:
            self.cog3right = 1
        else:
            self.cog3right = 0
        if self.cog4 == Constants.cog4DEF:
            self.cog4right = 1
        else:
            self.cog4right = 0
        if self.cog5 == Constants.cog5DEF:
            self.cog5right = 1
        else:
            self.cog5right = 0
        if self.cog6 == Constants.cog6DEF:
            self.cog6right = 1
        else:
            self.cog6right = 0

    def check_choices(self):  # transformes choice into dummy variables for easy payoff calculation
        if self.ambiguity1 == "A":
            self.amb1A_chosen = 1
            self.amb1B_chosen = 0
        else:
            self.amb1A_chosen = 0
            self.amb1B_chosen = 1
        if self.ambiguity2 == "A":
            self.amb2A_chosen = 1
            self.amb2B_chosen = 0
        else:
            self.amb2A_chosen = 0
            self.amb2B_chosen = 1
        if self.reduction1 == "A":
            self.red1A_chosen = 1
            self.red1B_chosen = 0
        else:
            self.red1A_chosen = 0
            self.red1B_chosen = 1
        if self.ambiguity1m == "A":
            self.amb1mA_chosen = 1
            self.amb1mB_chosen = 0
        else:
            self.amb1mA_chosen = 0
            self.amb1mB_chosen = 1
        if self.ambiguity2m == "A":
            self.amb2mA_chosen = 1
            self.amb2mB_chosen = 0
        else:
            self.amb2mA_chosen = 0
            self.amb2mB_chosen = 1
        if self.reduction1m == "A":
            self.red1mA_chosen = 1
            self.red1mB_chosen = 0
        else:
            self.red1mA_chosen = 0
            self.red1mB_chosen = 1

    def calculate_payout(self):  # still needs to be adjusted to mirrored
        self.payout = ((self.amb1A_chosen * self.group.amb1A_WIN * Constants.cpayoff) + (self.amb1B_chosen * (
        self.group.amb1B_WIN * Constants.cpayoff + Constants.markuppayoff)) + self.cog1right * Constants.mpayoff) + (
                      (self.amb2A_chosen * self.group.amb2A_WIN * Constants.cpayoff) + (self.amb2B_chosen * (
                      self.group.amb2B_WIN * Constants.cpayoff + Constants.markuppayoff)) + self.cog2right * Constants.mpayoff) + (
                      (self.red1A_chosen * self.group.red1A_WIN * Constants.cpayoff) + (self.red1B_chosen * (
                      self.group.red1B_WIN * Constants.cpayoff + Constants.markuppayoff)) + self.cog3right * Constants.mpayoff) + (
                      (self.amb1mA_chosen * (self.group.amb1mA_WIN * Constants.cpayoff + Constants.markuppayoff) + (
                      self.amb1mB_chosen * self.group.amb1mB_WIN * Constants.cpayoff) + self.cog4right * Constants.mpayoff) + (
                      (self.amb2mA_chosen * (self.group.amb2mA_WIN * Constants.cpayoff + Constants.markuppayoff)) + (
                      self.amb2mB_chosen * self.group.amb2mB_WIN * Constants.cpayoff) + self.cog5right * Constants.mpayoff) + (
                      (self.red1mA_chosen * (self.group.red1mA_WIN * Constants.cpayoff + Constants.markuppayoff)) + (
                      self.red1mB_chosen * self.group.red1mB_WIN * Constants.cpayoff) + self.cog6right * Constants.mpayoff))
        self.payoff = c(self.payout)
