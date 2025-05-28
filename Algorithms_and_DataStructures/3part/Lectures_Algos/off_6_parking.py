import math
def parking( X , Y ) :
	n = len( X )
	m = len( Y )

	def R( i , j ) :
		return abs( X[i] - Y[j] )
	dp = [ [ math.inf for _ in range( m )]  for _ in range( n ) ]

	dp[0][0] = R(0,0)

	for j in range( 1 , m ) :
		dp[0][j] = min( dp[0][j-1] , R(0,j) )

	for i in range( 1 , n) :
		for j in range( i , m ) :
			if j == i :
				dp[i][j] = dp[i-1][j-1] + R( i , j )
			else :
				dp[i][j] = min( dp[i-1][j] + R(i,j) , dp[i][j-1] )

	for row in dp :
		print( row )
	return dp[n-1][m-1]

X = [ 3,6,10,14 ]
Y = [ 1,4,5,10,11,13,17 ]
print( parking( X , Y ) )