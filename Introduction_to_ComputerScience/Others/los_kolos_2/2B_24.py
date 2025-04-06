def A( x ) :
    suma = 1
    for i in range( 2 , x ) :
        if x % i == 0 :
            suma += i
    return suma
#end def A

def B( x ) :
    a = 1
    b = 2
    while x > a :
        a , b = b , a+b
    if x == a :
        return b
    return a
#end def B

def C( x ) :
    y = 0
    while x > 0:
        y = y * 10 + x % 10
        x //= 10
    return x + y
#end def C

def cycle( x,n ) :

    def fun( x , n , y , cnt ) :

        if cnt > 1 and x == y :
            return cnt
        if cnt == n :
            return 0

        a = fun( x , n , A( y ) , cnt+1 )
        b = fun( x , n , B( y ) , cnt+1 )
        c = fun( x , n , C( y ) , cnt+1 )

        return max( a , b , c )

    #end def fun
    return fun( x , n , x , 0 )
#end def cycle

print( cycle( 29,6 ) )