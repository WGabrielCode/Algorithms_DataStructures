def lets_roll( start_City, flights, resorts ) :
	from queue import PriorityQueue

	def v_cnt( flights ) :
		m_v = -1
		for u, v, cost in flights :
			m_v = max( m_v, u, v )
		return m_v + 1

	def e_to_adj( n ) :
		G = [ [ ] for i in range( n ) ]
		for u, v, cost in flights :
			G[ u ].append( (v, cost) )
			G[ v ].append( (u, cost) )
		return G

	n = v_cnt( flights )
	G = e_to_adj( n )
	print( G )
	inf = float( "inf" )
	d = [ inf ] * n
	parent = [ -1 ] * n
	d[ start_City ] = 0
	pq = PriorityQueue()
	pq.put( (0, start_City) )
	is_resort_list = [ False ] * n
	for i in range( n ) :
		if i in resorts :
			is_resort_list[ i ] = True
	visited_resorts_cnt = 0


	while not pq.empty() :

		dist, u = pq.get()
		for v , cost in G[u] :

			if d[ v ] > d[ u ] + cost + cost :
				d[ v ] = d[ u ] + cost + cost
				if not is_resort_list[v] :
					pq.put( (d[ v ], v) )
	res = 0
	for u in range( n ) :
		if is_resort_list[u] :
			res += d[u]
	return res
start_city = 0
flights = [ (0, 1, 2), (0, 2, 4), (0, 3, 8), (3, 4, 16), (1, 4, 1), (2, 4, 1) ,( 1,5,1)  ,(4,5,1 )]
resorts = [ 1, 2, 4 ]
print( lets_roll( start_city, flights, resorts ) )
