def spirala( t ) :
    dir = [ ( 0,1 ) , ( 1,0 ) , ( 0,-1 ) , ( -1,0 ) ]
    dirindx = 0
    x , y = 0 , 0
    l = len( t )
    for i in range( 1, l*l +1 ) :
        t[ x ][ y ] = i
        endx , endy = x + dir[ dirindx ][ 0 ] , y + dir[ dirindx ][ 1 ]
        if endx < 0  or endx >= l or endy < 0 or endy >= l  or t[ endx ][ endy ] != 0 :
            dirindx = ( dirindx +1 ) % 4
            endx, endy = x + dir[dirindx][0], y + dir[dirindx][1]
        x , y = endx , endy
    return t

#end def

n = 10
T = [ [ 0 for _ in range( n ) ] for _ in range( n ) ]
T = spirala( T )
for i in range( len( T ) ) :
    for j in range( len( T[ 0 ] ) ) :
        print( T[ i ][ j ], end=" " )
    print()