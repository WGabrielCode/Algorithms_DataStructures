import random

def parzysta( x ) :
    while x > 0 :
        if (x%10) % 2 == 0 :
            return False
        x //= 10
    return True
#end def

def main( n ) :
    T = [0 for i in range(N + 1)]
    for i in range(N + 1):
        T[i] = i+1000
        if parzysta( T[ i ] ) :
            return True
    return False
#end def

N = 1000
print( main( N ) )

