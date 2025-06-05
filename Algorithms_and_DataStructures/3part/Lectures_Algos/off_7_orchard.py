
def orchard( T , m ) :
	S = sum( T )
	if S % m == 0 : return 0

	n = len( T )
	pre_sum = [ 0 for i in range( n ) ]
	pre_sum[0] = T[0]
	for i in range( 1 , n ) :
		pre_sum[i] = pre_sum[i-1]

	memo = {}
	# k - ile drzew jescze usunac
	def in_( i , k ) :
		if (i,k) in memo :
			return memo[ (i,k) ]
		if k == 0 :
			memo[ (i,k) ] = pre_sum[i]
			return pre_sum[i]

		res = 0
		if i >= k :
			res  += in_( i-1 , k )
		res += in_(i-1,k-1) + sum( T[i+1 : k+1] )

		memo[ ( i,k) ] = res
		return res

	for k in range( 1 , n ) :
		if in_( n-1 , k ) % m :
			return k


def orchard2( T, m ) :
	S = sum( T )
	if S % m == 0 :
		return 0  # Nie trzeba usuwać żadnych drzew

	r = S % m
	n = len( T )

	# dp[k][s] = czy można usunąć k drzew o sumie ≡ s mod m
	dp = [ [ False ] * m for _ in range( n + 1 ) ]
	dp[ 0 ][ 0 ] = True  # Usunięcie 0 drzew: suma ≡ 0 mod m

	for num in T :
		mod_num = num % m
		# Iterujemy od końca, aby uniknąć wielokrotnego użycia tego samego drzewa
		for k in range( n, -1, -1 ) :
			for s in range( m ) :
				if dp[ k ][ s ] :
					new_k = k + 1
					new_s = (s + mod_num) % m
					if new_k <= n :
						dp[ new_k ][ new_s ] = True

	for i in range( m ) :
		print( dp[i] , "\n" )
		
	# Szukamy najmniejszego k, gdzie dp[k][r] == True
	for k in range( 1, n + 1 ) :
		if dp[ k ][ r ] :
			return k

	return n  # W najgorszym przypadku usuwamy wszystkie drzewa (suma 0 jest podzielna przez m)

def orchard3( T , m ) :

	S = sum( T )
	if S % m == 0 : return 0

	while S % m != 0 :
		S -= 1

	n = len( T )
	dp = [ [False] * (S+1) for _ in range( n ) ]

	dp[0][0] = dp[0][T[0]] = True

	for i in range( 1 , n ) :
		for j in range( S+1 ) :
			if dp[i-1][j] :
				dp[i][j] = True
			elif j >= T[i] and dp[i-1][j - T[i]] :
				dp[i][j] = True


	for j in range( S , -1 , -1 ) :
		if dp[n-1][j] and j % m == 0 :
			cnt = 0
			i = n-1
			curr_j = j
			while i > 0 :
				#print( i , curr_j , T[i] ,  curr_j-T[i] , dp[i-1][curr_j-T[i]] , dp[i-1][curr_j] )
				if dp[i-1][curr_j-T[i]] :
					curr_j = curr_j - T[i]
					i -= 1
					cnt += 1
				else :
					i -= 1
			if dp[i][curr_j] and curr_j != 0 :
				cnt += 1
			break

	""" 
	print( cnt , i , curr_j )
	for i in range( n ) :
		for j in range( S+1 ) :
			if dp[i][j] :
				print(" ",end="")
			print(dp[i][j],end=" ")
		print()
	"""

	return n - cnt

def orchard4( T , m ) :

	S = sum( T )
	if S % m == 0 : return 0

	while S % m != 0 :
		S -= 1

	n = len( T )
	inf = float( "inf" )
	dp = [ [inf] * (S+1) for _ in range( n ) ]

	for j in range( S+1 ):
		dp[0][j] = 1
	dp[0][T[0]] = 0

	for i in range( 1 , n ) :
		for j in range( S+1 ) :
			if j >= T[i] and dp[i-1][j-T[i]] < dp[i][j] :
				dp[i][j] = dp[i-1][j-T[i]]
			if dp[i-1][j] + 1 < dp[i][j] :
				dp[i][j] = dp[i-1][j] + 1



	#	"""
	for i in range( n ) :
		print( dp[i], "\n" )
	#"""
	res = inf
	while S > 0 :

		res = min( dp[n-1][S] , res )
		S -= m

	return res


def orchard5( T , m ) :

	S = sum( T )
	if S % m == 0 : return 0

	S %= m

	n = len( T )
	inf = float( "inf" )
	dp = [ [inf] * (S+1) for _ in range( n ) ]

	for j in range( S+1 ):
		dp[0][j] = 1
	dp[0][T[0] % m] = 0

	for i in range( 1 , n ) :
		for j in range( S+1 ) :
			t_val = T[i] % m
			if j >= t_val and dp[i-1][j-t_val] < dp[i][j] :
				dp[i][j] = dp[i-1][j-t_val]
			if dp[i-1][j] + 1 < dp[i][j] :
				dp[i][j] = dp[i-1][j] + 1



	#	"""
	for i in range( n ) :
		print( dp[i], "\n" )
	#"""
	res = inf
	while S > 0 :

		res = min( dp[n-1][S] , res )
		S -= m

	return res

# 0 1 2 3 4 5 6
T = [2, 2, 7, 5, 1, 14, 7]
m = 7
# 2
"""
T = [2,7,5,3,1]
m = 10

T = [7,5,3,2]
m = 15
"""
print( orchard5( T , m ) )

#print( orchard2( T , m ) )