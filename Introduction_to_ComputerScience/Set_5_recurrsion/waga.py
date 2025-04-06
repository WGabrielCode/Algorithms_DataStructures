
def waga( t , n , p=0 ) :
    if n == 0 :
        return True
    if p == len( t ) :
        return False
    return waga( t, n-t[ p ], p+1 ) or waga( t, n, p+1 ) or waga( t, n + t[ p ] , p+1 )
#end def

T = [ 1,3,9,17,81 ]
#T = [ 1,2,4,8,16,32]
for w  in range( 1,122) :
    print( w, waga( T, w ) )