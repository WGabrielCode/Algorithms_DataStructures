
def sub_sum( A , s ) :
	n = len( A )
	dp = [ [False for i in range( s+1 ) ] for i in range( n ) ]
	dp[0][0] = dp[0][ A[0] ] = True

	for i in range( 1 , n ) :
		for j in range( s+1 ) :
			if j == 0 :
				dp[i][j] = True

			else :
				if dp[i-1][j] :
					dp[i][j] = True
				else :
					if j>=A[i] and dp[i-1][ j-A[i] ] :
						dp[i][j] = True
	return dp[n-1][s]
A = [3,5,7]
s = 15
print( sub_sum( A , s ) )