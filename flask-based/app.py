import random
import os
from flask import Flask, render_template, request
from prettytable import PrettyTable

# Variables
game_choices = ["rock", "paper", "scissors"]
total_wins = 0
total_losses = 0
total_ties = 0


def my_app():
    app = Flask(__name__)

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
        tally(winner)
        return results_match(player_choice, computer_choice, result)

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
        t.border = True
        t.format = True
        t.align = 'l'
        t.add_row(["Player threw", player_choice])
        t.add_row(["Computer threw", computer_choice])
        t.add_row(["Result", result])
        return t.get_html_string(border=True)

    def results_total():
        global total_wins
        global total_losses
        global total_ties
        t = PrettyTable(['Column1', 'Column2'])
        t.header = False
        t.border = True
        t.format = True
        t.align = 'l'
        t.add_row(["Player Wins", total_wins])
        t.add_row(["Computer Wins", total_losses])
        t.add_row(["Ties", total_ties])
        return t.get_html_string(border=True)

    @app.route('/', strict_slashes=False, methods=["GET", "POST"])
    def index():
        # If POST request, play the game
        if request.method == "POST":
            player_choice = request.form["my_selection"]
            computer_choice = computer_choose()
            match_output = play(player_choice, computer_choice)
            totals_output = results_total()
            return render_template("index.html",
                                   match_output=match_output,
                                   totals_output=totals_output)
        # If GET request, reset the counters and start fresh
        global total_wins
        global total_losses
        global total_ties
        total_wins = 0
        total_losses = 0
        total_ties = 0
        return render_template("index.html")

    return app


if __name__ == '__main__':
    app = my_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
