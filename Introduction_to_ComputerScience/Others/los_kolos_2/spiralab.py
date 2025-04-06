def spirala(n) :
    t = [[0 for i in range(n)] for i in range(n)]
    z=1
    l = n
    x,y = 0,0
    while z <= n*n  :
        for _ in range( l-1 ) :
            t[x][y] = z
            y+=1
            z+=1

        for i in range( l -1) :
            t[x][y] = z
            x+=1
            z+=1

        for i in range( l-1 ) :
            t[x][y] = z
            y-=1
            z+=1

        for i in range( l -1) :
            t[x][y] = z
            x-=1
            z+=1
        x+=1
        y+=1
        l -= 2
        if l<=0:
            break
    return t
#end def

t = spirala( 5 )
for i in t :
    print( *i )

