
def fc( A ) :
	n = len( A )
	dp = [ 1 for _ in range( n ) ]

	def is_within( bigger , smaller ) :
		return bigger[0] <= smaller[0] and bigger[1] >= smaller[1]

	for i in range( 1 , n )  :
		for j in range( i-1 , -1 , -1 ) :
			if is_within( A[j] , A[i] ) :
				dp[i] = max( dp[j] +1, dp[i] )
	return n - dp[n-1]

A = [ (1,5) , (2,4) , (3,5) , (4,5) ]
print( fc( A ) )