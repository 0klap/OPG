#Rýchly O(n * logn)
#Nestabilný n * n
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
    return pole