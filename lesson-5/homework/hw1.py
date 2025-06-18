1. Leap Year Function (is_leap)

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

# Example
print(is_leap(2000))  # True
print(is_leap(1900))  # False
print(is_leap(2024))  # True
 2. Conditional Statements Exercise

n = int(input("Enter a number: "))

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

n = 3 → Weird

n = 4 → Not Weird

n = 18 → Weird

n = 22 → Not Weird

3. Even Numbers Between a and b Without Loop
 Solution 1: With if-else using list comprehension

a = 3
b = 12

even_numbers = [i for i in range(a, b + 1) if i % 2 == 0]
print("Even numbers:", even_numbers)
 Solution 2: Without if-else — Using range() smartly
ь
a = 3
b = 12

start = a + (a % 2)  # If a is odd, go to next even; else stay
even_numbers = list(range(start, b + 1, 2))
print("Even numbers:", even_numbers)
