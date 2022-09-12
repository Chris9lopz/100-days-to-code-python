# Instructions
# Write a program that works out whether if a given number is an odd or even number.

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 1. Se utiliza el modulo para saber si es divisible o no por 2, en caso contrario se imprime el resultado
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")