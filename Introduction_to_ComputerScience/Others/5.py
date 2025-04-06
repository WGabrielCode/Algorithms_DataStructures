def f( x ) :
	return float( x ** x - 2024 )
# end def

def root() :
	a = 3
	b = 6
	e = 1e-6
	c = a

	while abs( b - a ) >= e :
		c = (a + b) / 2

		if f( c ) * f( a ) > 0 :
			a = c
		else :
			b = c
	return c

# end def

print( round( float( root() ), 6 ) )
