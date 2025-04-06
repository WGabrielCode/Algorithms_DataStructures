def waga( x ) :
	c = 0
	i = 2
	while x > 1 :
		if x % i == 0 :
			while x % i == 0 :
				x //= i
			c += 1
		i += 1
	return c


def main( t, indx = 0, a = 0, b = 0, c = 0 ) :
	if indx == len( t ) * len( t[ 0 ] ) :
		return waga( a ) == waga( b ) == waga( c ) and a != 0 and b != 0 and c != 0

	row = indx // len( t[ 0 ] )
	col = indx % len( t[ 0 ] )

	return (main( t, indx + 1, a * 10 + t[ row ][ col ], b, c ) or main( t, indx + 1, a, b * 10 + t[ row ][ col ],
	                                                                     c ) or main( t, indx + 1, a, b,
	                                                                                  c * 10 + t[ row ][ col ] ))


T = [ [ 3, 6 ], [ 7, 9 ] ]
print( main( T ) )