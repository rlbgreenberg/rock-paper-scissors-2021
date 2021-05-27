# game.py

import random

import os
from dotenv import load_dotenv

load_dotenv()

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One")

print("Rock, Paper, Scissors, Shoot!")

user_choice = input(f"Welcome {PLAYER_NAME} to my Rock-Paper-Scissors game...Please choose either 'rock', 'paper', or 'scissors': ")

#print(user_choice)
print("USER CHOICE: ", user_choice)


#validate the input such that only if it is one of the choices
#... will we continue with the rest of the program
#... otherwise we'll stop the program before it tries
#... and we'll ask the user to run the program again

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE: ", computer_choice)


# Rock beats Scissors

if (user_choice == "rock") and (computer_choice == "scissors"):
    print("You win!")

if (computer_choice == "rock") and (user_choice == "scissors"):
    print("Oh, the computer won. It's ok!")

#Paper beats Rock

if (user_choice == "paper") and (computer_choice == "rock"):
    print("You win!")

if (computer_choice == "paper") and (user_choice == "rock"):
    print("Oh, the computer won. It's ok!")

# Scissors beats Paper

if (user_choice == "scissors") and (computer_choice == "paper"):
    print("You win!")

if (computer_choice == "scissors") and (user_choice == "paper"):
    print("Oh, the computer won. It's ok!")

# Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

if (user_choice == "rock") and (computer_choice == "rock"):
    print("It's a tie!")

if (user_choice == "paper") and (computer_choice == "paper"):
    print("It's a tie!")

if (user_choice == "scissors") and (computer_choice == "scissors"):
    print("It's a tie!")


print ("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")