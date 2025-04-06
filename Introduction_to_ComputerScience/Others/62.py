def is_prime( x ):
    if x < 2 :
        return False
    i=2
    while i * i <= x :
        if x % i == 0 :
            return False
        i+=1
    return True
#end def

def sito( n ) :
    arr = [True for i in range( n+1 )]

    for i in range( 2 , n+1 ):
        if arr[i] :
            if is_prime( i ) :
                for j in range( i+i , n+1 , i ) :
                    arr[j] = False

    for i in range( 2 , n+1 ):
        if arr[i] :
            print(i , end = " " )
#end def

sito( 1000 )