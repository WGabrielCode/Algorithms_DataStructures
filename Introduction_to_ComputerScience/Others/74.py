def zlozona( x ) :
    if x < 4 :
        return False
    i = 2
    while i <= x :
        if x % i == 0 :
            return True
        i += 1
    return False
#end def

def prime( x ) :
    if x < 2 :
        return False
    i = 2
    while i * i <= x :
        if x % i == 0 :
            return False
        i += 1
    return True
#end def

def main( t ) :
    czyp = True
    a , b = 1 , 1
    while b < len( t ) :
        if zlozona( t[ b ] ) == False :
            return False
        elif czyp :
            for i in range( a+1 , b ) :
                if prime( t[ i ] ) :
                    czyp = False
        a , b = b , a+b
    return True
#end def

#T = [i for i in range( 2 , 100 ) ]
T = [ 6 for i in range( 100) ]
T[ 21 ] = 11
print( main( T ) )


