"""This module contains functions for basic calculator operations."""

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