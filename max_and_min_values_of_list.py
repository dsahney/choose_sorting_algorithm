# This function will take a list, L, and determine its maximum and minimum values.

import bubble_sort
import insertion_sort
import selection_sort

def max_min_bubble(L):
    ''' (list) -> tuple
    Return a tuple that uses the bubble sort algorithms, to determine the min and max value of a list, respectively.
    '''
    sorted_list =  bubble_sort(L)
    max_value = L[-1]
    min_value = L[0]
    return (min_value, max_value)

def max_min_insertion(L):
    ''' (list) -> tuple
    Return a tuple that uses the insertion sort algorithms, to determine the min and max value of a list, respectively.
    '''
    sorted_list =  insertion_sort(L)
    max_value = L[-1]
    min_value = L[0]
    return (min_value, max_value)

def max_min_selection(L):
    ''' (list) -> tuple
    Return a tuple that uses the selection sort algorithms, to determine the min and max value of a list, respectively.
    '''
    sorted_list =  selection_sort(L)
    max_value = L[-1]
    min_value = L[0]
    return (min_value, max_value)
