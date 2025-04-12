# z kazdego mozna do niego dojsc a zniego nie da sie wyjsc na macierzy
def stream( G ) :
	n = len( G )
	candidate = 0

	for v in range( 1, n ) :
		if G[ candidate ][ v ] == 1 :
			candidate = v

	for v in range( n ) :
		if G[ candidate ][ v ] == 1 :
			return None


	for v in range( n ) :
		if v != candidate and G[ v ][ candidate ] == 0 :
			return None

	return candidate


G1 = [ [ 0, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 1, 1, 0, 0 ], [ 1, 1, 0, 0 ] ]

G2 = [ [ 0, 1, 1, 1 ], [ 1, 0, 0, 0 ], [ 0, 1, 0, 0 ], [ 1, 1, 0, 0 ] ]

print( stream( G1 ) )
print( stream( G2 ) ) # Powinno zwrócić None