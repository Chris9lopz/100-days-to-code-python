# Adding
def add(n1,n2):
    return n1 + n2

# Subtract
def subtract(n1,n2):
    return n1 - n2

# Multiply
def multiply(n1,n2):
    return n1 * n2

# Divide
def divide(n1,n2):
    return n1 / n2

calculator = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
}

num1 = int(input('What is the first number?: '))

for option in calculator:
    print(option)

symbol = input('Pick an operation from the line of above: ')

num2 = int(input('What is the second number?: '))

operation_function = calculator[symbol]
answer = operation_function(num1,num2)

print(f'{num1} {symbol} {num2} = {answer}')