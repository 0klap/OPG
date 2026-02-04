import search, sorts
import time, random

def GenerateUnorderedList(n):
    randpole = []
    for j in range(n):
        randpole.append(random.randint(0, 10*j))
    return randpole

def GenerateOrderedList(n):
    pole = [0]
    for j in range(n-1):
        pole.append(random.randint(pole[-1], 10*j))
    return pole

def GenerateGrowingList(n):
    pole = [random.randint(0, 10)]
    for i in range(n-1):
       pole.append(random.randint(0, 5)+ pole[-1]) 

n = int(input("Zadaj N: "))

for i in range(10):
    pole = GenerateOrderedList(n)
    number = random.randint(0, 100)
    print(number)
    if number < 80:
        hodnota = random.choice(pole)
    else:
        hodnota = random.randint(pole[0], pole[-1])
    print(hodnota)
    print()
    
    zaciatok = time.time()
    index = search.LinearSearch(pole, hodnota)
    koniec = time.time()
    cas = koniec - zaciatok
    print(f"{index:<25}{cas}\n")

    zaciatok = time.time()
    index, steps = search.BinarySearch(pole, hodnota, 0, len(pole)-1)
    koniec = time.time()
    cas = koniec - zaciatok
    print(f"{index:<10}{steps:<10}{cas}\n")

    k = input()
    

