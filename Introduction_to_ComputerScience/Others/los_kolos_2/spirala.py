def spirala( n )
    t = [[ 0 for i in range( n) ] for i in range(n ) ]

    dir = [ (0,1),(1,0),(0,-1),(-1,0) ]
    current = 0
    z = 1
    while z <= n*n :
        x , y = 0 , 0
        new_x = x + dir[current][0]
        new_y = y + dir[current][1]

        if new_y < 0 or new_y >=n or new_x < 0 or new_x >= n or t[new_x][new_y] != 0 :


