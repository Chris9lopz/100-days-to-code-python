# Modules
from art import logo
import random

# Const attempts
EASY_MODE = 10
HARD_MODE = 5

# Function that define the level
def level_difficulty(level):

    if level == 'easy':
        return EASY_MODE # Return the number of attempts = 10
    elif level == 'hard':
        return HARD_MODE # Return the number of attempts = 5
    
def game():

    # Import logo and main prints
    print(logo) 
    print('Welcome to the Number Guessing Game')
    print('I\'m thinking of a number between 1 and 100')

    random_number = random.randint(1,100) # Choose the random number to choose
    # print(random_number) Answer
    level = input('Choose a difficulty. Type \'easy\' or \'hard\': ') # Select the level

    attempts = level_difficulty(level) # Return the level difficult regarding to the level input

    end_program = False # Flag 

    while not end_program:

        print(f'You have attempts {attempts} remaining to guess the number') # Calling the num of attempts
       
        user_guess = int(input('Make a guess: ')) # User input request

        # Conditionals to see if the number is less than or higher than the random number
        if user_guess < random_number:
            print('Too low')
            attempts -= 1 # Subtract attempts until 0 or the user guess the number
        elif user_guess > random_number:
            print('Too high')
            attempts -= 1 # Subtract attempts until 0 or the user guess the number
        else:
            print(f"You got it! The answer was {random_number}.")
            end_program = True

        if attempts == 0: # if total of attempts is equal to 0 say this and close the program
            print(f"You've run out of guesses, you lose. The correct number was {random_number}")
            end_program = True
        elif end_program == False: # Keep asking until attempts equal to or the user guess the number
            print('Guess again')

game() # Calling game function