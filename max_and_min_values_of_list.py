# This function will take a list, L, and determine its maximum and minimum values.

def max_min(L):
    ''' (list) -> tuple
    Return a tuple that shows the min and max value of a list, respectively.
    '''
    sorted_list =  bubble_sort(L)
    max_value = L[-1]
    min_value = L[0]
    return (min_value, max_value)
