def LinearSearch(pole, hodnota):
    for i in range(len(pole)):
        if pole[i] == hodnota:
            return i
    return -1

def BinarySearch(pole, hodnota, l_kraj, p_kraj, steps=1):
    
    if l_kraj > p_kraj: return -1, steps
    
    stred = (l_kraj + p_kraj) // 2
    
    if hodnota == pole[stred]:
        return stred, steps
    
    if hodnota < pole[stred]:
        return BinarySearch(pole, hodnota, l_kraj, stred-1, steps + 1)
    else: 
        return BinarySearch(pole, hodnota, stred+1, p_kraj, steps + 1)