# l-piersze l metrow lewego pasa
# p-pierwsze p metrwo prawego pasa
# k - pierwsze k pojazdow
# f(l,p,k) = czy da sie upakowac piersze k pojadow zeby zajac <=l na lewym pasie i <=p na prawym
# wynik zadania to argmax f( L,L,k) = True, k e {0,1....,n}

def ferry( A , L ) :
	mem = {}
	def f( left , right , k ) :
		if k == 0  :
			return True

		if left

def fl( A, L ) :
	mem = {}
	n = len( A )
	def dp( i, left, right ) :
		if i == n :
			return i
		res = i

		if left + A[ i ] <= L :
			res = max( res, dp( i + 1, left + A[ i ], right ) )

		if right + A[ i ] <= L :
			res = max( res, dp( i + 1, left, right + A[ i ] ) )
		return res
	return dp(0,0,0)

def prom_iteracyjnie( A, L ) :
	n = len( A )

	# dp[i][l] = True jeśli można ułożyć i aut, gdzie długość zajęta na lewym pasie to l
	dp = [ { } for _ in range( n + 1 ) ]
	dp[ 0 ][ 0 ] = 0  # na początku: 0 aut, 0 zajętego miejsca na lewym pasie, 0 na prawym

	for i in range( n ) :
		for left_len in dp[ i ] :
			right_len = sum( A[ :i ] ) - left_len  # reszta idzie na prawy pas
			car_len = A[ i ]

			# Próbujemy dać i-te auto na lewy pas
			if left_len + car_len <= L :
				if (left_len + car_len) not in dp[ i + 1 ] :
					dp[ i + 1 ][ left_len + car_len ] = (left_len, "left")

			# Próbujemy dać i-te auto na prawy pas
			if right_len + car_len <= L :
				if left_len not in dp[ i + 1 ] :
					dp[ i + 1 ][ left_len ] = (left_len, "right")

	# Szukamy największego i dla którego istnieje jakikolwiek stan
	max_i = 0
	for i in reversed( range( n + 1 ) ) :
		if dp[ i ] :
			max_i = i
			break

	# Rekonstrukcja ścieżki
	result = [ ]
	curr_left = list( dp[ max_i ].keys() )[ 0 ]  # dowolny możliwy stan
	for i in range( max_i, 0, -1 ) :
		prev_left, choice = dp[ i ][ curr_left ]
		result.append( choice )
		curr_left = prev_left

	result.reverse()
	return max_i, result


L = 7
A =[ 2,5,3,1,1]
A1 = [ 5,2,5,2]
print( fl( A1 , L ) )