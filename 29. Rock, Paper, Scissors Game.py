import random

# Rock, Paper, Scissors Game
choice = input("Select R for Rock, P for Paper, or S for Scissors: ").upper()

print(f"You chose {choice}")

options = ["R", "P", "S"]
computer = random.choice(options)

print(f"The computer chose {computer}")

if choice == computer:
    print("It's a TIE!")
elif (choice == "R" and computer == "S") or \
     (choice == "P" and computer == "R") or \
     (choice == "S" and computer == "P"):
    print("You WON!")
elif choice in options:
    print("You LOSE!")
else:
    print("Invalid choice! Please choose R, P, or S next time.")
