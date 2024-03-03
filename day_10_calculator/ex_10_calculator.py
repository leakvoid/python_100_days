def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

continue_calc = True

num1 = float(input("Input first number: "))
while continue_calc:
    operator = input("Choose operator: ")

    num2 = float(input("Input another number: "))

    result = operators[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {result}")

    num1 = result
    continue_calc = True if input("Do you wish to continue (y/n): ") == 'y' else False