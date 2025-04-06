def isit( x ) :
	a, b = 1, 1
	s = 2
	while b - a <= x :
		a, b = b, a + b
		s += b
		if s > x :
			return False
		if s == x :
			return True
	return False


def main( n ) :
	return isit( n )


print( main( int( input() ) ) )
