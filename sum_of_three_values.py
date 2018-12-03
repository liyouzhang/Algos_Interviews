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

