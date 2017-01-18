import random
from prettytable import PrettyTable


class RPS():

    game_choices = ["rock", "paper", "scissors"]
    dict_victor = {"key_user": "player",
                   "key_comp": "computer",
                   "key_tied": "nobody"}

    def __init__(self, user_wins=0, comp_wins=0, ties=0):
        self.user_wins = user_wins
        self.comp_wins = comp_wins
        self.ties = ties

    def user_won(self):
        self.user_wins += 1

    def comp_won(self):
        self.comp_wins += 1

    def tied(self):
        self.ties += 1

    def computer_choose(self):
        return random.choice(self.game_choices)

    def play(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            self.tied()
            winner = self.dict_victor.get("key_tied")
        elif player_choice == "rock" and computer_choice == "scissors":
            self.user_won()
            winner = self.dict_victor.get("key_user")
        elif player_choice == "scissors" and computer_choice == "paper":
            self.user_won()
            winner = self.dict_victor.get("key_user")
        elif player_choice == "paper" and computer_choice == "rock":
            self.user_won()
            winner = self.dict_victor.get("key_user")
        else:
            self.comp_won()
            winner = self.dict_victor.get("key_comp")
        return winner

    def result_of(self, player_choice, computer_choice, winner):
        if winner == self.dict_victor.get("key_user"):
            result = "Player Wins!    "
        elif winner == self.dict_victor.get("key_comp"):
            result = "Computer Wins :("
        elif winner == self.dict_victor.get("key_tied"):
            result = "It's a tie.     "
        else:
            pass
        t = PrettyTable(["Column1", "Column2"])
        t.header = False
        t.border = True
        t.format = True
        t.align = "l"
        t.add_row(["Player threw", player_choice])
        t.add_row(["Computer threw", computer_choice])
        t.add_row(["Result", result])
        return t.get_html_string(border=True)

    def results_total(self):
        t = PrettyTable(["Column1", "Column2"])
        t.header = False
        t.border = True
        t.format = True
        t.align = "l"
        t.add_row(["Player Wins", self.user_wins])
        t.add_row(["Computer Wins", self.comp_wins])
        t.add_row(["Ties", self.ties])
        return t.get_html_string(border=True)
