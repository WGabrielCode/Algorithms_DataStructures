#classical knapsack problem 0/1

def Knapsack_Problem( w , T ) :
	T_size = len( T )
	K = [ [ 0 for _ in range(w+1)] for _ in range( T_size ) ]

	for i in range( T_size) :
		for curr_w in range( 1 , w+1 ) :
			weight , val = T[i]

			if i == 0 :
				if weight >= curr_w :
					K[i][curr_w] = val

			else :
				if weight > curr_w :
					K[i][curr_w] = K[i-1][curr_w]
				else :
					K[i][curr_w] = max( K[i-1][curr_w] , val + K[i-1][curr_w-weight] )
	for i in range( T_size ):
		print( K[i] ,"\n" )

	return K[T_size-1][w]

def Knapsack_memo( w , T ) :
	n = len( T )
	memo = {}

	def in_knapsack( i , w ) :

		if (i,w) in memo : return memo[(i,w)]

		curr_w , curr_val = T[i]

		if w == 0 :
			memo[(i,w)] = 0
			return 0

		if i == 0 :
			res = 0
			if curr_w >= w :
				res = T[i]
			memo[(i,w)] = res
			return res

		res = 0
		if curr_w >= w:
			res = max( )
		else : possible_val = curr_val

		memo[ (i,w) ] = max( in_knapsack(i,w-1) + possible_val , in_knapsack( i-1,w) )





	return in_knapsack( n , w )

def knapsack_P2( w , T ) :
	n = len( T )
	dp = [ [0] * (w+1) for _ in range( n ) ]

	for j in range( w+1 ) :
		curr_w , curr_v = T[0]
		if curr_w <= j :
			dp[0][j] = curr_v

	for i in range( n ) :

		curr_w , curr_v = T[i]
		for j in range( w+1 ) :

			if j == 0 :
				dp[i][j] = 0
			else :
				if curr_w == j:
					dp[i][j] = max( dp[i-1][j] , curr_v )
				elif curr_w < j :
					dp[i][j] = max( dp[i-1][j-curr_w] + curr_v , dp[i-1][j] )
	for i in range( n ) :
		print( dp[i] , "\n" )
	return dp[n-1][w]

def Knapsack_Problem_deepSeek_testing( w, T ) :
	T_size = len( T )
	K = [ [ 0 for _ in range( w + 1 ) ] for _ in range( T_size ) ]

	for i in range( T_size ) :
		weight, val = T[ i ]
		for curr_w in range( 1, w + 1 ) :
			if i == 0 :
				if weight <= curr_w :  # POPRAWIONE: <= zamiast >=
					K[ i ][ curr_w ] = val
			else :
				if weight > curr_w :
					K[ i ][ curr_w ] = K[ i - 1 ][ curr_w ]
				else :
					K[ i ][ curr_w ] = max( K[ i - 1 ][ curr_w ], val + K[ i - 1 ][ curr_w - weight ] )

	for i in range( T_size ) :
		print( K[ i ] )

	return K[ T_size - 1 ][ w ]
bc_w = 12
T = [ (1,6), (2,10), (3,12), (4,20), (2,5) ,(3,9) ]
# w , val

print( knapsack_P2( bc_w , T ) )
#print( Knapsack_Problem_deepSeek_testing( bc_w , T ) )
