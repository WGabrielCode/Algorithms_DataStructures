from egzP6btesty import runtests 
"""
Orientacyjny łączny czas : 0.60 sek.
Status testów: A A A A A A A A A A
O(n)

"""
def jump( M ):

    moves = { 'UL':(-1,2) , 'UR':(1,2) , 'RU':(2,1) , 'RD':(2,-1) , 'DR':(1,-2) , 'DL':(-1,-2) , 'LD':(-2,-1) , 'LU':(-2,1) }

    memo = { (0,0) : True }

    x = 0
    y = 0
    result = 1

    for move in M :

        add_x , add_y  = moves[ move ]
        x += add_x
        y += add_y

        key = (x,y)
        if key in memo :
            item_bool = memo[key]
            result += -1 if item_bool else 1
            memo[key] = not item_bool
        else :
            result += 1
            memo[ (x,y) ] = True

    return result
"""
M = ['UL', 'RD', 'LU', 'LU', 'RD', 'DL', 'UR', 'DR']
print( jump( M ) )
"""
runtests(jump, all_tests = True)