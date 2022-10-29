from replit import clear # Work on replit exclusive
from art import logo

print(logo) # Print logo

end_program = False # Flag where say when the program stop

while not end_program:
  name = input('What\'s your name?: ') # Inputs
  bid_price = int(input('What\'s your bid?: '))

  total_user = {} # Creating a empty dict
  total_user[name] = bid_price # Adding info 

  highest_price = max(total_user, key=total_user.get) # To know who is the highest bidder

  participant = input('Are there any other bidders?: ').lower() # Asking to the user if there any other bidder

  if participant == 'yes':
    clear() # Using module replt / Clears the screen
  else:
    print(f'The winner is {highest_price} with ${total_user[highest_price]}') # Print winner
    end_program = True # Finish the loop / program