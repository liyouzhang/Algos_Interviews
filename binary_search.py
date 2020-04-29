"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


# LZ answer 20200427
# wrong - because infinite recursion..
# has not been corrected yet
def binary_search_LZ(input_array, value):
    """
    find the middle idx of the array length, and if even, err on the lower side
    compare value and the middle element
    if ==, then return the index
    if value < middle, then find the middle of the left array
    and compare, until ==
    if exhaust all options, then return -1
    edge cases: to be add
    """
    middle_idx = int(len(input_array)/2) - 1 
    # int(3.5) = 3, no matter if odd or even
    # -1 because idx starts at 0
    if value == input_array[middle_idx]:
        return middle_idx
    elif value > input_array[middle_idx]:
        right_idx_start = middle_idx + 1 # +1 to exclude middle element
        right = input_array[right_idx_start::]
        output = binary_search(right, value)
        return right_idx_start + output 
    elif value < input_array[middle_idx]:
        left_idx_end = middle_idx -1 
        left = input_array[::left_idx_end]
        output = binary_search(left,value)
        return output
    return -1


# correct answer from https://www.cs.usfca.edu/~galles/visualization/Search.html
# improvement over mine: 
# mine creates sub array, but actually all I need to do is to move the pointer idx
def binary_search(input_array, value):
    '''
    code here
    '''
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = int((low+high)/2)
        if value == input_array[mid]:
            return mid
        elif value < input_array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1 



test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)