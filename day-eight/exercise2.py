# Instructions

"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

You need to write a function that checks whether if the number passed into it is a prime number or not.
"""

#Write your code below this line ๐
def prime_checker(number):
    for i in range(2,number):
        if number % i == 0:
            return print('It\'s not a prime number')
    return print('It\'s a prime number')

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)