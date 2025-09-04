from egzP4atesty import runtests 

#O( n^2 ) runtime error
def mosty_2 ( T ):

    T.sort(  )
    n = len( T )
    dp = [1] * n

    for i in range( 1 , n ) :
        for j in range( i ) :
            if T[i][1] > T[j][1] :
                dp[i] = max( dp[i] , dp[j]+1 )

    return max( dp )
"""
Orientacyjny łączny czas : 0.26 sek.
Status testów: A A A A A A A A A A
O(nlogn)
"""
def mosty ( T ):

    T.sort()
    n = len( T )

    result = []

    def search( x ) :
        left = 0
        right = len( result )

        while left <= right :

            if left == right  :
                return left

            mid = (left+right) // 2
            if result[mid] <= x :
                if result[mid] == x :
                    return mid
                left = mid + 1
            else :
                right = mid

    for i in range( n ) :
        val = T[i][1]
        idx = search( val )
        if idx == len( result ) :
            result.append( val )
        else :
            result[idx] = val

    return len( result )

"""
T = [ (1, 2), (2, 3), (3, 0) ,(1,0),(10,100),(12,12) ]
print( mosty( T ) )
"""

runtests ( mosty, all_tests=True  )