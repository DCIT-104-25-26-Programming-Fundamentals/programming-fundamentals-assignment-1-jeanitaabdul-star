# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# Part A - Function to print one multiplication table
def single_table(number):
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")


# Part B - Function to print tables from 1 to N
def all_tables(n):
    for num in range(1, n + 1):
        print(f"\nMultiplication Table for {num}:")
        for i in range(1, 13):
            print(f"{num} x {i} = {num * i}")
        print("---------------------------")


# Main program
number = int(input("Enter a number:5 "))

if number <= 0:
    print("Error: Please enter a positive integer.")
else:
    # Part A
    single_table(5))

    # Part B
    n = int(input("\nEnter N for tables from 1 to N: "))

    if n <= 0:
        print("Error: Please enter a positive integer.")
    else:
        all_tables(n)
