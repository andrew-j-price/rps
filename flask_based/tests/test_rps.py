from flask_based.rps import RPS
rps = RPS()


def test_initialize():
    assert rps.user_wins == 0 and rps.comp_wins == 0 and rps.ties == 0


def test_computer_choices():
    assert rps.computer_choose() == "rock" or "paper" or "scissors"


def test_play_the_game():
    # Tie Games
    assert rps.play("rock", "rock") == rps.dict_victor.get("key_tied")
    assert rps.user_wins == 0 and rps.comp_wins == 0 and rps.ties == 1
    assert rps.play("paper", "paper") == rps.dict_victor.get("key_tied")
    assert rps.user_wins == 0 and rps.comp_wins == 0 and rps.ties == 2
    assert rps.play("scissors", "scissors") == rps.dict_victor.get("key_tied")
    assert rps.user_wins == 0 and rps.comp_wins == 0 and rps.ties == 3
    # Computer Wins
    assert rps.play("paper", "scissors") == rps.dict_victor.get("key_comp")
    assert rps.user_wins == 0 and rps.comp_wins == 1 and rps.ties == 3
    assert rps.play("rock", "paper") == rps.dict_victor.get("key_comp")
    assert rps.user_wins == 0 and rps.comp_wins == 2 and rps.ties == 3
    assert rps.play("scissors", "rock") == rps.dict_victor.get("key_comp")
    assert rps.user_wins == 0 and rps.comp_wins == 3 and rps.ties == 3
    # User Wins
    assert rps.play("paper", "rock") == rps.dict_victor.get("key_user")
    assert rps.user_wins == 1 and rps.comp_wins == 3 and rps.ties == 3
    assert rps.play("rock", "scissors") == rps.dict_victor.get("key_user")
    assert rps.user_wins == 2 and rps.comp_wins == 3 and rps.ties == 3
    assert rps.play("scissors", "paper") == rps.dict_victor.get("key_user")
    assert rps.user_wins == 3 and rps.comp_wins == 3 and rps.ties == 3
