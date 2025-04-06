def main( t ):
    l = len( t )
    rows = [ 0 for _ in range( l ) ]
    colu = [ 0 for _ in range( l ) ]
    minj = float( 'inf' )
    maxi = 0

    for i in range( l ) :
        for j in range( l ) :
            colu[ j ] += t[ i ][ j ]
            rows[ i ] += t[ i ][ j ]

    for x in range( l ) :
        if minj > rows[x]:
            minj = rows[x]
            mj = x
        if maxi < colu[x]:
            maxi = colu[x]
            mi = x

    return mj + 1 , mi +1

#end def

T = [
    [100,9,8,19,15] ,
    [1,6,8,1,15],
    [1,6,7,12,15],
    [5,6,8,65,15],
    [1,6,8,12,9]
    ]
print( main( T ) )

#[ 5,6,8,65,15]