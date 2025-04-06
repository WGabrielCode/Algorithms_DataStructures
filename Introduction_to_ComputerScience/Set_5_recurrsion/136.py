def res( t , w , k, c = 1 ) :
    leng = len( t )

    if c == leng * leng :
        return True

    moves = [ ( -1,-2 ) , ( 1,-2 ) , ( -1,2 ) ,
    ( 1,2 ) , ( -2,-1 ) , ( -2,1 ) , ( 2,-1 ) , ( 2,1 ) ]

    for pw , pk in moves :
        nw = w + pw
        nk = k + pk
        if nw >= 0 and nk >= 0 and nw < leng and nk < leng and t[ nw ][ nk ] :
            t[ nw ][ nk ] = False
            if res( t , nw , nk , c+1 ) :
                return True
            t[nw][nk] = True
    return False
#end def

def chess( n , w , k ) :
    t = [ [True for _ in range( n ) ] for _ in range( n ) ]
    t[ w ][ k ] = False
    return res( t , w , k )
#end def

print( chess( 5 , 0 , 0 ) )
