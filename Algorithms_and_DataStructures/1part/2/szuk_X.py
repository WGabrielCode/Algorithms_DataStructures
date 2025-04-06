def find_sum( arr , x ) :
    i = 0
    j = len( arr) -1
    while i < j :
        curr_sum = arr[i] + arr[j]
        if curr_sum == x :
            return i, j
        if curr_sum < x :
            i += 1
        else :
            j -= 1
    return None , None

arr = [2,5,7,8,10,15,20]
print( find_sum( arr , 17) )