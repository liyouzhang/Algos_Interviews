def find_sum_of_two_one(A, val):
  '''
  input - array of numbers; val - a number
  output - bool
  1. native:
  - try all combinations of two numbers in array: 2 for loops
  - for each, test if == target
  '''

  #1. naive approach
  for a in A:
    for b in A:
      if b != a:
        if a + b == val:
          return True
  return False

  #space - O(1)
  #running time - O^2

def find_sum_of_two_two(A, val):
    '''
    approach 2. find if val-current_num is in the list
    create a set of found_values
    loop through the array,
    check if val-value is in the found_values, if yes, return true
    else, add to the set
    '''
    found_values = set()
    for i in A:
        if val-i in found_values:
            return True
        found_values.add(i)
    return False

    #space - O(n) set 
    #run time - O(n) 1 for loop

def find_sum_of_two_three(A, val):
    '''
    approach 3. 
    use two indexes to avoid for loop
    1. sort array
    2. use two idx
    3. sum, if sum < target, then move left +1 ; if > target, then move right -1
    '''
    i = 0
    j = len(A) - 1
    A.sort()
    if A[i] + A[j] < val:
        i += 1
    if A[i] + A[j] > val:
        j -= 1
    if A[i] + A[j] == val:
        return True
    return False


