# Write a program that adds the digits in a 2 digit number. e.g. 
# if the input was 35, then the output should be 3 + 5 = 8

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# 1. Identificando el typo de dato str que retorna un input se selecciona la posicion de los dos
#numeros, luego se hace el casteo de cada uno de ellos a tipo integer
suma_numeros = int(two_digit_number[0]) + int(two_digit_number[1])

# 2. Se realiza la impresion de la variable
print(str(suma_numeros))
