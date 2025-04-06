def podz( x ) :
	i = 1
	sum = 0
	while (i < x) :
		if x % i == 0 :
			sum += i
		i += 1
	return sum


# end def

def main( a, b ) :
	if a == podz( b ) and b == podz( a ) :
		return True
	return False


# end def

print( (main( 220, 284 )) )
