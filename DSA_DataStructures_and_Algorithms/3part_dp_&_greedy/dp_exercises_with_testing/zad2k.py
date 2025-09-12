from zad2ktesty import runtests

def palindrom( S ):
    n = len( S )
    #R = [ S[i] for i in range( n ) ]

    R = [1] * n
    max_v = -float("inf")

    def check( left , right , res ) :
        while left >= 0 and right < n :
            if S[left] != S[right] :
                break
            res += 2
            left -= 1
            right += 1
        return res

    for i in range( 1 , n ) :
        R[i] = max( R[i] , check( i-1 , i+1 , 1 ) , check( i-1 , i , 0 ) )
        if max_v < R[i] :
            max_v = R[i]

    return max_v

S = "aacaccabcc"
print( palindrom( S ) )

#runtests ( palindrom )