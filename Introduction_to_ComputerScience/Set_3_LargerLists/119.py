def main( t ) :
    leng = len( t )
    maks = -1
    mw = -1

    for i in range( leng ) :
        current = t[i][0]
        c = 1
        for j in range( 1,leng ) :
            if current == t[ i ][ j ] :
                c += 1
            else :
                current = t[ i ][ j ]
                c = 1
            if maks < c :
                maks = c
                mw = i
    return mw
#end def
T = [
    [8, 1, 2, 7, 5, 3, 6, 4, 9],
    [9, 4, 3, 6, 8, 7, 1, 8, 8],
    [6, 7, 5, 4, 9, 1, 2, 8, 3],
    [1, 5, 4, 3, 6, 8, 8, 9, 6],
    [3, 6, 9, 9, 1, 7, 7, 2, 1],
    [2, 8, 7, 4, 5, 2, 5, 3, 4],
    [5, 2, 1, 9, 7, 4, 2, 3, 7],
    [4, 3, 8, 5, 2, 6, 8, 4, 5],
    [7, 9, 6, 3, 1, 8, 1, 6, 9]
]
print( main( T )  )