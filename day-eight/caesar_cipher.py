# List of letter of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Inputs 
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

    # Function of encryption
#def encrypt(text,shift): # Parameters word and shift movement
#  encrypt_list = [] # Empty list 
#  for letter in text: 
#    new_word = alphabet.index(letter) # Searching the letter into the alphabet
#    encrypt_list.append(alphabet[new_word + shift]) # Add elements and move # of words according to shift
#  encrypt_word = ''.join(encrypt_list) # List to str
#  print(f"The encode text is {encrypt_word}") # Output default
#encrypt(text,shift) # Calling the function
#
#def dencrypt(text,shift): # Parameters word and shift movement
#  encrypt_list = [] # Empty list 
#  for letter in text: 
#    new_word = alphabet.index(letter) # Searching the letter into the alphabet
#    encrypt_list.append(alphabet[new_word - shift]) # Add elements and move # of words according to shift
#  encrypt_word = ''.join(encrypt_list) # List to str
#  print(f"The dencode text is {encrypt_word}") # Output default
#
#dencrypt(text,shift) # Calling the function

def caesar(text,shift,direction):
    empty_text = []
    for letter in text:
        word = alphabet.index(letter)
        if direction.lower() == 'encode':
            empty_text.append(alphabet[word + shift])
        elif direction.lower() == 'decode':
            empty_text.append(alphabet[word - shift])
        else:
            print('Incorrect option, try again')
            break

    new_word = ''.join(empty_text)

    if direction.lower() == 'encode':
        print(f"The encode text is {new_word}")
    else:
        print(f"The dencode text is {new_word}")

caesar(text=text, shift=shift, direction=direction)