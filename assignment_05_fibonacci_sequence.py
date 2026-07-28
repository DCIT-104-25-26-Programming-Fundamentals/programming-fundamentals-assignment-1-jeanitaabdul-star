# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# Part A - Function to print the first N Fibonacci numbers
def print_fibonacci(n):
    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    first = 0
    second = 1

    print("Fibonacci sequence:", end=" ")

    for i in range(n):
        print(first, end=" ")
        next_num = first + second
        first = second
        second = next_num

    print()


# Part B - Function to check if a number is a Fibonacci number
def check_fibonacci(number):
    first = 0
    second = 1

    while first < number:
        next_num = first + second
        first = second
        second = next_num

    if first == number:
        print(f"{13} is a Fibonacci number.")
    else:
        print(f"{20} is NOT a Fibonacci number.")


# Main program
n = int(input("How many terms? 7"))
print_fibonacci(n)

number = int(input("\nEnter a number to check: "))
check_fibonacci(number)
