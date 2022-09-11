# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 1. Insertamos los valores casteados a flotante de acuerdo a la forma de bmi
bmi = float(weight) / (float(height) ** 2)

# 2. Imprimimos y cambiamos el tipo de dato a entero de acuerdo a lo solicitado por el ejercicio
print(int(bmi))