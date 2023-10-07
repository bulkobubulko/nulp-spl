from input_handling import get_input

def addition(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    try:
        result = first_number / second_number
        return result
    except ZeroDivisionError:
        print("Division by zero is not allowed. Enter values again.")
        first_number, second_number = get_input()
        return division(first_number, second_number)

def power(first_number, second_number):
    return first_number ** second_number

def square_root(first_number):
    try:
        result = first_number ** 0.5
        return result
    except ValueError:
        print("Square root of negative number is not allowed. Enter value again.")
        first_number = get_input()
        return square_root(first_number)

def remainder(first_number, second_number):
    try:
        result = first_number % second_number
        return result
    except ZeroDivisionError:
        print("Division by zero is not allowed. Enter values again.")
        first_number, second_number = get_input()
        return remainder(first_number, second_number)

def calculate(first_number, second_number, operator):
    if operator == '+':
        return addition(first_number, second_number)
    elif operator == '-':
        return subtraction(first_number, second_number)
    elif operator == '*':
        return multiplication(first_number, second_number)
    elif operator == '/':
        return division(first_number, second_number)
    elif operator == '^':
        return power(first_number, second_number)
    elif operator == '√':
        return square_root(first_number)
    elif operator == '%':
        return remainder(first_number, second_number)
    else:
        return "Invalid operator. Please try again."