#O(n*n)
def SelectSort(pole):
    for a in range(1, len(pole)):
        i = a
        for b in range(a+1, len(pole) - 1):
            if pole[i] > pole[b]:
                i = b
        pole[a], pole[i] = pole[i], pole[a]
    return pole

#O(n*n)
def InsertSort(pole):
    for a in range(1, len(pole)):
        x = pole[a]
        b = a-1
        while b >=1 and pole[b] > x:
            pole[b], pole[b+1] = pole[b+1], pole[b]
            b = b - 1
    return pole

#O(n*n)
def InsertSortgUpgrade(pole):
    for a in range(1, len(pole)):
        x = pole[a]
        b = a-1
        while b >=1 and pole[b] > x:
            pole[b], pole[b+1] = pole[b+1], pole[b]
            b -= 1
        pole[b + 1] = x
    return pole

#O(n*n)
def BubbleSort(pole):
    while True:
        y = 0
        for a in range(len(pole) - 1):
            if pole[a] > pole[a+1]:
                pole[a], pole[a+1] = pole[a+1], pole[a]
                y += 1
        if y == 0:
            return pole

#O(n*n)
def BubbleSortUpgrade(pole):
    u = 0
    while True:
        y = 0
        for a in range(len(pole) - 1 - u):
            if pole[a] > pole[a+1]:
                pole[a], pole[a+1] = pole[a+1], pole[a]
                y += 1
        if y == 0:
            return pole
        u += 1

#O(n*logn)
def QuickSort(pole, l_kraj, p_kraj):
    if l_kraj < p_kraj:
        i = l_kraj
        for j in range(l_kraj, p_kraj):
            if pole[j] < pole[p_kraj]:
                pole[j], pole[i] = pole[i], pole[j]
                i+=1
        pole[i], pole[p_kraj] = pole[p_kraj], pole[i]
        QuickSort(pole, l_kraj, i - 1)
        QuickSort(pole, i+1, p_kraj)

#O(n*logn)
def MergeSort(pole):
    return pole

#O(n*logn)
def TreeSort(pole):
    return pole

#O(n*logn)
def HeapSort(pole):
    return pole

#O(n*k)
# k = počet číslic / znakov
def RadixSort(pole, n):
    mx = max(pole)
    e10 = 1
    vysledok = [0]*n
    while e10 <= mx:
        cislice = [0]*10
        for cislo in pole:
            cislice[cislo // e10 %10] += 1
        index = 0
        for i in range(10):
            cislice[i], index = index, index+cislice[i]
        for cislo in pole:
            vysledok[cislice[cislo // e10 %10]] += cislo % e10
            cislice[cislo // e10 %10] += 1
        pole, vysledok = vysledok, pole
        e10 *= 10
    return pole