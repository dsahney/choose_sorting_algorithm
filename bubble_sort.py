# Bubble Sort Algorithm

def bubble_sort(L):
    ''' (list) -> list
    Return a list, L, that is sorted from least to greatest value.
    >>> bubble_sort([2, 1, 4, 6, 2, 3])
    [1, 2, 2, 3, 4, 6]
    >>> bubble sort([-1, -4, 0, 3, 2, -10, 1])
    [-10, -4, -1, 0, 1, 2, 3]
    '''
    x = len(L) - 1
    
    while x != 0:
        for i in range(end):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]

        x -= 1
    
