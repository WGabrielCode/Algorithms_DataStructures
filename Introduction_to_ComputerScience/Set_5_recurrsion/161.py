from math import log10
def co( x ) :
    c = 0
    while x > 0 :
        if x % 2 == 1 :
            c +=1
        x //= 2
    return c
#end def co

def main( t , p = 0 , a = 0 , b = 0 , c = 0 ) :
    tleng = len( t )
    suma1 = 0
    if p == 0 :
        for i in range( tleng ) :
            t[ i ] = co( t[ i ] )
            suma1 += t[ i ]
    if suma1 % 3 != 0  :
        return False

    if p == tleng :
        return a == b == c

    #if a == b == c :  return True

    return (
    main( t , p + 1 , a + t[ p ] , b , c ) or
    main( t , p + 1 , a , b + t[ p ] , c ) or
    main( t , p + 1 , a , b , c + t[ p ] )
            )
#end def main

T = [ 2,3,5,7,15 ]
print( main( T ) )

n = 99999
print( int( log10(n) ) +1  )