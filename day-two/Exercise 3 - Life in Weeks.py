# Create a program using maths and f-Strings that tells us how many days, weeks, 
# months we have left if we live until 90 years old.

# ð¨ Don't change the code below ð
age = input("What is your current age?")
# ð¨ Don't change the code above ð

#Write your code below this line ð

# 1. Se crea variables calculando cuanto se tiene en 90 aÃ±os menos la edad ingresada por usuario
months = (90 * 12) - (int(age) * 12) # Se castea a entero edad
days = (90 * 365) - (int(age) * 365)
weeks = (90 * 52) - (int(age) * 52)

# 2. Imprimimos usando f-String para indicar el tiempo faltante
print(f"You have {days} days, {weeks} weeks, and {months} months left.")