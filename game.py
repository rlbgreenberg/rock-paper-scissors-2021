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

# from reid
if user_choice == computer_choice:
    print("It's a tie, try again!")
elif (user_choice == "scissors") and (computer_choice == "paper"):
        print("Scissors cuts paper, you win!")
elif (user_choice == "rock") and (computer_choice == "scissors"):
        print("rock smashes scissors, you win!")
elif (user_choice == "paper") and (computer_choice == "rock"):
        print("Paper covers rock, you win!")
#COMPUTER WINNING SCENARIOS
elif (user_choice == "scissors") and (computer_choice == "rock"):
        print("rock smashes scissors, you lose!")
elif (user_choice == "rock") and (computer_choice == "paper"):
        print("paper covers rock, you lose!")
elif (user_choice == "paper") and (computer_choice == "scissors"):
        print("Scissors cuts paper, you lose!")

print ("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")