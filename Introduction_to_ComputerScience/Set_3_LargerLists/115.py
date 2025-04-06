def rozklad( x ) :
    arr = [ 0 for _ in range( x ) ]
    i = 2
    while x > 1 :
        if x % i == 0 :
            while x % i == 0 :
                x //= i
                arr[ i-1 ] += 1
        i += 1
    return arr
#end def
def main( t ) :
    leng = len( t )
    ws = [ [ -1 for _ in range( leng ) ] for _ in range( leng ) ]
    for i in range( 1, leng -1 ) :
        for j in range( 1, leng -1 ) :
            if ws[ i -1 ][ j ] == -1 :
                ws[ i -1 ][ j ] = rozklad( t[ i -1 ][ j ] )
            if ws[ i ][ j +1 ] == -1 :
                ws[ i ][ j +1 ] = rozklad( t[ i ][ j +1 ] )
            if ws[ i ][ j -1 ] == -1 :
                ws[ i ][ j -1 ] = rozklad( t[ i ][ j -1 ] )
            if ws[ i +1 ][ j ] == -1 :
                ws[ i +1 ][ j ] = rozklad( t[ i +1 ][ j ] )

#end def
T = [
    [5, 6, 8, 12, 15],
    [10, 9, 8, 12, 15],
    [6, 6, 9, 12, 15],
    [12, 6, 8, 12, 15],
    [1, 6, 36, 12, 16]
]
print(main(T))