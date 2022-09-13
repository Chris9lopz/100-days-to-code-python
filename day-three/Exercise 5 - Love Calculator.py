"""
Instructions

You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_names = name1.lower() + name2.lower()

t_count = lower_names.count("t")
r_count = lower_names.count("r")
u_count = lower_names.count("u")
e_count = lower_names.count("e")

first_digit = t_count + r_count + u_count + e_count

l_count = lower_names.count("l")
o_count = lower_names.count("o")
v_count = lower_names.count("v")

second_digit = l_count + o_count + v_count + e_count

total_score = int(str(first_digit) + str(second_digit))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score > 40 and total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")