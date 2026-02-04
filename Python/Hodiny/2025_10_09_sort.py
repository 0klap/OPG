import time, random, datetime
#Search
def LinearSearch(pole, hodnota):
    for i in range(len(pole)):
        if pole[i] == hodnota:
            return i
    return -1

def BinarySearch(pole, hodnota, l_kraj, p_kraj):
    stred = (l_kraj + p_kraj) // 2
    if l_kraj < p_kraj: return -1
    if hodnota == pole[stred]:
        return stred
    if hodnota < pole[stred]:
        return BinarySearch(pole, hodnota, l_kraj, stred)
    else: 
        return BinarySearch(pole, hodnota, stred, p_kraj)

def StartLinearSearch(pole, hodnota, cislo):
    print(f"Zacinam LinearSearch {cislo}...")
    zaciatok = time.time()
    index = LinearSearch(pole, hodnota)
    koniec = time.time()
    cas = koniec - zaciatok
    print(f"{koniec - zaciatok} \n")
    print(index)
    return round(cas, rounding)

def StartBinarySearch(pole, hodnota, cislo):
    print(f"Zacinam BinarySearch {cislo}...")
    zaciatok = time.time()
    index = BinarySearch(pole, hodnota, 0, len(pole))
    koniec = time.time()
    cas = koniec - zaciatok
    print(f"{koniec - zaciatok} \n")
    print(index)
    return round(cas, rounding)

#Sorts
def SelectSort(pole):
    for a in range(1, len(pole)):
        i = a
        for b in range(a+1, len(pole) - 1):
            if pole[i] > pole[b]:
                i = b
        pole[a], pole[i] = pole[i], pole[a]
    return pole

def InsertionSort(pole):
    for a in range(1, len(pole)):
        x = pole[a]
        b = a-1
        while b >=1 and pole[b] > x:
            pole[b], pole[b+1] = pole[b+1], pole[b]
            b = b - 1
    return pole

def InsertionSortgUpgrade(pole):
    for a in range(1, len(pole)):
        x = pole[a]
        b = a-1
        while b >=1 and pole[b] > x:
            pole[b], pole[b+1] = pole[b+1], pole[b]
            b -= 1
        pole[b + 1] = x
    return pole

def BubbleSort(pole):
    while True:
        y = 0
        for a in range(len(pole) - 1):
            if pole[a] > pole[a+1]:
                pole[a], pole[a+1] = pole[a+1], pole[a]
                y += 1
        if y == 0:
            return pole

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

def StartBubbleSort(pole, cislo):
    print(f"Zacinam BubbleSort {cislo}...")
    zaciatok = time.time()
    pole = BubbleSort(pole)
    koniec = time.time()
    cas = koniec - zaciatok
    print(f"{koniec - zaciatok} \n")
    return round(cas, rounding)

def StartBubbleSortUpgrade(pole, cislo):
    print(f"Zacinam BubbleSortUpgrade {cislo}....")
    zaciatok = time.time()
    pole = BubbleSortUpgrade(pole)
    koniec = time.time()
    cas = koniec - zaciatok
    print(f"{koniec - zaciatok} \n")
    return round(cas, rounding)

def StartSelectSort(pole, cislo):
    print(f"Zacinam SelectSort {cislo}....")
    zaciatok = time.time()
    pole = SelectSort(pole)
    koniec = time.time()
    cas = koniec - zaciatok
    print(f"{koniec - zaciatok} \n")
    return round(cas, rounding)

def StartInsertSort(pole, cislo):
    print(f"Zacinam SelectSort {cislo}....")
    zaciatok = time.time()
    pole = InsertionSort(pole)
    koniec = time.time()
    cas = koniec - zaciatok
    print(f"{koniec - zaciatok} \n")
    return round(cas, rounding)

def StartInsertSortUpgrade(pole, cislo):
    print(f"Zacinam SelectSort {cislo}....")
    zaciatok = time.time()
    pole = InsertionSortgUpgrade(pole)
    koniec = time.time()
    cas = koniec - zaciatok
    print(f"{koniec - zaciatok} \n")
    return round(cas, rounding)


def SearchProgram(start = 0, koniec = 1000, skok = 100):
    LinearSearchTimes = []
    BinarySearchTimes = []

    for i in range(start, koniec, skok):
        n.append(i)
        randpole = []
        for j in range(i):
            randpole.append(random.randint(0, 10*j))
        
        pole1 = randpole
        pole2 = randpole
        print(pole1)

        hodnota = int(input("Zadaj hladanu hodnotu: "))

        cas1 = StartLinearSearch(pole1, hodnota, i)
        LinearSearchTimes.append(cas1)

        pole2 = InsertionSort(pole2)
        cas2 = StartBinarySearch(pole2, hodnota, i)
        BinarySearchTimes.append(cas2)

        with open("search/search_times.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{i:<10}{cas1:<25}{cas2:<25}")



def SortProgram(start = 0, koniec = 1000, skok = 100):

    BubbleSortTimes = []
    BubbleSortUpgradeTimes = []
    SelectSortTimes = []
    InsertionSortTimes = []
    InsertionSortUpgradeTimes = []

    for i in range(start, koniec, skok):
        n.append(i)
        randpole = []
        for j in range(i):
            randpole.append(random.randint(0, 10*j))

        pole1 = randpole
        pole2 = randpole
        pole3 = randpole
        pole4 = randpole
        pole5 = randpole

        cas1 = StartBubbleSort(pole1, i)
        BubbleSortTimes.append(cas1)

        cas2 = StartBubbleSortUpgrade(pole2, i)
        BubbleSortUpgradeTimes.append(cas1)

        cas3 = StartSelectSort(pole3, i)
        SelectSortTimes.append(cas3)

        cas4 = StartInsertSort(pole4, i)
        InsertionSortTimes.append(cas4)

        cas5 = StartInsertSortUpgrade(pole5, i)
        InsertionSortUpgradeTimes.append(cas5)

        with open("sort/sort_times.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{i:<10}{cas1:<25}{cas2:<25}{cas3:<25}{cas4:<25}{cas5:<25}")
        

    print(f"N\tBubblesort\t\tBubblesortUpgrade\tSelectsort\tInsertionsort")
    with open("sort/sort_times_log.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\n{datetime.datetime.now()}")
        f.write(f"\n{'N':<10}{'Bubblesort':<25}{'BetterBubble':<25}{'Selectsort':<25}{'Insertionsort':<25}{'InsertionsortUpgrade':<25}")
        f.close()


    for i in range(len(BubbleSortTimes)):
        print(f"\n{n[i]:<10}{BubbleSortTimes[i]:<25}{BubbleSortUpgradeTimes[i]:<25}{SelectSortTimes[i]:<25}{InsertionSortTimes[i]:<25}")
        with open("sort/sort_times_log.txt", "a", encoding="utf-8") as f:
            f.write(f"\n{n[i]:<10}{BubbleSortTimes[i]:<25}{BubbleSortUpgradeTimes[i]:<25}{SelectSortTimes[i]:<25}{InsertionSortTimes[i]:<25}")
    f.close()

n = []
rounding = 10

#start = int(input("Start: "))
#koniec = int(input("Koniec: "))
#skok = int(input("Skok: "))

    