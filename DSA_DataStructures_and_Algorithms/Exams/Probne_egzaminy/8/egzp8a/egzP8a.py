from egzP8atesty import runtests 

def reklamyrec ( T, S, o ):
    n = len( T )
    T = [ (T[i][0],T[i][1] , S[i] ) for i in range( n ) ]

    T.sort()


    memo = {}
    def rec( finish , idx ) :
        if idx >= len( T ) :
            return 0

        key = ( finish , idx )
        if key in memo :
            return memo[key]

        next_start , next_finish , pay = T[idx]
        """
        nonlocal o
        if next_finish > o+1 : #or next_start > o :
            memo[key] = 0
            return 0
        """

        res = rec( finish ,idx+1 )

        if next_start > finish :
            res = max( pay + rec( next_finish , idx+1 ) , res )

        memo[key] = res
        return res

    return rec( -1 , 0 )


def reklamy( T, S, o ) :
    n = len( T )
    T = [ (T[ i ][ 0 ], T[ i ][ 1 ], S[ i ]) for i in range( n ) ]

    T.sort()

    dp = [0] * (o+100)
    dp[o+4] = float("inf")
    prev_finish = 0

    for start , finish , pay in T :

        for i in range( prev_finish , start ) :
            dp[i] = max( dp[i] , dp[max( 0 ,i-1 ) ] )

        dp[finish] = max( dp[finish-1] , ( dp[start-1] if start -1 >= 0 else 0 ) + pay )

    print( dp )
    return 2



T = [ (0, 3), (4, 5), (1, 4) ]
S = [ 5000, 3000, 15000 ]
o = 6
print( reklamy( T, S, o) )

runtests ( reklamy, all_tests = False )