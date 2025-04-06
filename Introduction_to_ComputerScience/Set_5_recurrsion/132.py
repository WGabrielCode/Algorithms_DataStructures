def newton( n , k ) :
    if n == k:
        return 1
    if k == 1 :
        return n
    return newton( n-1 , k-1 ) + newton( n-1 , k )
#end def

print( newton( 12,6 ) )