def sudoku ( t ) :
    for i in range

T = [[0] * 9 for _ in range ( 9) ]
for j in range ( 9 ) :
    num = input()
    for i in range ( 9 ) :
        T[i][j] = int ( num[ i * 2 ] )
print ( sudoku(T) )
"""
for i in range ( 9 )  :
    for j in range ( 9 ) :
        print ( T[i][j], end = ' ' )
    print ()
"""