import os


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Zero Error: Divided by zero")
    else:
        return a / b


operations_dict = {
    '+': 'add',
    '-': 'subtract',
    '*': 'multiply',
    '/': 'divide'
}


def calculator_function(number1, number2, operator):
    calculator_function_map = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    return calculator_function_map[operator](number1, number2)


def calculator():
    number1 = float(input("Enter the first number: "))

    for symbol in operations_dict:
        print(symbol)

    continue_flag = True
    while continue_flag:
        operator = input('Pick an operator: ')
        number2 = float(input("Enter the next number: "))
        output = calculator_function(number1, number2, operator)
        print(f'{number1} {operator} {number2} = {output}')

        should_continue = (
            (input(f'Enter "y" to continue with {output} OR "n" to start new calculation OR "x" to exit: ')).
            lower())
        if should_continue == 'y':
            number1 = output
        elif should_continue == 'n':
            continue_flag = False
            os.system('cls')
            calculator()
        else:
            continue_flag = False


calculator()
