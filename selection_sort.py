# Helper function
def find_smallest_index(L, i):
    ''' (list, int) -> int
    Return the index of the smallest item in L[i:]. # first occurence?!?!!?!?!?!?1??
    >>> find_smallest_index([1, 3, 4, 2, 7, 9], 3)
    3
    '''
    index_of_smallest_item = i
    
    for j in range(i+1, len(L)):
        if L[j] < L[index_of_smallest_item]:
            index_of_smallest_item = j
            
     return index_of_smallest_item

# Selection Sort Algorithm
def selection_sort(L):
    ''' (list) -> list
    Return a list, L, that has been sorted from least to greatest value.
    >>> selection_sort([2, 1, 4, 6, 2, 3])
    [1, 2, 2, 3, 4, 6]
    >>> selection_sort([-1, -4, 0, 3, 2, -10, 1])
    [-10, -4, -1, 0, 1, 2, 3]
    '''
    for i in range(len(L)):
        index_of_smallest_item = find_smallest_index(L, i)
        L[index_of_smallest_item], L[i] = L[i], L[index_of_smallest_item]
        
    return L
