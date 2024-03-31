# Funciones 
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ValueError("Division by zero is not allowed.")

# Preguntar Al Usuario
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Opciones A Elegir
operation = input("Enter the operation (+, -, *, /): ")

# Condicionales 
if operation == "+":
    result = sumar(num1, num2)
elif operation == "-":
    result = restar(num1, num2)
elif operation == "*":
    result = multiplicar(num1, num2)
elif operation == "/":
    result = dividir(num1, num2)
else:
    raise ValueError("Invalid operation.")

print("Result:", result)