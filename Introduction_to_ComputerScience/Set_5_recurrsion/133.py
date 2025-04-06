from math import log10

def is_prime( x ) :
    if x < 2 :
        return False
    if x == 2 or x == 3 or x == 5 :
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 :
        return False
    i = 5
    while i * i <= x :
        if x % i == 0 or x % ( i + 2 ) == 0 :
            return False
        i += 6
    return True
#end def
def nn( x, i ) :
    leng = int( log10( x ) ) + 1
    if i >= leng :
        return x
    left = x //( 10 ** (leng -i )  )
    right = x %( 10 ** ( leng - i -1 ) )
    return  left * (10 ** ( leng - i -1 ) )  + right
#end def

def main( x , indx = 0 ) :
    leng = int( log10( x ) ) + 1
    if leng < 2 :
        return
    elif is_prime( x ) :
        print( x, end = " ")

    if leng <= indx :
        return

    main( nn( x, indx ) , indx +1 )
    main( x, indx + 1 )
#end def main

main(int(  12345 ))