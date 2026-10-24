import random
import sys
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    ___
---'   _)_
          __)
          ___)
         ___)
---.____)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("\nWelcome to the Rock, Paper, Scissors game:")
confirm = input("Press enter to continue of type (Help) for the rules ").lower()
if confirm =="help" : 
 print("""
********Rules********
1)You choose and the computer chooses
2)Rock smashes scissors -> Rock wins
3)Scissors cut paper -> Scissors wins
4)Paper covers Rock -> Paper wins 
""")
user_choice = input("Enter your choice(rock , paper , scissors) : ").lower() 
if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice, please run the program again.")
    sys.exit(2)
else:
    if user_choice == "rock":
        print(f"\nYou chose:\n{rock}")
    elif user_choice == "paper":
        print(f"\nYou chose:\n{paper}")
    else:
        print(f"\nYou chose:\n{scissors}")

# computer choice
computer_choice = random.choice(["rock", "paper", "scissors"])

if computer_choice == "rock":
    print(f"\nComputer chose:\n{rock}")
elif computer_choice == "paper":
    print(f"\nComputer chose:\n{paper}")
else:
    print(f"\nComputer chose:\n{scissors}")

# Determine the winner (OUTSIDE the block)
if user_choice == computer_choice:
    print("It's a tie")
elif (
    (user_choice == "rock" and computer_choice == "scissors")
    or 
    (user_choice == "paper" and computer_choice == "rock")
    or
    (user_choice == "scissors" and computer_choice == "paper")
):
    print(f"You win! {user_choice} beats {computer_choice}.")
else:
    print(f"You lose! {computer_choice} beats {user_choice}.")
