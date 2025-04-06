
def main( t ) :
    l = len( t )
    maxc = 0
    maxstart = 0
    maxkoniec = 0
    c , start = 1 , 0

    for i in range( 1, l ) :
        if t[ i-1 ] < t[ i ] :
            c += 1
        else :
            if maxc < c :
                maxc = c
                maxstart = start
                maxkoniec = i
            c, start = 1, i
    print( t[ maxstart : maxkoniec ] )
    return maxc
#end def

T = [2,3,4,9,6,7,16,15,10,11]
print( main( T ) )