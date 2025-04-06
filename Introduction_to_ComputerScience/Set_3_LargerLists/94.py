def parzysta( x ) :
    while x > 0  :
        if ( x % 10 ) % 2 == 0 :
            return True
        x //= 10
    return False
#end def

def main( t ) :
    l = len( t )
    for j in range( l ) :
        ck = True
        for i in range( l ) :
            if not parzysta( t[ i ][ j ] ) :
                ck = False
        if ck :
            return True
    return False
#end def
T = [
    [1,6,8,12,15] ,
    [1,6,8,12,15],
    [1,6,8,12,15],
    [1,6,8,12,15],
    [1,6,8,12,15]
    ]
print( main( T ) )