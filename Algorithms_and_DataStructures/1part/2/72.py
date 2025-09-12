def subarr( t ) :
    l = len( t )
    res = [ 0 for _ in range( ( 1 + l ) * l // 2 ) ]
    z = 0
    for i in range( l ) :
        for j in range( i + 1 , l + 1 ) :
            res[ z ] = t[ i : j ]
            z+=1
    return res
#end def

def main( t ) :
    l = len ( t )
    maxn = 0
    subarrays = subarr( t )
    revsubarrays = subarr( t[::-1] )

    for i in range( len( subarrays ) ) :
        for j in range( len( revsubarrays )  ) :
            if subarrays[ i ] == revsubarrays[ j ] :
                n = len( subarrays[ i ] )
                if maxn < n :
                    maxn = n
    return maxn
#end def

T = [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]

print( main( T ) )