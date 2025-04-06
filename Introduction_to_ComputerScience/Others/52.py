def rozklad( x ) :
	s = 0
	i = 2
	while x > 1 :
		if x % i == 0 :
			while x % i == 0 :
				x //= i
				s += suma( i )
		i += 1
	return s


# end def

def suma( x ) :
	s = 0
	while x > 0 :
		s += x % 10
		x //= 10
	return s


# end def

def main( x ) :
	if suma( x ) == rozklad( x ) :
		return True
	return False


# end def

for i in range( 1, int( 1e2 ) ) :
	if main( i ) :
		print( i, end = " " )
