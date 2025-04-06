def allin1( x ) :
	min_sum = float( 'inf' )
	best_pair = None

	for i in range( 1, x ) :
		for j in range( 1, x ) :
			a, b = i, j

			while b <= x :
				a, b = b, a + b
				if b == x :
					if min_sum > i + j :
						min_sum = i + j
						best_pair = (i, j)
	return best_pair
# end def
print( allin1( int( input() ) ) )
# 19 11 30
