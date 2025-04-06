def main( t ) :
    min = float( 'inf' )
    max = -( min )

    for i in range( len( t ) ) :
        if t[ i ] < min :
            min = t[ i ]
        if t[ i ] > max :
            max = t[ i ]

    a , b = True , True

    for i in range( len( t ) ) :
        if min == t[ i ] :
            if a :
                a = False
            else :
                return False
        if max == t[ i ] :
            if b :
                b = False
            else :
                return False
    return True
#end def

T = [ 1,7,5,2,1,6,9,3,1,91,0]
print( main( T ) )