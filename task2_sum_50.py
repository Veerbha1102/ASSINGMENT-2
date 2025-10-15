# task2_sum_50.py

# Initialize a variable to store the sum
total_sum = 0

# 1. Uses a for loop to iterate over numbers from 1 to 50.
# range(1, 51) includes 1 and goes up to (but not including) 51,
# effectively covering the numbers 1, 2, ..., 50.
for number in range(1, 51):
    # 2. Calculates the sum of all integers in this range.
    total_sum = total_sum + number

# 3. Displays the final sum.
print(f"The sum of integers from 1 to 50 is: {total_sum}")

# Note: The mathematical formula for the sum of the first 'n' integers is n*(n+1)/2.
# For n=50, sum = 50 * 51 / 2 = 1275.
# This confirms the loop calculation is correct.
