def main( t ) :
    l = len( t )
    c = 1
    maxc = -2
    r = None

    for i in range( 1 , l ) :
        if c == 1 :
            r = t[ i ] - t[ i-1 ]
            c += 1
            continue
        if t[ i ] - t[ i-1 ] == r :
            c+=1
        else :
            if maxc < c :
                maxc = c
            c = 1
    return maxc
#end def

T = [2, 3, 4, 5, 6, 7, 16, 15, 16, 15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
print(main(T))