def zlozona( x ) :
    if x < 4  :
        return False
    if  x == 5 :
        return False
    if x % 2 == 0 or x % 5 == 0 or x % 3 == 0:
        return True
    i = 5
    while  i* i <= x :
        if x % i == 0 or x % ( i + 2 ) == 0 :
            return True
        i += 6
    return False
#end def

def nieparzysta( x ) :
    while x > 0 :
        if (x % 10) % 2 == 0 :
            return False
        x //= 10
    return True
#end def

def main( t ) :
    for j in range( len( t ) ) :
        ck = True
        for i in range( len( t )):
            if nieparzysta( t[ i ][ j ] ) and zlozona( t[ i ][ j ] ) :
                ck = False
                break
        if ck :
            return False
    return True
#end def

T = [
    [1,6,8,12,15] ,
    [1,6,8,12,15],
    [1,6,8,12,15],
    [1,6,8,12,15],
    [1,6,8,12,15]
    ]
print( main( T ) )