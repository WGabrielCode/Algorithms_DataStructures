def spirala( t ) :
    l = len( t )
    maxz = l* l
    x , y , z = 0 , 0 , 1

    while z <= maxz :
        print(l)
        for _ in range( l - 1 ) :
            t[ x ][ y ] = z
            y +=1
            z += 1
        for _ in range(l - 1):
            t[x][y] = z
            x += 1
            z += 1
        for _ in range(l - 1):
            t[x][y] = z
            y -= 1
            z += 1
        for _ in range(l - 1):
            t[x][y] = z
            x -= 1
            z += 1
        x += 1
        y += 1
        l -= 2
    return t
#end def

n = 6
T = [[0 for _ in range(n)] for _ in range(n)]
T = spirala(T)
for i in range(len(T)):
    for j in range(len(T[0])):
        print(T[i][j], end=" ")
    print()