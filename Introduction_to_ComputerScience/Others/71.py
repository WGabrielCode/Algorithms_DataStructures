def dodatni( t , b ) :
    r = None
    c = 1
    maxc = 1
    l = len( t )
    for i in range( 1 , l ) :
        if c == 1 :
            r = t[ i ] - t[ i-1 ]
            if (b and r > 0) or ( not b and r < 0 ) :
              c += 1
            continue
        if t[ i ] - t[ i-1 ] == r :
            c += 1
        else :
            if maxc < c :
                maxc = c
            c = 1
    if maxc < c:
        maxc = c
    return maxc
#end def
def main( t ) :
    print( dodatni( t , True ) )
    print(dodatni(t, False))
    return (dodatni( t , True ) - dodatni( t , False ))
#end def

T = [ 1,2,3,4,5,6,7,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
print( main( T ) )



