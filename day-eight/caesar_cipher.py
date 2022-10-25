# List of letter of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Inputs 
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text,shift,direction): # Calling parameters
    empty_text = [] # Create a empty list
    for letter in text:
        word = alphabet.index(letter) # Looking for each letter in alphabet to know it index
        if direction.lower() == 'encode': # Calling direction = encode
            empty_text.append(alphabet[word + shift]) # Moves 5 positions to the right
        elif direction.lower() == 'decode': # Calling direction = decode
            empty_text.append(alphabet[word - shift]) # Moves 5 positions to the left
        else:
            print('Incorrect option, try again') # Requested a new start over if <> direction
            break

    new_word = ''.join(empty_text) # List to Str

    if direction.lower() == 'encode':
        print(f"The encode text is {new_word}") # Output message default
    else:
        print(f"The dencode text is {new_word}") # Output message default

caesar(text=text, shift=shift, direction=direction) # Calling the function