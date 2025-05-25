
def mm( ML ) :

	n = len( ML ) - 1
	dp = [ [ 0 for i in range( n+1 ) ] for i in range( n+1 ) ]

	for l in range( 2 , n + 1 ) :

		for i in range( 1 , n - l +2 ) :
			j = i + l-1
			dp[i][j] = float( "inf" )
			for k in range( i , j ) :
				cost = dp[i][k] + dp[k+1][j] + ML[i-1]*ML[k]*ML[j]
				if cost < dp[i][j] :
					dp[i][j] = cost
	return dp


ML = [ 1,2,5,7,10 ]
print( mm( ML ) )