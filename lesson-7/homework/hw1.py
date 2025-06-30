1. is_prime(n) funksiyasi

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
Izoh:

0 va 1 tub emas.

Har qanday sonni 2 dan √n gacha tekshirib chiqamiz.

2. digit_sum(k) funksiyasi

def digit_sum(k):
    return sum(int(d) for d in str(k))

Sonni satrga aylantiramiz va har bir raqamni yig'amiz.
3. print_powers_of_two(N) funksiyasi

def print_powers_of_two(N):
    power = 1
    while (power := power * 2) <= N:
        print(power, end=' ')
