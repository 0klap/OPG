#Napíšte program, ktorý si vypýta celé číslo N
#a zmeria čas trvania algoritmu pre zväčšenie x o 1
import time

n = int(input("Zadaj N: "))
total1 = 0
avg1 = 0

total2 = 0
avg2 = 0

total3 = 0
avg3 = 0

for i in range(2):
    #Prvý algoritmus
    zaciatok = time.time()
    x = 0
    x = n*1
    koniec = time.time()

    print(f"Algoritmus1: {zaciatok} {koniec} {koniec - zaciatok} {x}")
    total1 += koniec - zaciatok

    #Druhý algoritmus - O(n)
    zaciatok = time.time()
    x = 0

    for i in range(n):
        x += 1
    koniec = time.time()
    print(f"Algoritmus2: {zaciatok} {koniec} {koniec - zaciatok} {x}")
    total2 += koniec - zaciatok

    #Tretí algoritmus - O(n**2)
    zaciatok = time.time()
    x = 0

    for i in range(n):
        for j in range(n):
            x += 1
    koniec = time.time()
    print(f"Algoritmus2: {zaciatok} {koniec} {koniec - zaciatok} {x}")
    total3 += koniec - zaciatok

avg1 = total1 / 10
avg2 = total2 / 10
avg3 = total2 / 10

print(f"{avg1}\t{avg2}\t{avg3}")