def szybkiepot( a , b ) :

    r = 1
    while( b != 0 ) :
        if b % 2 == 1 :
            r *= a
        b //= 2
        a *= a
    return r
#end def
a , b = 5 , 11
print( a**b)
print( szybkiepot( a , b ) )

