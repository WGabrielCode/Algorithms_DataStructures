from zad1ktesty import runtests

def roznica( IN ):
    n = len( IN )
    S = [ 1 ] * n

    for i in range( n ) :
        if IN[ i ] == "1" : S[ i ] = -1

    print( S )
    max_v = -float( "inf" )
    for i in range( 1, n ) :
        S[ i ] = max( S[ i - 1 ] + S[ i ], S[ i ] )
        if max_v < S[ i ] :
            max_v = S[ i ]
    return max_v


S1 = [ 1 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 ]
S = "11000010001"
#print( roznica( S ) )

runtests ( roznica )