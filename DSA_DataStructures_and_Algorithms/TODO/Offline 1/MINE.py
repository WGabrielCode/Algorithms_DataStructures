def maze( L ) :

	n = len( L )
	B = [ [-1 for i in range( n ) ] for i in range( n ) ]

	def check_tile_i( i , j ) :
		return i >= 0 and i < n and B[i][j] != -1 and L[i][j] == "."

	def check_tile_j(j,i) :
		return (i >= 0 and i < n and B[j][i] != -1 and L[j][i] == "." )

	def in_( i , j , B , res ) :
		if i == j == len( B )  - 1 :
			return res


			B[i-1][j] =
			in_( i-1 , j , B , )


	res = []
	in_( 0 , 0  , B , res )

L = [ "....","..#.", "..#.", "...." ]
print( maze( L ) )