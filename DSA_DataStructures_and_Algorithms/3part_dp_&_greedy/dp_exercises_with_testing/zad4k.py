from zad4ktesty import runtests

def falisz ( T ):

    n = len( T )
    for j in range( 1 , n ) :
        T[0][j] += T[0][j-1]
        T[j][0] += T[j-1][0]
    #print( T )

    for i in range( 1 , n ) :
        for j in range( 1 , n ) :
            T[i][j] += min( T[i-1][j] , T[i][j-1] )
    return T[n-1][n-1]

T = [
[0, 5, 4, 3],
[2, 1, 3, 2],
[8, 2, 5, 1],
[4, 3, 2, 0]
]
#print( falisz( T ) )

runtests ( falisz )
