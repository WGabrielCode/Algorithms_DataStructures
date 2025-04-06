def rozklad( x ) :
    arr = [ 0 for _ in range( x ) ]
    i = 0
    j = 2
    while x > 1 :
       if( x % j == 0 ) :
           arr[i] = j
           i += 1
           while x % j == 0 :
               x //= j
       j += 1
    return arr[ 0:i ]
#end def

def main( n , t ) :
    access = [ False for _ in range( n ) ]
    access[ 0 ] = True

    for i in range( n ) :
        if access[ i ] :
            for j in rozklad( t[ i ] ) :
                if i+j < n :
                    access[ i+j ] = True
    if access[ n-1 ] == True :
        return True
    return False
#end def

T = [2,3,4,5,6,7,16,12,10,11]
print( main( len( T ) , T ) )