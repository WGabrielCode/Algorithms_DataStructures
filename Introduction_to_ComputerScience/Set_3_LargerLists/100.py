def main( t , k ) :
    n = len( t )
    size = 3
    while n >= size :
        for x in range( n - size + 1 ) :
            for y in range( n - size + 1 ) :
                if t[ x ][ y ] * t[ x + size -1 ][ y ] * t[ x ][ y + size -1 ] * t[ x + size -1 ][ y + size -1 ] == k :
                    return True ,( y + y +size -1 )// 2 , ( x + x + size -1 ) // 2
        size += 2
    return False
#end def

T = [
    [4, 9, 8, 19, 4],
    [1, 6, 8, 1, 15],
    [1, 6, 3, 12, 3],
    [5, 6, 65, 69, 15],
    [4, 6, 3, 12, 4]
]
print( main( T , 256 ) )