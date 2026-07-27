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

def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(f"{val:>4}", end=" ")
        print()


def read_matrix(rows, cols, name=""):
    prefix = f"for {name} " if name else ""
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1} {prefix}(space-separated): ")
        # Convert string input "1 2 3" into a list of integers [1, 2, 3]
        row_values = [int(val) for val in row_input.split()]
        matrix.append(row_values)
    return matrix


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)

    return transposed


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)

    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            dot_product = 0
            for k in range(cols_a):
                dot_product += matrix_a[i][k] * matrix_b[k][j]
            row.append(dot_product)
        result.append(row)

    return result


def main():
    print("--- PART A: TRANSPOSE ---")
    m = int(input("Enter number of rows (M): "))
    n = int(input("Enter number of columns (N): "))
    mat_a = read_matrix(m, n)

    print("\nOriginal Matrix:")
    print_matrix(mat_a)

    transposed = transpose_matrix(mat_a)
    print("\nTransposed Matrix:")
    print_matrix(transposed)

    print("\n" + "=" * 40 + "\n")

    print("--- PART B: ADDITION ---")
    print(f"Reading two matrices of size ({m} x {n})...")
    mat_b1 = read_matrix(m, n, name="Matrix 1")
    mat_b2 = read_matrix(m, n, name="Matrix 2")

    sum_result = add_matrices(mat_b1, mat_b2)
    print("\nMatrix Sum:")
    print_matrix(sum_result)

    print("\n" + "=" * 40 + "\n")

    print("--- PART C: MULTIPLICATION ---")
    p = int(input(f"Enter number of columns for Matrix B (P) [Matrix A is {m}x{n}]: "))

    print(f"\nEnter Matrix A ({m} x {n}):")
    mult_a = read_matrix(m, n, name="Matrix A")

    print(f"\nEnter Matrix B ({n} x {p}):")
    mult_b = read_matrix(n, p, name="Matrix B")

    product_result = multiply_matrices(mult_a, mult_b)
    print("\nMatrix Product (A x B):")
    print_matrix(product_result)


if __name__ == "__main__":
    main()