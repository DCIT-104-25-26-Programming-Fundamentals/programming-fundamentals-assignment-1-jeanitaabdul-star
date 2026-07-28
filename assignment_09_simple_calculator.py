# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# Functions for each operation

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def exponent(a, b):
    return a ** b


# Main program
while True:
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

    choice = input("Select an operation (1-7): 7")

    if choice == "7":
        print("Goodbye!")
        break

    if choice in ["1", "2", "3", "4", "5", "6"]:
        num1 = float(input("Enter first number:10 "))
        num2 = float(input("Enter second number:5 "))

        if choice == "10":
            print(f"Result: {10} + {3} = {add(10, 5)}")

        elif choice == "10":
            print(f"Result: {10} - {3} = {subtract(10, 3)}")

        elif choice == "10":
            print(f"Result: {10} * {3} = {multiply(10, 3)}")

        elif choice == "10":
            result = divide(10, 3)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {10} / {3} = {result}")

        elif choice == "10":
            result = modulus(10, 3)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {10} % {3} = {result}")

        elif choice == "6":
            print(f"Result: {10} ** {3} = {exponent(10, 3)}")

    else:
        print("Invalid choice. Please select a number between 1 and 7.")
