import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to Rock Paper Scissors.")
player_choice = input("Choose rock, paper, or scissors: ").lower()
if player_choice == "rock":
    print("\nPlayer Chose ROCK")
    print(rock)
if player_choice == "paper":
    print("\nPlayer Chose PAPER")
    print(paper)
if player_choice == "scissors":
    print("\nPlayer Chose SCISSORS")
    print(scissors)


# get computer choice
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print("\nCOMPUTER Chose ROCK")
    print(rock)
if computer_choice == 1:
    print("\nCOMPUTER Chose PAPER")
    print(paper)
if computer_choice == 2:
    print("\nCOMPUTER Chose SCISSORS")
    print(scissors)


# GAME LOGIC
if (
    player_choice == "rock"
    and computer_choice == 0
    or player_choice == "paper"
    and computer_choice == 1
    or player_choice == "scissors"
    and computer_choice == 2
):
    print("ITS A TIE")
elif player_choice == "rock" and computer_choice == 2:
    print("PLAYER WINS")
elif player_choice == "paper" and computer_choice == 0:
    print("PLAYER WINS")
elif player_choice == "scissors" and computer_choice == 1:
    print("PLAYER WINS")
elif computer_choice == 0 and player_choice == "scissors":
    print("COMPUTER WINS")
elif computer_choice == 1 and player_choice == "rock":
    print("COMPUTER WINS")
elif computer_choice == 2 and player_choice == "paper":
    print("COMPUTER WINS")
