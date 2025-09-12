from zad7ktesty import runtests 

def ogrodnik (T, D, Z, l):
    n = len( D )
    def dfs( i , j ) :
        N = len( T )
        M = len( T[0] )

        res = T[i][j]
        T[i][j] = 0

        if i-1 >= 0 and T[i-1][j] != 0 :
            res += dfs( i-1 , j )
        if i + 1 < N and T[ i + 1 ][ j ] != 0 :
            res += dfs( i + 1, j )
        if j-1 >= 0 and T[i][j-1] != 0 :
            res += dfs( i , j-1 )
        if j+1 < M and T[i][j+1] != 0 :
            res += dfs( i,j+1 )

        return res

    #zmiana tablicy D na sume wartosci korzeni
    for i in range( n ) :
        D[i] = dfs( 0 , D[i] )
    #print( D )
    dp = [ [0] * (l+1) for i in range( n ) ]
    # D-cost , Z - val , l - max_cost
    for i in range( D[0] , l+1 ):
        dp[0][i] = Z[0]

    for i in range( 1 , n ) :
        for j in range( 1 , l+1 ) :
            if D[i] <= j :
                dp[i][j] = max( dp[i-1][j-D[i]] + Z[i] , dp[i-1][j] )
            else :
                dp[i][j] = dp[i-1][j]
    """
    for i in range( n ) :
        print( dp[i] )
    """
    return dp[n-1][l]

D = [4, 9, 12, 16]
Z = [13, 11, 15, 4]
l = 32
T = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 6, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 3, 1, 0, 0, 2, 2, 2, 0, 2, 4, 2, 0],
    [0, 0, 0, 1, 2, 0, 0, 1, 4, 6, 0, 2, 1, 3, 0, 0, 3, 1, 0, 0]
]
#print( ogrodnik( T,D,Z,l ) )
runtests( ogrodnik, all_tests=True )
