def zlozona( x ) :
    if x <= 2 :
        return False

    if x == 3 or x == 5 :
        return False

    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 :
        return True
    i = 5
    while i * i <= x :
        if x % i == 0 or x % ( i + 1 ) == 0 :
            return True
        i += 6
    return False
#end def

count = 0
def main( a  , b , r = 1 ) :
    global count
    if a <= 0 or b < 0 :
        return
    if a -1 == b == 0  :
        if zlozona( r )  :
            count  += 1
        else :
            return

    main( a-1 , b, 2*r + 1  )
    main( a , b-1 , 2*r )

main( 2,3 )
print( count )