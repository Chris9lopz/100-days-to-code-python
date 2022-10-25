#Instructions

"""
You are painting a wall. The instructions on the paint 
can says that 1 can of paint can cover 5 square meters of wall. 
Given a random height and width of wall, calculate how many cans 
of paint you'll need to buy.
"""

#Write your code below this line 👇
import math # Import math module

def paint_calc(height,width,cover): # Define parameters
    return math.ceil((height * width) / cover) # Use ceil method to return and round up the calculation
    
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: ")) # Argument
test_w = int(input("Width of wall: ")) # Argumen
coverage = 5 # Argument
total = paint_calc(height=test_h, width=test_w, cover=coverage) # Print function
print(f'You\'ll need {total} cans of paint.') # Result

# Tested in coding rooms, score 100% in each test.