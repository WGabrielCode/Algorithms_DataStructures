def fun ( a ) :
    suma = 0
    while a > 0 :
        suma += a
        a //= 10
    return suma

def main ( s ) :
    for i in range ( s//10 , s ) :
        if fun ( i ) == s :
            return i
    return -1

print ( main( 1370 ) )