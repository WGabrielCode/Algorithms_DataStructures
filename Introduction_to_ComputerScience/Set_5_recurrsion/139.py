def is_res( x ) :
    if x == 1 :
        return True
    if x % 2 == 0  :
        return is_res( x//2 )
    if x % 3 == 0 :
        return is_res( x//3 )
    if x % 5 == 0  :
        return is_res( x//5 )
    return False
#end def

def main( x ):
    c = 0
    for i in range( 1 , x+1 ) :
        if is_res( i ) :
            c += 1
            print( i , end = " ")
    return c
#end def
print( main( 10 ) )