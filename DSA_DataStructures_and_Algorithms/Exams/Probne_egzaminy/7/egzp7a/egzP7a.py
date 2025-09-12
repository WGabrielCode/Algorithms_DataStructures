from egzP7atesty import runtests 

def akademik( T ):

    memo = {}
    n = len( T )

    for i in range( n ) :

        skip = False
        for val in T[i] :
            if val == None :
                skip = True
        if skip : continue

        memo[ i ] = False

    if m





    return memo

T = [(2, 3, None), (0, 1, 3), (0, 2, None), (1, 3, 4), (2, 3, None) ]
print( akademik( T ) )

#runtests ( akademik )