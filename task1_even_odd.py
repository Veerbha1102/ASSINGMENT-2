# task1_even_odd.py

# 1. Takes an integer input from the user.
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
else:
    # 2. Checks whether the number is even or odd using an if-else statement.
    # A number is even if the remainder when divided by 2 is 0.
    if number % 2 == 0:
        # 3. Displays the result accordingly.
        print(f"The number {number} is Even.")
    else:
        # 3. Displays the result accordingly.
        print(f"The number {number} is Odd.")
