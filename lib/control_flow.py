#!/usr/bin/env python3

def admin_login(username, password):
    """Authenticate user based on username and password."""
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    return "Access denied"

def hows_the_weather(temperature):
    """Return a message based on the temperature."""
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    """Return Fizz, Buzz, FizzBuzz, or the number based on divisibility."""
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    """Perform basic arithmetic operations."""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
