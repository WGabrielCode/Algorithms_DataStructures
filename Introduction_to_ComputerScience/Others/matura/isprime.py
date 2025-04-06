def is_prime ( x ) :
    if x < 2 :
        return False
    i = 2
    while i * i <= x :
        if x % i == 0 :
            return False
        i+=1
    return True
#end def

print ( is_prime ( 69 ) )