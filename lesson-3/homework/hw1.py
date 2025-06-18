1. Create and Access List Elements
fruits = ['apple', 'banana', 'cherry', 'mango', 'orange']
print("Uchinchi meva:", fruits[2])
2. Concatenate Two Lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Yangi ro'yxat:", combined)
3. Extract Elements from a List

numbers = [10, 20, 30, 40, 50]
extracted = [numbers[0], numbers[len(numbers)//2], numbers[-1]]
print("Ajratilgan elementlar:", extracted)
4. Convert List to Tuple

movies = ['Inception', 'Titanic', 'Matrix', 'Avatar', 'Interstellar']
movies_tuple = tuple(movies)
print("Tuple:", movies_tuple)
5. Check Element in a List

cities = ['London', 'Paris', 'Tokyo', 'Berlin']
print("Paris ro'yxatda bormi?", 'Paris' in cities)
6. Duplicate a List Without Using Loops

numbers = [1, 2, 3]
duplicate = numbers * 2
print("Takrorlangan ro'yxat:", duplicate)
7. Swap First and Last Elements of a List

nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print("O'zgartirilgan ro'yxat:", nums)
8. Slice a Tuple

numbers = tuple(range(1, 11))
print("Kesilgan qism (index 3–7):", numbers[3:8])
9. Count Occurrences in a List

colors = ['blue', 'red', 'green', 'blue', 'yellow', 'blue']
count = colors.count('blue')
print("'blue' necha marta uchradi:", count)
10. Find the Index of an Element in a Tuple

animals = ('cat', 'dog', 'lion', 'tiger')
index = animals.index('lion')
print("'lion' indeksi:", index)
11. Merge Two Tuples

t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print("Birlashgan tuple:", merged)
12. Find the Length of a List and Tuple

my_list = [1, 2, 3, 4]
my_tuple = (10, 20, 30)
print("Ro'yxat uzunligi:", len(my_list))
print("Tuple uzunligi:", len(my_tuple))
13. Convert Tuple to List

t = (100, 200, 300, 400, 500)
converted = list(t)
print("Ro'yxatga aylantirilgan:", converted)
14. Find Maximum and Minimum in a Tuple

nums = (4, 10, 2, 8, 6)
print("Eng katta:", max(nums))
print("Eng kichik:", min(nums))
15. Reverse a Tuple

words = ('hello', 'world', 'python', 'rocks')
reversed_words = words[::-1]
print("Teskari tartibda:", reversed_words)
