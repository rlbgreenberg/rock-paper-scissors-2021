# game.py

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

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



print ("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")