def fun ( x ) :
    while x != 1:
        if x==4 :
            return False
        suma=0
        while x > 0 :
            suma += ( x%10 ) ** 2
            x //= 10
        x = suma
    return True
#end def

def is_prime ( x ):
    if x < 2 :
        return False
    i = 2
    while ( i * i <= x ) :
        if x % i == 0 :
            return False
        i+=1
    return True

def main ( u , l , k ) :
    for i in range ( u, l+1 ) :
        if is_prime( i ) and fun( i ) :
            k -= 1
        if k == 0 :
            return i
#end def
print (main( 1, 100000, 5 ) )
