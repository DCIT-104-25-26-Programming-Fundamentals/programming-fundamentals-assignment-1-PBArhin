# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(arr, n):
    total = 0
    for num in arr:
        total += num
    return total


def calculate_average(arr, n):
    total = calculate_sum(arr, n)
    return total / n  


def find_maximum(arr, n):
    max_val = arr[0]
    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val


def find_minimum(arr, n):
    min_val = arr[0]
    for i in range(1, n):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val


def main():
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: Number of elements must be greater than zero.")
        return

    arr = []
    for i in range(n):
        val = int(input(f"Enter number {i + 1}: "))
        arr.append(val)

    print("\nResults:")
    print(f"Sum:     {calculate_sum(arr, n)}")
    print(f"Average: {calculate_average(arr, n)}")
    print(f"Maximum: {find_maximum(arr, n)}")
    print(f"Minimum: {find_minimum(arr, n)}")


if __name__ == "__main__":
    main()