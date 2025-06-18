1. Age Calculator

name = input("Ismingizni kiriting: ")
birth_year = int(input("Tug‘ilgan yilingizni kiriting: "))
current_year = 2025

age = current_year - birth_year
print(f"{name}, sizning yoshingiz {age} da.")
2. Extract Car Names
From: 'LMaasleitbtui' → Car names: 'Lamborghini', 'Subaru' (Hidden letters: Lamb..., Sub...)
txt = 'LMaasleitbtui'
car1 = txt[0] + txt[2] + txt[4] + txt[6] + txt[8]  # "Lamb..."
car2 = txt[1] + txt[3] + txt[5] + txt[7] + txt[9] + txt[11]  # "Subaru..."
print("Car names:", car1, car2)
(If real cars are encoded alternately, logic can be adjusted accordingly.)

3. Extract Car Names
From: 'MsaatmiazD' (Likely "Mazda" and "Mitsubishi")

txt = 'MsaatmiazD'
car1 = txt[::2]  # M a t a z = "Mataz"
car2 = txt[1::2] # s a m i D = "samiD"
print("Car name guesses:", car1, car2)
(These seem like encoded names; you can update logic if known.)

4. Extract Residence Area
python

txt = "I'am John. I am from London"
# Extract last word
area = txt.split("from")[-1].strip()
print("Residence area:", area)
5. Reverse String

text = input("Matn kiriting: ")
print("Teskari tartibda:", text[::-1])
6. Count Vowels

text = input("Matn kiriting: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Unli harflar soni:", count)
7. Find Maximum Value

nums = input("Sonlarni vergul bilan kiriting: ")  # Masalan: 4,7,2,9
num_list = list(map(int, nums.split(',')))
print("Eng katta son:", max(num_list))

8. Check Palindrome
word = input("So‘z kiriting: ").lower()
if word == word[::-1]:
    print("Bu so‘z palindrom.")
else:
    print("Bu so‘z palindrom emas.")
9. Extract Email Domain

email = input("Email manzilini kiriting: ")  # Masalan: user@gmail.com
domain = email.split('@')[-1]
print("Email domeni:", domain)
10. Generate Random Password

import random
import string

length = 12
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Tasodifiy parol:", password)
