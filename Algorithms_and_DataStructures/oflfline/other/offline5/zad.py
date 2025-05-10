from zadtesty import runtests

def goodknight( G, s, t ) :
	from queue import PriorityQueue
	def M_to_adj() :
		n = len( G )
		A = [ [ ] for i in range( n ) ]
		for i in range( n ) :
			for j in range( n ) :
				if G[ i ][ j ] != -1 :
					A[ i ].append( (G[ i ][ j ], j) )
		return A

	n = len( G )
	inf = float( "inf" )
	G = M_to_adj()

	d = [ inf ] * n
	d[ s ] = 0
	no_sleep = [ 0 ] * n
	pq = PriorityQueue()
	pq.put( (0, s , d ) )
	while not pq.empty() :
		dist, u = pq.get()
		for cost, v in G[ u ] :
			sleep_cost = 0
			if no_sleep[ u ] + cost > 16 :
				sleep_cost = 8

			if d[ v ] > d[ u ] + cost + sleep_cost :
				d[ v ] = d[ u ] + cost + sleep_cost
				if sleep_cost == 8 :
					no_sleep[ v ] = cost
				else :
					no_sleep[ v ] = no_sleep[ u ] + cost
				pq.put( (d[ v ], v) )
	return d[ t ]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
