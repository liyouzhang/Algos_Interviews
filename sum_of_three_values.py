def sum_three_one(arr,val):
    '''
    input : arr - list of numbers; val - float / int
    output : bool

    approach 1 - naive
    '''
    for i in arr:
        for j in arr:
            if j != i:
                if (val - i - j) != i and (val-i-j) != j and (val-i-j) in arr:
                    print (i,j, (val-i-j))
                    return True
    return False

    #Space - O(1)
    #Run time - O(n^2)

def sum_three_two(arr,val):
    '''
    approach 2:
    1. sort the array
    2. have 2 idx
    3. check if val - idx1 - idx2 still in the array between these 2 idx
    4. if yes, then 

    '''
    arr.sort()
    i = 0
    j = len(arr)-1
    for i in 
