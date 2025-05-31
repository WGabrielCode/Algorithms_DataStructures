
def pp( A ) :

	target = sum( A )
	if target % 2 != 0 :
		return False
	else :
		target //= 2

	n = len( A )
	dp = [ [False]*(target+1) for _ in range( n ) ]

	for i in range( n ):
		if A[i] > target :
			return False

	dp[0][A[0]] = dp[0][0] = True

	for i in range( 1 , n ) :
		for j in range( target+1 ) :
			if dp[i-1][j] :
				dp[i][j] = True
			elif A[i] <= j :
				dp[i][j] = dp[i-1][j-A[i]]
		if dp[i][target] :
			return True
	#"""
	for i in range( n ) :
		for j in range( target+1 ) :
			print( dp[i][j], end=" " )
		print( "\n" )
	#"""
	return dp[n-1][target]


A = [ 3,1,1,2,2,1 ]
B = [ 2,2,8 ]
print( pp( A ) )