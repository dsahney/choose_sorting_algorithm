# Helper Function, insert.
def insert(L, i):
    ''' (list, int) -> NoneType
    As a precondition, L[:i] must be sorted from least to greatest.
    ''' 
    # num is the number that is to be inserted in to the sorted list.
    num = L[i]
    
    # locate the index, k, where num belongs. We will shift the other values, to make room for num.
    k = i
    
    while k != 0 and L[k-i] > num:
        L[k] = L[k-1]
        k -= 1 # this will shift L[k - 1], to the right by one index, to L[k].
        
    L[k] = num # this will place num to its respective position.
    
def insertion_sort_algorithm(L):
    ''' (list) -> list
    Takes a list, L, and sorts its numbers from least to greatest value.
    '''
    for x in range(len(L)):
        insert(L, x)
    return L
