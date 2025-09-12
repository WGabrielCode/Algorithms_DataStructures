def LIS( A ) :
	def F_to_x( x ) :
		for i in range( x-1 , -1 , -1 ) :
			if A[i] < A[x] :
				F[x] = max( F[i]+1 , F[x] )
	n = len( A )
	F = [1] * n
	for i in range( 1 , n ) :
		F_to_x( i )
	return max( F )

def lis_list( A ) :
	n = len( A )
	dp = [-1] * n

	def in_list( i ) :
		if dp[i] != -1 :
			return dp[i]

		if i == 0 :
			dp[0] = 1
			return 1

		dp[i] = 1
		for j in range( i ) :
			if A[i] > A[j] :
				dp[i] = max( dp[i] , in_list( j ) + 1 )

		return dp[i]
	in_list( n-1 )
	return max( dp )

def lis_memo( A ) :
	memo = {}
	def in_lis( i ) :

		if i in memo :
			return memo[i]

		if i == 0 :
			memo[i] = 1
			return 1

		memo[i] = 1
		for j in range( i) :
			if A[i] > A[j] :
				memo[i] = max( memo[i] , in_lis( j ) +1 )
		return memo[i]

	in_lis( len( A ) - 1 )
	return max( memo.values() )

A = [2,1,4,3,4,8,5,7]
B = [6,5,4,3,2,1]
print( lis_list(  A ) )
print( lis_memo( A ) )
print( LIS( A ) )