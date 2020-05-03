"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array):
    '''
    pivot idx starts at -1 as convention
    while pivot idx 
        compare with pointer starting at idx = 0
        while pointer <= pivot:
            if pivot >= pointer:
                None
            if pivot < pointer:
                move pointer behind pivot 
                move pivot to previous position
                move previous num to idx = 0
            pointer idx +=1
        pivot idx -= 1
    '''
    pivot = len(array) - 1
    while pivot >= 0:
        pointer = 0
        while pointer <= pivot:
            if array[pivot] >= array[pointer]:
                None
            else:
                pivot_num = array[pivot] # pivot_num is 2
                array[pivot] = array[pointer] # array[-1] = 3 
                array[pivot-1] = pivot_num
                array[] = 


    return []

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)