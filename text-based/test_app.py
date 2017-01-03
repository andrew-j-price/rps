from app import computer_choose


def test_computer_choose():
    assert computer_choose() == "rock" or "paper" or "scissors"
