from math import log
from math import floor

def isubseq( x ) :
    l = floor( log( x , 10 ) ) + 1
    for i in range( floor( log( x , 10 ) ) + 1 ) :
        #for j in reversed( range( 1 , floor( log( x , 10 ) ) + 2) )  :
        for j in range( floor( log( x , 10 ) )+ 1 , 0 , -1) :
            print( x % 10**j )
        x //= 10
#end def

def subarrays(arr):
    n = len(arr)
    z=0
    result = [0 for _ in range( (1 + n ) * n // 2 ) ]
    for i in range(n):
        for j in range(i + 1, n + 1):
            result[ z ] = arr[ i : j ]
            z += 1
    return result
def is_prime( x ) :
    if x < 2 :
        return False
    if x == 2 or x == 3 or x == 5 :
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 :
        return False
    i = 5
    while i * i <= x :
        if x % i == 0 or x % ( x+ 2 ) == 0 :
            return False
        i += 6
    return True
#end def

for i in range( 100 ) :
    if is_prime( i ) :
        print( i )


#print( isubseq( 123456 ))

print( subarrays( str(123456) ) )