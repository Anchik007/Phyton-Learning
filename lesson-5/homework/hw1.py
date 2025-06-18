
1. Leap Year Function

def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Example usage:
print(is_leap(2000))  # True
print(is_leap(1900))  # False
print(is_leap(2024))  # True
 2. Conditional Statements Exercise

n = int(input("Enter a number: "))

# Check and print based on specified conditions
if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:  # n is even and greater than 20
    print("Not Weird")
 Sample Inputs / Outputs:

Input: 3 → Output: Weird

Input: 4 → Output: Not Weird

Input: 18 → Output: Weird

Input: 22 → Output: Not Weird

 3. Even Numbers Between a and b (Without Using Loop)
Includes Solution 1 with if-else + list comprehension and Solution 2 with smart range() logic — both with error handling and comments.

Solution 1: With if-else using list comprehension

a = 3
b = 12

# Validate input
if a > b:
    raise ValueError("Invalid range: 'a' should be less than or equal to 'b'.")

# List comprehension with an if-condition to filter even numbers
even_numbers = [i for i in range(a, b + 1) if i % 2 == 0]

print("Even numbers between a and b:", even_numbers)
 Solution 2: Without if (using smart range() logic)

a = 3
b = 12

# Validate input
if a > b:
    raise ValueError("Invalid range: 'a' should be less than or equal to 'b'.")

# Start from the first even number ≥ a
start = a if a % 2 == 0 else a + 1

# Use step=2 to skip all odd numbers
even_numbers = list(range(start, b + 1, 2))

print("Even numbers between a and b:", even_numbers)
