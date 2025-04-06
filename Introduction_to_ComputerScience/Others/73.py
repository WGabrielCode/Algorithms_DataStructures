import random

def chances( x ) :
    c = 0
    arr = [ random.randrange( 1, 365 ) for _ in range( x ) ]
    for i in range( x-1 ) :
        for j in range( i+1, x ) :
            if arr[ i ] == arr[ j ] :
                return 1
    return 0

def main( x ) :
    r = 0
    m = 100000
    for i in range( m ) :
        r += chances( x )
    return r/m
#end def

print( main( 20 ) )