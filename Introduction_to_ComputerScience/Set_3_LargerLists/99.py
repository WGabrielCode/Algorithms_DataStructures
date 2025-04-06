def main( t ) :
    leng = len( t )
    cmax = 0
    for i in range( leng - 2 ) :
        for j  in range( leng - 2 ) :
            c = 1
            x, y = i +1 , j +1
            q = t[ x ][ y ] / t[ i ][ j ]
            while x < leng and y < leng  :
                ck = t[ x ][ y ] / t [ x - 1 ][ y - 1 ]
                if  ck== q :
                    c += 1
                cmax = max( cmax , c )
                if ck != q :
                    break
                x , y = x + 1 , y + 1
    if cmax >= 3 :
        return True , cmax
    else :
        return False

#end def

T = [
    [5, 6, 8, 12, 15],
    [1, 9, 8, 12, 15],
    [1, 6, 81, 12, 15],
    [1, 6, 8, 81*9, 15],
    [1, 6, 36, 12, 81*9*9]
]
print(main(T))