#!/usr/bin/python
import os
import random
import sys
from prettytable import PrettyTable


# Variables
game_choices = ["rock", "paper", "scissors"]
total_wins = 0
total_losses = 0
total_ties = 0


def text_banner():
    t = PrettyTable(['Column1'])
    t.header = False
    t.add_row([""])
    t.add_row(["  Welcome to a game of Rock, Paper, Scissors!  "])
    t.add_row([""])
    print(t)


def text_help():
    t = PrettyTable(['Game Options'])
    t.align = 'l'
    t.add_row(["Enter r/rock to play Rock"])
    t.add_row(["Enter p/paper to play Paper"])
    t.add_row(["Enter s/scissors to play Scissors"])
    t.add_row(["Enter h/help for help options"])
    t.add_row(["Enter t/total for all match results"])
    t.add_row(["Enter q/quit to exit"])
    t.add_row(["                                               "])
    print(t)


def text_game_over():
    t = PrettyTable(['Column1'])
    t.header = False
    t.align = 'c'
    t.add_row([""])
    t.add_row(["Thank you for playing!"])
    t.add_row(["                                               "])
    print(t)
    print("")
    print("Final Results are:")
    results_total()


def get_input():
    player_input = raw_input("Enter your choice: ")
    player_input = player_input.lower()
    if player_input == "r":
        player_input = "rock"
    if player_input == "p":
        player_input = "paper"
    if player_input == "s":
        player_input = "scissors"
    validate_player_input(player_input)
    return player_input


def validate_player_input(throw):
    if throw in game_choices:
        return
    elif (throw == "q") or (throw == "quit"):
        text_game_over()
        sys.exit(0)
    elif (throw == "t") or (throw == "total"):
        results_total()
        return
    elif (throw == "h") or (throw == "help"):
        text_help()
        return
    else:
        print("Bad input.  Try again please.")
        return None


def computer_choose():
    return game_choices[random.randint(0, 2)]


def play(player_choice, computer_choice):
    winner = "computer"
    if player_choice == computer_choice:
        winner = "tie"
        result = "It's a tie.     "
    elif player_choice == "rock" and computer_choice == "scissors":
        winner = "player"
        result = "Player Wins!    "
    elif player_choice == "scissors" and computer_choice == "paper":
        winner = "player"
        result = "Player Wins!    "
    elif player_choice == "paper" and computer_choice == "rock":
        winner = "player"
        result = "Player Wins!    "
    else:
        result = "Computer Wins :("
    results_match(player_choice, computer_choice, result)
    tally(winner)


def tally(who_won):
    global total_wins
    global total_losses
    global total_ties
    if who_won == 'player':
        total_wins += 1
    if who_won == 'computer':
        total_losses += 1
    if who_won == 'tie':
        total_ties += 1


def results_match(player_choice, computer_choice, result):
    t = PrettyTable(['Column1', 'Column2'])
    t.header = False
    t.align = 'l'
    t.add_row(["Player threw", player_choice])
    t.add_row(["Computer threw", computer_choice])
    t.add_row(["Result", result])
    print(t)


def results_total():
    global total_wins
    global total_losses
    global total_ties
    t = PrettyTable(['Column1', 'Column2'])
    t.header = False
    t.align = 'l'
    t.add_row(["Player Wins", total_wins])
    t.add_row(["Computer Wins", total_losses])
    t.add_row(["Ties", total_ties])
    print(t)


if __name__ == "__main__":
    try:
        os.system("clear")
        text_banner()
        text_help()
        if sys.version[0] == "3":
            raw_input = input
        while True:
            my_choice = get_input()
            while my_choice not in game_choices:
                my_choice = get_input()
            computer_choice = computer_choose()
            play(my_choice, computer_choice)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        sys.exit(1)
