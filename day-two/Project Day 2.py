# Proyecto dia 2
# Crear una calculadora que permita definir cuanto pagará cada persona
# Tendrá que preguntar por el total de la cuenta, cuanto es la propina que desea dar
# En cuantos se divide la cuenta y tener en cuenta que el resultado se muestre en 2 cifras decimal

# Se imprime el saludo de la calculadora 
print("Welcome to the tip calculator.")

# Se solicita el monto total de la factura
total_bill = float(input("What was the total bill? $"))

# Se solicita el porcentaje de propina entre los definidos por el proyecto
perc_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

# Se solicita el total de personas a dividir la cuenta
split_per_person = int(input("How many people to split the bill? "))

# Se calcula el total de la cuenta por el porc indicado divido por el total de personas
# Se usa la funcion round para definir 2 decimales
total = round(((total_bill * (perc_tip / 100)) + total_bill) / split_per_person,2) 
print(f"Each person should pay: ${total}")