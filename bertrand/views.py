from bertrand import models
from ._builtin import Page, WaitPage


# class AssignRoles(Page):
#  def after_all_players_arrive(self):
#     self.player.role()

class Instructions(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    pass

class MTask1(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    pass


class Cog1OUT(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    pass


class Amb1(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    form_model = models.Player
    form_fields = ["ambiguity1"]


class Cog1IN(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    form_model = models.Player
    form_fields = ["cog1"]

class MTask2(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    pass


class Cog2OUT(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    pass


class Amb2(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    form_model = models.Player
    form_fields = ["ambiguity2"]


class Cog2IN(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    form_model = models.Player
    form_fields = ["cog2"]

class MTask3(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    pass


class Cog3OUT(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    pass


class Red1(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    form_model = models.Player
    form_fields = ["reduction1"]


class Cog3IN(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    form_model = models.Player
    form_fields = ["cog3"]

class MTask4(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    pass


class Cog4OUT(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    pass


class Amb1m(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    form_model = models.Player
    form_fields = ["ambiguity1m"]


class Cog4IN(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    form_model = models.Player
    form_fields = ["cog4"]

class MTask5(Page):
        def is_displayed(self):
            return self.player.id_in_group > 0

        pass


class Cog5OUT(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    pass


class Amb2m(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    form_model = models.Player
    form_fields = ["ambiguity2m"]


class Cog5IN(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    form_model = models.Player
    form_fields = ["cog5"]

class MTask6(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    pass


class Cog6OUT(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    pass


class Red1m(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    form_model = models.Player
    form_fields = ["reduction1m"]


class Cog6IN(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    form_model = models.Player
    form_fields = ["cog6"]


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Draws(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = models.Group
    form_fields = ["amb1A_WIN", "amb1B_WIN", "amb2A_WIN", "amb2B_WIN", "red1A_WIN", "red1B_WIN", "amb1mA_WIN",
                   "amb1mB_WIN", "amb2mA_WIN", "amb2mB_WIN", "red1mA_WIN", "red1mB_WIN"]


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class ResultsCalculation(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    def before_next_page(self):
        self.player.check_cog()
        self.player.check_choices()
        self.player.calculate_payout()

    pass


class Results(Page):
    def is_displayed(self):
        return self.player.id_in_group > 0

    pass


page_sequence = [
    #  AssignRoles,
    Instructions,
    MTask1,
    Cog1OUT,
    Amb1,
    Cog1IN,
    MTask2,
    Cog2OUT,
    Amb2,
    Cog2IN,
    MTask3,
    Cog3OUT,
    Red1,
    Cog3IN,
    MTask4,
    Cog4OUT,
    Amb1m,
    Cog4IN,
    MTask5,
    Cog5OUT,
    Amb2m,
    Cog5IN,
    MTask6,
    Cog6OUT,
    Red1m,
    Cog6IN,
    ResultsWaitPage,
    Draws,
    ResultsWaitPage,
    ResultsCalculation,
    Results
]