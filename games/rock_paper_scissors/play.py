"""
Play rock, paper, scrissors with the computer. The player is asked which option he chooses
and the computer will randomly pick one and announce the winner. If both sides end up with
the same option, the game will rerun until a winner is chosen.

Usage:
    python play.py

Example:
    Q -> What do you choose - rock, paper or scissors: rock
"""
from random import randint


OPTIONS = [
    "rock",
    "paper",
    "scissors"
]

RESULT_COMBINATIONS = {
    "rock": {
        "rock": "tied",
        "paper": "lose",
        "scissors": "win"
    },
    "paper": {
        "rock": "win",
        "paper": "tied",
        "scissors": "lose"
    },
    "scissors": {
        "rock": "lose",
        "paper": "win",
        "scissors": "tied"
    }
}

RESULT_OUTPUT = {
    "tied": {
        "user_output": "The user and computer have chosen the same thing and are tied. Try again.",
        "instructions": "continue"
    },
    "win": {
        "user_output": "Congratulations, you have won.",
        "instructions": "end"
    },
    "lose": {
        "user_output": "The computer has won. Better luck next time.",
        "instructions": "end"
    }
}

def main():
    flag = True

    while flag:
        user_choice = input("What do you choose - rock, paper or scissors: ").lower()
        if user_choice not in OPTIONS:
            print(f"You have chosen {user_choice}, but the only available options are 'rock', 'paper' and 'scissors'. Please choose one of them!")
            continue
        computer_choice = OPTIONS[randint(0, 2)]
        print("Computer choice: ", computer_choice)

        winner_determined = determine_winner(user_choice, computer_choice)
        if winner_determined == "end":
            flag = False


def determine_winner(user_choice, computer_choice):
    user_outcome = RESULT_COMBINATIONS[user_choice][computer_choice]
    # print("User outcome: ", user_outcome)
    result = RESULT_OUTPUT[user_outcome]
    # print("Result: ", result)
    print(result["user_output"])
    return result["instructions"]


if __name__=="__main__":
    main()
