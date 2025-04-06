def spirala( l ) :
    t = [[0 for _ in range( l ) ] for _ in range( l )]
    dir = [ ( 0 , 1 ) , ( 1 , 0 ) , ( 0 , -1 ) ,( -1 , 0 ) ]
    dirindx = 0
    x , y = 0 , 0
    for i in range( 1, l * l + 1 ) :
       t[ x ][ y ] = i
       endx , endy = x + dir[ dirindx ][ 0 ] , y + dir[ dirindx ][ 1 ]
       if endx < 0 or endx >= l or endy < 0 or endy >= l or t[ endx ][ endy ] != 0 :
           dirindx = (dirindx + 1) % 4
           endx , endy  = x + dir[ dirindx ][ 0 ] , y + dir[ dirindx ][ 1 ]
       x , y = endx , endy
    return t
#end def
n =5
s = spirala( n )

for i in range( n ) :
    for j in range ( n ) :
        print( s[ i ][ j ] , end = " ")
    print( )