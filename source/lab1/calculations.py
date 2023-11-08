# Include the parent directory in the system's import path
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from lab1.input_handling import get_input

def addition(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    if second_number == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return first_number/second_number

def power(first_number, second_number):
    return first_number ** second_number

def square_root(first_number):
    if first_number == 0:
        raise ValueError("Square root of negative number is not allowed.")
    return first_number ** 0.5

def remainder(first_number, second_number):
    if second_number == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    else:
        return first_number % second_number

def calculate(first_number, second_number, operator):
    if operator == '+':
        return addition(first_number, second_number)
    elif operator == '-':
        return subtraction(first_number, second_number)
    elif operator == '*':
        return multiplication(first_number, second_number)
    elif operator == '/':
        try: 
            return division(first_number, second_number)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return "undefined"
    elif operator == '^':
        return power(first_number, second_number)
    elif operator == '√':
        try: 
            return square_root(first_number)
        except ValueError as e:
            print(f"Error: {e}")
            return "undefined"
    elif operator == '%':
        try: 
            return remainder(first_number, second_number)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return "undefined"
    else:
        return "Invalid operator. Please try again."