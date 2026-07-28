# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# =============================================================================
# Matrix Operations: Transpose, Addition, Multiplication
# =============================================================================
def read_matrix(rows, cols, name="Matrix"):
    """Reads a rows x cols matrix from user input, one row per line."""
    matrix = []
    print(f"\nEnter values for {name} ({rows}x{cols}):")
    for i in range(rows):
        while True:
            raw = input(f"Enter row {i + 1}: ").split()
            if len(raw) != cols:
                print(f"  Expected {cols} values, got {len(raw)}. Try again.")
                continue
            try:
                row = [float(x) for x in raw]
            except ValueError:
                print("  Please enter numbers only. Try again.")
                continue
            matrix.append(row)
            break
    return matrix
def print_matrix(matrix, title="Matrix"):
    """Prints a matrix in a neatly aligned grid."""
    print(f"\n{title}:")
    if not matrix:
        print("  (empty)")
        return
    # Determine column width based on the longest formatted number
    formatted = [[format_num(val) for val in row] for row in matrix]
    width = max(len(val) for row in formatted for val in row)
    for row in formatted:
        line = "  ".join(val.rjust(width) for val in row)
        print(f"  {line}")
def format_num(x):
    """Formats a number without unnecessary trailing zeros/decimals."""
    if x == int(x):
        return str(int(x))
    return f"{x:.2f}"
# -----------------------------------------------------------------------------
# PART A — Transpose
# -----------------------------------------------------------------------------
def transpose(matrix):
    """Returns the transpose of a matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result
# -----------------------------------------------------------------------------
# PART B — Addition
# -----------------------------------------------------------------------------
def add_matrices(a, b):
    """Adds two matrices of the same size element-wise using nested loops."""
    rows = len(a)
    cols = len(a[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result
# -----------------------------------------------------------------------------
# PART C — Multiplication
# -----------------------------------------------------------------------------
def multiply_matrices(a, b):
    """Multiplies matrix A (MxN) by matrix B (NxP) using nested loops."""
    m = len(a)
    n = len(a[0])
    p = len(b[0])
    result = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    return result
# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------
def get_dimensions(label="matrix"):
    rows = int(input(f"Enter number of rows for {label}: "))
    cols = int(input(f"Enter number of columns for {label}: "))
    return rows, cols
def run_transpose():
    print("\n=== PART A: Transpose a Matrix ===")
    rows, cols = get_dimensions()
    matrix = read_matrix(rows, cols)
    print_matrix(matrix, "Original Matrix")
    result = transpose(matrix)
    print_matrix(result, "Transposed Matrix")
def run_addition():
    print("\n=== PART B: Add Two Matrices ===")
    rows, cols = get_dimensions("both matrices (same size)")
    a = read_matrix(rows, cols, "Matrix A")
    b = read_matrix(rows, cols, "Matrix B")
    print_matrix(a, "Matrix A")
    print_matrix(b, "Matrix B")
    result = add_matrices(a, b)
    print_matrix(result, "Sum (A + B)")
def run_multiplication():
    print("\n=== PART C: Multiply Two Matrices ===")
    m, n = get_dimensions("Matrix A")
    print(f"Matrix B must have {n} rows to match A's columns.")
    n2 = int(input("Confirm number of rows for Matrix B: "))
    if n2 != n:
        print("Error: Matrix B's rows must equal Matrix A's columns.")
        return
    p = int(input("Enter number of columns for Matrix B: "))
    a = read_matrix(m, n, "Matrix A")
    b = read_matrix(n, p, "Matrix B")
    print_matrix(a, "Matrix A")
    print_matrix(b, "Matrix B")
    result = multiply_matrices(a, b)
    print_matrix(result, "Product (A x B)")
def main():
    print("=" * 50)
    print("MATRIX OPERATIONS PROGRAM")
    print("=" * 50)
    run_transpose()
    run_addition()
    run_multiplication()
if __jeanita__ == "__main__":
    main()
