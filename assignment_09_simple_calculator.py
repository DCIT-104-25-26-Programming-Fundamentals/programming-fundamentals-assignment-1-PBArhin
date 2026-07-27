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

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return round(num1 / num2, 2)


def modulus(num1, num2):
    if num2 == 0:
        return "Error: Modulus by zero is undefined."
    return num1 % num2


def power(num1, num2):
    return num1 ** num2


# =============================================================================
# HELPER FUNCTIONS & MAIN LOOP
# =============================================================================

def get_numbers():
    try:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        # Format whole floats (like 10.0) as integers (10) for cleaner display
        n1_display = int(num1) if num1.is_integer() else num1
        n2_display = int(num2) if num2.is_integer() else num2
        return num1, num2, n1_display, n2_display
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return None, None, None, None


def main():
    operations = {
        "1": (add, "+"),
        "2": (subtract, "-"),
        "3": (multiply, "*"),
        "4": (divide, "/"),
        "5": (modulus, "%"),
        "6": (power, "**")
    }

    while True:
        print("\n============================")
        print("      SIMPLE CALCULATOR     ")
        print("============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")

        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("\nGoodbye!")
            break
        elif choice in operations:
            func, symbol = operations[choice]
            num1, num2, n1_disp, n2_disp = get_numbers()

            if num1 is not None:
                result = func(num1, num2)
                if isinstance(result, str):  
                    print(result)
                else:
                    res_display = int(result) if isinstance(result, float) and result.is_integer() else result
                    print(f"Result: {n1_disp} {symbol} {n2_disp} = {res_display}")
        else:
            print("Invalid choice! Please select a number between 1 and 7.")


if __name__ == "__main__":
    main()