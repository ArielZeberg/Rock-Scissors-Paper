# ASCII art for the rock, paper, and scissors choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

# Welcome message and prompt to start the game
welcome = input("Welcome to rock-paper-scissors game! Type 'start' to start the game.").strip().lower()

# Generate a random choice for the computer: 0 for rock, 1 for paper, 2 for scissors
computer_random = random.randint(0, 2)

# Check if the user typed 'start' to begin the game
if welcome == "start":
    try:
        # Prompt user for their choice: 0 for rock, 1 for paper, 2 for scissors
        user_choice = int(input("What do you choose? type 0 for rock, 1 for paper, 2 for scissors.").strip())
        
        # If the user chooses rock (0)
        if user_choice == 0:
            print(f"You chose: {rock}")
            if computer_random == 0:
                print(f"The computer chose: {rock}\nDraw.")
            elif computer_random == 1:
                print(f"The computer chose: {paper}\nYou lose.")
            elif computer_random == 2:
                print(f"The computer chose: {scissors}\nYou win!")

        # If the user chooses paper (1)
        elif user_choice == 1:
            print(f"You chose: {paper}")
            if computer_random == 0:
                print(f"The computer chose: {rock}\nYou win!")
            elif computer_random == 1:
                print(f"The computer chose: {paper}\nDraw.")
            elif computer_random == 2:
                print(f"The computer chose: {scissors}\nYou lose.")
        
        # If the user chooses scissors (2)
        elif user_choice == 2:
            print(f"You chose: {scissors}")
            if computer_random == 0:
                print(f"The computer chose: {rock}\nYou lose.")
            elif computer_random == 1:
                print(f"The computer chose: {paper}\nYou win!")
            elif computer_random == 2:
                print(f"The computer chose: {scissors}\nDraw.")
        
        # If the user enters an invalid number
        else:
            print("You typed an invalid number - you lose.")
    
    except ValueError:
        # Handle the case where the input is not an integer
        print("Invalid input. Please enter a number (0, 1, or 2).")

else:
    # If the user doesn't type 'start'
    print("Invalid command. Please type 'start' to begin the game.")
