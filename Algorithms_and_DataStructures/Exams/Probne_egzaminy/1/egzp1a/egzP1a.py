from egzP1atesty import runtests

# O(nm) recurrsion overflow :
def titanic_recurrent( W, M, D ) :

	inserted  = ""
	for i in range( len( W ) ) :
		inserted += ( M[ ord( W[i] ) - ord("A") ][1] )
	print( inserted )
	memo = {}
	def rec( i ) :

		if i >= len( inserted ) :
			return 0

		if i in memo :
			return memo[i]

		res = float( "inf" )

		for j in D :
			n = len( M[j][1] )
			if inserted[i:i+n] == M[j][1] :
				res = min( res , 1 + rec( i + n ) )

		memo[i] = res
		return res

	return rec( 0 )

# O(nm) dp solution 1.15sec
def titanic_dp( W, M, D ) :

	inserted  = ""
	for i in range( len( W ) ) :
		inserted += ( M[ ord( W[i] ) - ord("A") ][1] )

	minus = []
	dot = []
	for i in D :
		if M[i][1][0] == "-" :
			minus.append( M[i][1] )
		else :
			dot.append( M[i][1] )

	dot.sort( key = len )
	minus.sort( key = len )

	n = len( inserted )
	inf = float("inf")
	dp = [inf] * n

	for i in range( n-1 , -1 , -1 ) :
		if inserted[i] == "." :
			max_len = n - i
			for code in  dot :
				if len(code) <= max_len :
					if inserted[i : i + len( code )] == code :
						possible_rest = dp[i+len(code)] if i+len(code) < len( inserted ) else 0
						dp[i] = min( dp[i] , 1 + possible_rest )
		else :
			max_len = n - i
			for code in minus :
				if len( code ) <= max_len :
					if  inserted[ i : i + len( code ) ] == code :
						possible_rest = dp[ i + len( code ) ] if i + len( code ) < len( inserted ) else 0
						dp[ i ] = min( dp[ i ], 1 + possible_rest )
				else :
					break
	return dp[0]

# O(nm) ( runtime error )
def titanic_dict_dp( W, M, D ) :

	inserted  = ""
	for i in range( len( W ) ) :
		inserted += ( M[ ord( W[i] ) - ord("A") ][1] )

	memo = {}
	for i in D :
		memo[ M[i][1] ] = 0

	n = len( inserted )
	inf = float("inf")
	dp = [inf] * n


	for i in range( n-1 , -1 , -1 ) :
		current_string = ""

		for j in range( i , n ) :
			current_string += inserted[j]
			if current_string in memo :
				possible_rest = dp[j+1] if j+1 < len( inserted ) else 0
				dp[i] = min( dp[i] , 1 + possible_rest )
	return dp[0]

def titanic( W, M , D ) :

#"""
W = "SOS"
D = [0, 4, 13, 19, 25]
M = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'),
('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
('S', '...'), ('T', '-'), ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
('Y', '-.--'), ('Z', '--..')]

print( titanic( W, M, D ) )
#"""

runtests( titanic, recursion = False )
