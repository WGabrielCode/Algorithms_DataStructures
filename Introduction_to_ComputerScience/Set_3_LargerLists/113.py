def distance( t ) :
    leng = len( t )
    bmax = t[ 0 ]
    bmin = t[ 0 ]
    indx_max = 0
    idnx_min = 0

    for i in range( leng ) :
        for j in range( leng ) :
            if bmax[ j ] < t[ i ][ j ] :
                bmax = t[ i ]
                indx_max = i
                break
            elif bmin[ j ] > t[ i ][ j ] :
                bmin = t[ i ]
                indx_min = i
                break
    return abs(indx_max - indx_min )
#end def

T = [
    [0,1,1,1,1],
    [1,1,1,1,1],
    [0,0,1,0,1],
    [1,1,1,1,0],
    [0,0,0,0,1]
    ]
print( distance( T ) )