def is_prob( t, i,j ) :
    leng = len( t )
    w =0
    k =0
    for x in range( leng ):
        for y in range( leng ) :
            if x != i and y != j :
                if t[x][y] :
                    return True
    return False
#end def is_prob

def move( t ) :
    leng = len( t )
    t_w = [ False for i in range( leng) ]
    t_k = [ False for i in range( leng) ]

    for i in range( leng ) :
        for j in range( leng ) :
            if t[i][j]:
                t_w[i] = True
                t_k[j] = True

    for i in range( leng ) :
        for j in range( leng ) :
            if t[i][j] and is_prob(t, i,j) :



