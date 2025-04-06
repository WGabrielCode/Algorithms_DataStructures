from math import sqrt

def main( m , n )  :
    m = int ( (sqrt(m) - int(sqrt(m) ) ) * 10**n )
    suma = 0

    while m > 0 :
        suma += m % 10
        m //= 10

    return suma
#end def

print ( main ( 5 , 6 ) )