# O(1): konstant tid. Ett steg, oavsett hur stor listan är.
"""
Best case:    O(1)
Average case: O(1)
Worst case:   O(1)
Hämtar alltid index 0, oavsett hur stor listan är.
"""
def first(data):
    return data[0]          # index i en räcka

"""
Uppslagning i dict (hashtabell):
Best case:    O(1)
Average case: O(1)
Worst case:   O(n)  - om alla nycklar kolliderar (samma hashvärde)
"""
d = {"anna": 25}
d["anna"]                   # uppslagning i hashtabell (dict)



# O(log n): halverar varje varv.
"""
Best case:    O(1)      - x ligger precis i mitten vid första kollen
Average case: O(log n)
Worst case:   O(log n)  - x finns inte, vi halverar tills inget är kvar
"""
def binary_search(data, x):     # data måste vara sorterad
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == x:
            return mid
        if data[mid] < x:
            low = mid + 1       # kasta vänstra halvan
        else:
            high = mid - 1      # kasta högra halvan
    return -1



# O(n): en loop över alla element.
"""
Best case:    O(1)  - x ligger först i listan
Average case: O(n)  - x ligger i mitten (n/2 steg, konstanten stryks)
Worst case:   O(n)  - x ligger sist eller finns inte
"""
def linear_search(data, x):
    for i in range(len(data)):
        if data[i] == x:
            return i
    return -1



# O(n log n): dela i halvor (log n nivåer) och gå igenom alla på varje nivå (n).
"""
Best case:    O(n log n)
Average case: O(n log n)
Worst case:   O(n log n)
Alltid samma, delar och slår ihop oavsett hur datan ser ut.
Kräver O(n) extra minne. Stabil.
"""
def merge_sort(data):
    if len(data) < 2:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)   # slår ihop i O(n)

"""
sorted() använder Timsort (merge sort + insertion sort):
Best case:    O(n)       - listan är redan sorterad
Average case: O(n log n)
Worst case:   O(n log n)
"""
sorted(data)                    # Pythons inbyggda sortering, också O(n log n)



# O(n²): nästlad loop över samma lista.
"""
Best case:    O(n²)  - denna version går alltid igenom båda looparna
Average case: O(n²)
Worst case:   O(n²)  - listan är sorterad baklänges
(Optimerad bubble sort som avbryter när inga byten sker: best case O(n))
"""
def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]



# O(2ⁿ): varje anrop gör två nya anrop
"""
Best case:    O(2ⁿ)
Average case: O(2ⁿ)
Worst case:   O(2ⁿ)
Alltid samma, varje anrop delar sig i två tills basfallet nås.
"""
def fib(n):
    if n <= 1:                         # basfall
        return n
    return fib(n - 1) + fib(n - 2)     # två rekursiva anrop

# ELLER me Tornen i Hanoi ,också O(2ⁿ)
"""
Best case:    O(2ⁿ)
Average case: O(2ⁿ)
Worst case:   O(2ⁿ)
Alltid exakt 2ⁿ - 1 drag för n skivor.
"""
def hanoi(n, from_, dest, temp):
    if n == 0:
        return
    hanoi(n - 1, from_, temp, dest)    # flytta n-1 åt sidan
    print(f"Move disk {n} from {from_} to {dest}")
    hanoi(n - 1, temp, dest, from_)    # flytta tillbaka n-1




# O(n!): pröva alla möjliga ordningar (permutationer)
"""
Best case:    O(n!)
Average case: O(n!)
Worst case:   O(n!)
Alltid samma, måste skapa alla n! ordningar.
"""
def permutations(items):
    if len(items) <= 1:
        return [items]
    result = []
    for i in range(len(items)):                    # n val
        rest = items[:i] + items[i+1:]
        for p in permutations(rest):               # (n-1)! för resten
            result.append([items[i]] + p)
    return result