import random

# Create a hangman game 

# Step 1: Create a list of random words

word_list = ["jirafa","elefante","tigre","leon","pulpo","tiburon","dinosaurio"]

# Step 2: Choose randomly a word into the list

chosen_word = random.choice(word_list)
print(f'This is a clue {chosen_word}')

# Step 3: Ask to the user a letter

guess = input("Guess a letter: ").lower()

# Step 4: Validate if the letter is into the chosen_word 

for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")

# Step 5: Create a blank list and replace the spaces '_' with the correct letter

blank_list = []
for i in range(len(chosen_word)):
  blank_list.append("_")

print(blank_list)

position = 0
for letter in chosen_word:
    if letter == guess:
        blank_list[position] = letter
        position += 1
    else:
        position += 1

print(blank_list)