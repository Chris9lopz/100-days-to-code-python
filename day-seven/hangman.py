import random

# Create a hangman game 

# Step 1: Create a list of random words

word_list = ["jirafa","elefante","tigre","leon","pulpo","tiburon","dinosaurio"]

# Step 2: Choose randomly a word into the list

chosen_word = random.choice(word_list)

# Step 3: Ask to the user a letter

guess = input("Guess a letter: ").lower()

# Step 4: Validate if the letter is into the chosen_word 

for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")