def is_in( x ) :
	a, b = 1, 1
	s = 1
	first = 1
	while a <= x :
		if s == x :
			return True
		elif s < x :
			s += b
			a, b = b, a + b
		else :
			s -= first
			first = a
	return False


# Test cases
print( is_in( 1 ) )  # True
print( is_in( 2 ) )  # True
print( is_in( 3 ) )  # True
print( is_in( 4 ) )  # False
print( is_in( 5 ) )  # True
print( is_in( 6 ) )  # False
print( is_in( 7 ) )  # True
print( is_in( 8 ) )  # True
print( is_in( 9 ) )  # False
print( is_in( 10 ) )  # True
