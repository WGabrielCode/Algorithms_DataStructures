from queue import PriorityQueue


def dijkstra2( G, start, stop ) :
	n = len( G )
	parent = [ -1 for i in range( n ) ]
	d = [ 1e7 for i in range( n ) ]
	d[ start ] = 0

	pq = PriorityQueue()
	pq.put( (0, 1e7, start) )

	while not pq.empty() :
		dist, last_cost, u = pq.get()
		if dist > d[ u ] :
			continue
		for v, cost in G[ u ] :
			if last_cost > cost :
				if d[ v ] > d[ u ] + cost :
					parent[ v ] = u
					d[ v ] = d[ u ] + cost
					pq.put( (d[ v ], dist, v) )
	print( parent, d )



G = [ [ (1, 5), (2, 4) ], [ (3, 1) ], [ (1, 1), (3, 7) ], [ ] ]

s = 0
dijkstra2( G, s, 2 )
