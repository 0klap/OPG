import time, random

#Search
def LinearSearch(pole, hodnota):
    for i in range(len(pole)):
        if pole[i] == hodnota:
            return i
    return -1

def BinarySearch(pole, hodnota, l_kraj, p_kraj, steps = 0):
    if l_kraj > p_kraj: return -1, steps
    stred = (l_kraj + p_kraj) // 2
    if hodnota == pole[stred]:
        return stred, steps

    if hodnota < pole[stred]:
        return BinarySearch(pole, hodnota, l_kraj, stred-1, steps + 1)
    else: 
        return BinarySearch(pole, hodnota, stred+1, p_kraj, steps + 1)


#Sort
def BubbleSort(pole):
    while True:
        y = 0
        for a in range(len(pole) - 1):
            if pole[a] > pole[a+1]:
                pole[a], pole[a+1] = pole[a+1], pole[a]
                y += 1
        if y == 0:
            return pole

def BubbleSortSteps(pole):
    porovnania = 0
    presuny  = 0
    while True:
        y = 0
        for a in range(len(pole) - 1):
            porovnania += 1
            if pole[a] > pole[a+1]:
                pole[a], pole[a+1] = pole[a+1], pole[a]
                presuny += 2
                y += 1
        if y == 0:
            return porovnania, presuny

def SelectSort(pole):
    for a in range(1, len(pole)):
        i = a
        for b in range(a+1, len(pole)):
            if pole[i] > pole[b]:
                i = b
        pole[a], pole[i] = pole[i], pole[a]
    return pole

def SelectSortSteps(pole):
    porovnania = 0
    presuny  = 0
    for a in range(0, len(pole)):
        i = a
        for b in range(a+1, len(pole)):
            porovnania += 1
            if pole[i] > pole[b]:
                i = b
        pole[a], pole[i] = pole[i], pole[a]
        presuny += 2
    return porovnania, presuny

def InsertSort(pole):
    for a in range(1, len(pole)):
        x = pole[a]
        b = a-1
        while b >=1 and pole[b] > x:
            pole[b], pole[b+1] = pole[b+1], pole[b]
            b -= 1
        pole[b + 1] = x
    return pole

def InsertSortSteps(pole):
    porovnania = 0
    presuny  = 0
    for a in range(1, len(pole)):
        x = pole[a]
        b = a-1
        while b >= 0 and pole[b] > x:
            porovnania += 1
            pole[b], pole[b+1] = pole[b+1], pole[b]
            presuny += 2
            b -= 1
        
        porovnania += 1
        pole[b + 1] = x
        presuny += 1

    return porovnania, presuny

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

def QuickSortSteps(pole, l_kraj, p_kraj):
    porovnania = 0
    presuny = 0

    if l_kraj < p_kraj:
        i = l_kraj
        for j in range(l_kraj, p_kraj):
            porovnania += 1
            if pole[j] < pole[p_kraj]:
                pole[j], pole[i] = pole[i], pole[j]
                presuny += 2
                i += 1
        pole[i], pole[p_kraj] = pole[p_kraj], pole[i]
        presuny += 2

        lave_porovnania, lave_presuny = QuickSortSteps(pole, l_kraj, i - 1)
        prave_porovnania, prave_presuny = QuickSortSteps(pole, i + 1, p_kraj)

        porovnania += lave_porovnania + prave_porovnania
        presuny += lave_presuny + prave_presuny

    return porovnania, presuny


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

