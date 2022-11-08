from art import logo
import random

EASY_MODE = 10
HARD_MODE = 5

def level_difficulty(level):

    if level == 'easy':
        return EASY_MODE
    elif level == 'hard':
        return HARD_MODE
    
def game():

    print(logo)
    print('Welcome to the Number Guessing Game')
    print('I\'m thinking of a number between 1 and 100')

    random_number = random.randint(1,100)
    print(random_number)
    level = input('Choose a difficulty. Type \'easy\' or \'hard\': ')

    attempts = level_difficulty(level)

    end_program = False

    while not end_program:

        print(f'You have attempts {attempts} remaining to guess the number')
       
        user_guess = int(input('Make a guess: '))

        if user_guess < random_number:
            print('Too low')
            attempts -= 1
        elif user_guess > random_number:
            print('Too high')
            attempts -= 1
        else:
            print(f"You got it! The answer was {random_number}.")
            end_program = True

        if attempts == 0:
            print(f"You've run out of guesses, you lose. The correct number was {random_number}")
            end_program = True
        elif end_program == False:
            print('Guess again')

game()