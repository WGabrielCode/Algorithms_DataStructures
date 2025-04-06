def rook(n, l):
    def fun(n, l, y,x, cnt) :
        mini = float('inf')
        if x == y == n-1:
            return cnt
        for i in range( y+1 ,n ) :
            if ( i,x ) in l :
                break
            mini = min( mini , fun( n,l,i,x,cnt+1))
        for j in range(x+1,n) :
            if ( y,j ) in l :
                break
            mini = min( mini , fun( n,l,y,j,cnt+1) )
        return mini
    #end def fun
    res = fun(n, l, 0, 0, 0)
    if res == float('inf') :
        return None
    else :
        return res
#end def
L = [ (0,4),(4,0)]

print( rook(4,L ))