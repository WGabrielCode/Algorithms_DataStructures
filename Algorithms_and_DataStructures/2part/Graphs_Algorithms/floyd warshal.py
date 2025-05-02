def floyd_warshall( graph ) :
	n = len( graph )
	dist = [ [ graph[ i ][ j ] for j in range( n ) ] for i in range( n ) ]


	for k in range( n ) :
		for i in range( n ) :
			for j in range( n ) :

				if dist[ i ][ j ] > dist[ i ][ k ] + dist[ k ][ j ] :
					dist[ i ][ j ] = dist[ i ][ k ] + dist[ k ][ j ]

	return dist

inf = float( 'inf' )
G = [
	  [ 0 , 5 , inf, 10 ],
      [ inf , 0 , 3 , inf ],
      [ inf , inf , 0 , 1 ],
      [ inf , inf , inf , 0 ]
	]
print( floyd_warshall( G ) )