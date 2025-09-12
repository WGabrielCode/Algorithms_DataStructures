def suma( x , l) :
    s=0
    while x > 0 :
        s+= (x%10)**l
        x //= 10
    return s
#end def

def fun( x, l) :
    if x == suma( x, l ) :
        return True
    return False
#end def

def main( x ) :
    i = 10**(x-1)
    max = 10**(x)
    while i < max :
        if fun( i , x ) :
            print( i , end = " " )
        i+=1
#end def

main( 3 )
