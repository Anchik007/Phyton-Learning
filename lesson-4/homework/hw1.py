1. Sort a Dictionary by Value (Ascending and Descending)

d = {'a': 3, 'b': 1, 'c': 2}

# Ascending
asc = dict(sorted(d.items(), key=lambda x: x[1]))
print("O‘sish tartibida:", asc)

# Descending
desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print("Kamayish tartibida:", desc)
2. Add a Key to a Dictionary

d = {0: 10, 1: 20}
d[2] = 30
print("Yangi lug‘at:", d)
3. Concatenate Multiple Dictionaries

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged = {**dic1, **dic2, **dic3}
print("Birlashgan lug‘at:", merged)
4. Generate a Dictionary with Squares (1 to n)

n = 5
squares = {x: x**2 for x in range(1, n+1)}
print("Kvadratlar lug‘ati:", squares)
5. Dictionary of Squares (1 to 15)

squares_15 = {x: x**2 for x in range(1, 16)}
print("1 dan 15 gacha kvadratlar:", squares_15)
 Set Mashqlari
1. Create a Set

my_set = {1, 2, 3, 4, 5}
print("Yaratilgan set:", my_set)
2. Iterate Over a Set

for item in my_set:
    print("Element:", item)
3. Add Member(s) to a Set

my_set.add(6)
my_set.update([7, 8])
print("Qo‘shilgandan so‘ng:", my_set)
4. Remove Item(s) from a Set

my_set.discard(2)  # xato bermaydi
my_set.remove(3)   # agar yo‘q bo‘lsa xato beradi
print("O‘chirilgandan so‘ng:", my_set)
5. Remove an Item if Present in the Set

item = 4
if item in my_set:
    my_set.remove(item)
print("Agar bo‘lsa, olib tashlandi:", my_set)
