#!/usr/bin/python
import os
import random
import sys
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

    def __repr__(self):
        return "Won: {}; Loss: {}; Tied: {}".format(self.user_wins, self.comp_wins, self.ties)  # noqa: E501

    def computer_choose(self):
        return random.choice(self.game_choices)

    def get_input(self):
        player_input = raw_input("Enter your choice: ")
        player_input = player_input.lower()
        if player_input == "r":
            player_input = "rock"
        if player_input == "p":
            player_input = "paper"
        if player_input == "s":
            player_input = "scissors"
        self.validate_player_input(player_input)
        return player_input

    def validate_player_input(self, throw):
        if throw in self.game_choices:
            return
        elif (throw == "q") or (throw == "quit"):
            self.text_game_over()
            sys.exit(0)
        elif (throw == "t") or (throw == "total"):
            self.results_total()
            return
        elif (throw == "h") or (throw == "help"):
            self.text_help()
            return
        else:
            print("Bad input.  Try again please.")
            return None

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
            sys.exit(3)
        t = PrettyTable(["Column1", "Column2"])
        t.header = False
        t.align = "l"
        t.add_row(["Player threw", player_choice])
        t.add_row(["Computer threw", computer_choice])
        t.add_row(["Result", result])
        print(t)

    def results_total(self):
        t = PrettyTable(["Column1", "Column2"])
        t.header = False
        t.align = "l"
        t.add_row(["Player Wins", self.user_wins])
        t.add_row(["Computer Wins", self.comp_wins])
        t.add_row(["Ties", self.ties])
        print(t)

    def text_banner(self):
        t = PrettyTable(["Column1"])
        t.header = False
        t.add_row([""])
        t.add_row(["  Welcome to a game of Rock, Paper, Scissors!  "])
        t.add_row([""])
        print(t)

    def text_help(self):
        t = PrettyTable(["Game Options"])
        t.align = "l"
        t.add_row(["Enter r/rock to play Rock"])
        t.add_row(["Enter p/paper to play Paper"])
        t.add_row(["Enter s/scissors to play Scissors"])
        t.add_row(["Enter h/help for help options"])
        t.add_row(["Enter t/total for all match results"])
        t.add_row(["Enter q/quit to exit"])
        t.add_row(["                                               "])
        print(t)

    def text_game_over(self):
        t = PrettyTable(["Column1"])
        t.header = False
        t.align = "c"
        t.add_row([""])
        t.add_row(["Thank you for playing!"])
        t.add_row(["                                               "])
        print(t)
        print("")
        print("Final Results are:")
        self.results_total()


if __name__ == "__main__":
    try:
        os.system("clear")
        if sys.version[0] == "3":
            raw_input = input
        match = RPS()
        match.text_banner()
        match.text_help()
        while True:
            my_choice = match.get_input()
            while my_choice not in match.game_choices:
                my_choice = match.get_input()
            computer_choice = match.computer_choose()
            winner = match.play(my_choice, computer_choice)
            match.result_of(my_choice, computer_choice, winner)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        sys.exit(1)
