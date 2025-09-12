
def min_cost( O,C,T,L ) :
	n = len( O )
	for i in range( n )	:
		C[i] = ( O[i] , C[i] )
	C = sorted( C , key = lambda x : x[0] )
	C.append( (L,0) )
	inf = float("inf")

	n += 1
	dp = [ [inf] * n for i in range( 2 ) ]

	used = False

	if C[0][0] == T :
		dp[0][0] = C[0][1]
	elif C[0][0] > T and C[0][0] <= 2*T :
		dp[0][0] = 0
		used = True

	min_i = 0
	for j in range( 1 , n ) :
		dist , cost = C[j]
		curr_dist = 0
		min_idx = dist - T
		for i in range( min_i , j ) :
			td , tc = C[i]
			if td < min_idx :
				min_i = i+1
			else :
				dp[0][j] = min( dp[0][j] , dp[0][i] + tc )
	if used :
		for `j in range( n ) :
			val , cost  = C[j]

	print( C )
	print( dp )
	return 0

O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25

print( min_cost(O, C, T, L) )