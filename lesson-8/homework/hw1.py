1. Handle ZeroDivisionError

try:
    x = 10
    y = 0
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
2. Raise ValueError on invalid integer input

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: That was not a valid integer.")
3. Handle FileNotFoundError

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
4. Raise TypeError for non-numerical input

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
        raise TypeError("Inputs must be numbers.")
    print(float(a) + float(b))
except TypeError as e:
    print("Error:", e)
5. Handle PermissionError

try:
    with open("/root/secret.txt", "r") as file:
        data = file.read()
except PermissionError:
    print("Error: Permission denied.")
6. Handle IndexError

try:
    items = [1, 2, 3]
    print(items[5])
except IndexError:
    print("Error: Index out of range.")
7. Handle KeyboardInterrupt

try:
    number = input("Enter a number (Press Ctrl+C to cancel): ")
    print("You entered:", number)
except KeyboardInterrupt:
    print("\nInput cancelled by user.")
8. Handle ArithmeticError

try:
    result = 10 / 0
except ArithmeticError:
    print("Arithmetic error occurred.")
9. Handle UnicodeDecodeError

try:
    with open("unicode_file.txt", encoding="ascii") as file:
        print(file.read())
except UnicodeDecodeError:
    print("Error: Unicode decode issue.")
10. Handle AttributeError

try:
    lst = [1, 2, 3]
    lst.upper()  # invalid for lists
except AttributeError:
    print("Error: Attribute not found for object.")

File Input/Output Exercises
1. Read entire text file

with open("sample.txt", "r") as file:
    print(file.read())
2. Read first n lines

n = 3
with open("sample.txt", "r") as file:
    for _ in range(n):
        print(file.readline(), end='')
3. Append text and display

with open("sample.txt", "a") as file:
    file.write("\nNew line added.")
with open("sample.txt", "r") as file:
    print(file.read())
4. Read last n lines

n = 2
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(''.join(lines[-n:]))
5. Read line by line into list

with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)
6. Read line by line into variable

with open("sample.txt", "r") as file:
    text = file.read()
    print(text)
7. Read into array (list)

with open("sample.txt", "r") as file:
    array = [line.strip() for line in file]
    print(array)
8. Find longest words

with open("sample.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)
9. Count lines

with open("sample.txt", "r") as file:
    count = sum(1 for line in file)
    print("Line count:", count)
10. Word frequency

from collections import Counter

with open("sample.txt", "r") as file:
    words = file.read().replace(",", " ").split()
    freq = Counter(words)
    print(freq)
11. Get file size

import os
print("File size:", os.path.getsize("sample.txt"), "bytes")
12. Write list to file

items = ["Apple", "Banana", "Cherry"]
with open("list.txt", "w") as file:
    for item in items:
        file.write(item + "\n")
13. Copy file content

with open("sample.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())
14. Combine lines from two files

with open("file1.txt") as f1, open("file2.txt") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())
15. Read a random line

import random
with open("sample.txt") as file:
    lines = file.readlines()
    print(random.choice(lines).strip())
16. Check if file is closed

file = open("sample.txt", "r")
print("Closed?", file.closed)
file.close()
print("Closed?", file.closed)
17. Remove newlines

with open("sample.txt") as file:
    lines = [line.strip() for line in file]
    print(lines)
18. Count words in file

with open("sample.txt") as file:
    text = file.read()
    words = text.replace(",", " ").split()
    print("Word count:", len(words))
19. Extract characters into list

char_list = []
for fname in ["file1.txt", "file2.txt"]:
    with open(fname) as f:
        char_list.extend(list(f.read()))
print(char_list)
20. Generate A.txt to Z.txt

import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is {letter}.txt\n")
21. Letters on each line

import string

letters_per_line = 5
letters = string.ascii_lowercase

with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), letters_per_line):
        f.write(letters[i:i+letters_per_line] + "\n")
