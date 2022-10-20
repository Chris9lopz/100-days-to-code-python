import random

# Create a hangman game

# Create a list of posible words
word_list = ["jirafa","elefante","tigre","leon","pulpo","tiburon","dinosaurio"]

# Select a random word from the list
chosen_word = random.choice(word_list)

print(f'This is a clue {chosen_word}')

# Create a empty list 
blank_list = []

# Add into the empty list the length of the chosen word
for i in range(len(chosen_word)):
    blank_list.append("_")

# Loop until is not '_' more in the blank_list or blank_list equal to 0
while '_' in blank_list or len(blank_list) == 0:
    
    # Ask to the user a letter and convert in a lower letter
    guess = input("Guess a letter: ").lower()

    print(blank_list)

    # Modify the value of the blank list if the letter is in chosen_word
    position = 0
    for letter in chosen_word:
        if letter == guess:
            blank_list[position] = letter
            position += 1
        else:
            position += 1

    print(blank_list)

print('You won')