def RadixSortSteps(pole, n):
    porovnania = 0  
    presuny = 0     

    mx = max(pole)
    e10 = 1
    vysledok = [0]*n

    while e10 <= mx:
        cislice = [0]*10
        for cislo in pole:
            cislice[cislo // e10 % 10] += 1
        index = 0
        for i in range(10):
            cislice[i], index = index, index + cislice[i]
        for cislo in pole:
            idx = cislo // e10 % 10
            vysledok[cislice[idx]] = cislo
            presuny += 1
            cislice[idx] += 1
        for i in range(n):
            pole[i] = vysledok[i]
            presuny += 1
        e10 *= 10
    return porovnania, presuny


def MergeSort(pole):

    if len(pole) <= 1:
        return pole

    stred = len(pole)//2
    lavo = pole[:stred]
    pravo = pole[stred:]

    lavo_zoradene = MergeSort(lavo)
    pravo_zoradene = MergeSort(pravo)

    result = []
    i = j = 0

    while i < len(lavo_zoradene) and j < len(pravo_zoradene):
        if lavo_zoradene[i] < pravo_zoradene[j]:
            result.append(lavo_zoradene[i])
            i += 1
        else:
            result.append(pravo_zoradene[j])
            j += 1

    while i < len(lavo_zoradene):
        result.append(lavo_zoradene[i])
        i += 1

    while j < len(pravo_zoradene):
        result.append(pravo_zoradene[j])
        j += 1

    return result

def MergeSortSteps(pole):
    porovnania = 0
    presuny = 0

    if len(pole) <= 1:
        return pole, porovnania, presuny

    stred = len(pole)//2
    lavo = pole[:stred]
    pravo = pole[stred:]

    lavo_zoradene, lave_porovnania, lave_presuny = MergeSortSteps(lavo)
    pravo_zoradene, prave_porovnania, prave_presuny = MergeSortSteps(pravo)

    porovnania += lave_porovnania + prave_porovnania
    presuny += lave_presuny + prave_presuny

    result = []
    i = j = 0
    while i < len(lavo_zoradene) and j < len(pravo_zoradene):
        porovnania += 1
        if lavo_zoradene[i] < pravo_zoradene[j]:
            result.append(lavo_zoradene[i])
            i += 1
            presuny += 1
        else:
            result.append(pravo_zoradene[j])
            j += 1
            presuny += 1

    while i < len(lavo_zoradene):
        result.append(lavo_zoradene[i])
        i += 1
        presuny += 1

    while j < len(pravo_zoradene):
        result.append(pravo_zoradene[j])
        j += 1
        presuny += 1

    return result, porovnania, presuny


def GenerateUnorderedList(n):
    randpole = []
    for j in range(n):
        randpole.append(random.randint(0, 10*j))
    return randpole

def GenerateOrderedList(n):
    pole = [0]
    for j in range(n):
        pole.append(random.randint(pole[-1], 10*j))
    return pole

import random

def GenerateGrowingList(n):
    pole = [0]
    for j in range(0, n):
        step = random.randint(-10, 10)
        next_val = min(pole[-1] + step, 10*j)
        next_val = max(next_val, 0)
        pole.append(next_val)
    return pole


def GenerateDecliningList(n):
    pole = GenerateGrowingList(n)
    return pole[::-1]



def SortProgram():
    n = int(input("Zadaj N: "))
    for i in range(5):
        pole = GenerateGrowingList(n)

        #BubbleSort
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        temp_pole1 = BubbleSort(temp_pole1)
        koniec = time.time()
        cas = koniec - zaciatok
        porovnania, presuny = BubbleSortSteps(temp_pole2)
        print(f"Bubble:\t{cas*1000:<20}{porovnania:<20}{presuny:<20}\n")

        #SelectSort
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        temp_pole1 = SelectSort(temp_pole1)
        koniec = time.time()
        cas = koniec - zaciatok
        porovnania, presuny = SelectSortSteps(temp_pole2)
        print(f"Select:\t{cas*1000:<20}{porovnania:<20}{presuny:<20}\n")

        #InsertSort
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        temp_pole1 = InsertSort(temp_pole1)
        koniec = time.time()
        cas = koniec - zaciatok
        porovnania, presuny = InsertSortSteps(temp_pole2)
        print(f"Insert:\t{cas*1000:<20}{porovnania:<20}{presuny:<20}\n")

        #InsertSort + BinarySearch
        hodnota = random.randint(pole[0], pole[-1])
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        temp_pole1 = InsertSort(temp_pole1)
        index, steps = BinarySearch(pole, hodnota, 0, len(pole)-1)
        koniec = time.time()
        cas = koniec - zaciatok
        porovnania, presuny = InsertSortSteps(temp_pole2)
        print(f"In+Bi:\t{cas*1000:<20}{porovnania+steps:<20}{presuny:<20}\n")


        #QuickSort
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        QuickSort(temp_pole1, 0, len(temp_pole1) - 1)
        koniec = time.time()
        cas = koniec - zaciatok
        porovnania, presuny = QuickSortSteps(temp_pole2, 0, len(temp_pole2) - 1)
        print(f"Quick:\t{cas*1000:<20}{porovnania:<20}{presuny:<20}\n")

        #MergeSort
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        temp_pole1 = MergeSort(temp_pole1)
        koniec = time.time()
        cas = koniec - zaciatok
        pole, porovnania, presuny = MergeSortSteps(temp_pole2)
        print(f"Merge:\t{cas*1000:<20}{porovnania:<20}{presuny:<20}\n")


        #RadixSort
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        temp_pole1 = RadixSort(temp_pole1, len(temp_pole1))
        koniec = time.time()
        cas = koniec - zaciatok
        porovnania, presuny = RadixSortSteps(temp_pole2, len(temp_pole2))
        print(f"Radix:\t{cas*1000:<20}{porovnania:<20}{presuny:<20}\n")

        
def SortProgram2():
    n = int(input("Zadaj N: "))
    for i in range(5):
        pole = GenerateDecliningList(n)

        #BubbleSort
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        temp_pole1 = BubbleSort(temp_pole1)
        koniec = time.time()
        cas = koniec - zaciatok
        porovnania, presuny = BubbleSortSteps(temp_pole2)
        print(f"Bubble:\t{cas*1000:<20}{porovnania:<20}{presuny:<20}\n")

        #SelectSort
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        temp_pole1 = SelectSort(temp_pole1)
        koniec = time.time()
        cas = koniec - zaciatok
        porovnania, presuny = SelectSortSteps(temp_pole2)
        print(f"Select:\t{cas*1000:<20}{porovnania:<20}{presuny:<20}\n")

        #InsertSort
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        temp_pole1 = InsertSort(temp_pole1)
        koniec = time.time()
        cas = koniec - zaciatok
        porovnania, presuny = InsertSortSteps(temp_pole2)
        print(f"Insert:\t{cas*1000:<20}{porovnania:<20}{presuny:<20}\n")

        #InsertSort + BinarySearch
        hodnota = random.randint(min(pole), max(pole))
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        temp_pole1 = InsertSort(temp_pole1)
        index, steps = BinarySearch(pole, hodnota, 0, len(pole)-1)
        koniec = time.time()
        cas = koniec - zaciatok
        porovnania, presuny = InsertSortSteps(temp_pole2)
        print(f"In+Bi:\t{cas*1000:<20}{porovnania+steps:<20}{presuny:<20}\n")


        #QuickSort
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        QuickSort(temp_pole1, 0, len(temp_pole1) - 1)
        koniec = time.time()
        cas = koniec - zaciatok
        porovnania, presuny = QuickSortSteps(temp_pole2, 0, len(temp_pole2) - 1)
        print(f"Quick:\t{cas*1000:<20}{porovnania:<20}{presuny:<20}\n")

        #MergeSort
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        temp_pole1 = MergeSort(temp_pole1)
        koniec = time.time()
        cas = koniec - zaciatok
        pole, porovnania, presuny = MergeSortSteps(temp_pole2)
        print(f"Merge:\t{cas*1000:<20}{porovnania:<20}{presuny:<20}\n")


        #RadixSort
        temp_pole1 = pole.copy()
        temp_pole2 = pole.copy()

        zaciatok = time.time()
        temp_pole1 = RadixSort(temp_pole1, len(temp_pole1))
        koniec = time.time()
        cas = koniec - zaciatok
        porovnania, presuny = RadixSortSteps(temp_pole2, len(temp_pole2))
        print(f"Radix:\t{cas*1000:<20}{porovnania:<20}{presuny:<20}\n")
    print("----------------")
def SearchProgram():
    n = int(input("Zadaj N: "))
    for i in range(10):
        pole = GenerateOrderedList(n)
        hodnota = random.randint(pole[0], pole[-1])
        print(hodnota)

        zaciatok = time.time()
        index = LinearSearch(pole, hodnota)
        koniec = time.time()
        cas = koniec - zaciatok
        print(f"{index:<20}{cas}\n")

        zaciatok = time.time()
        index, steps = BinarySearch(pole, hodnota, 0, len(pole)-1)
        koniec = time.time()
        cas = koniec - zaciatok
        print(f"{index:<10}{steps:<10}{cas}\n")
    


SortProgram2()
SortProgram2()