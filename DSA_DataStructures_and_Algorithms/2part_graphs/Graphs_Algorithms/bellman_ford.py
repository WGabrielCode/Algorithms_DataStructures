def bellman_ford( G, start ) :
	n = len( G )
	parent = [ -1 for i in range( n ) ]
	d = [ 1e7 for i in range( n ) ]
	d[start] = 0

	for _ in range( n-1 ) :
		for u in range( n ) :
			for v , cost in G[u] :
				if d[v] > d[u] + cost :
					d[v] = d[u] + cost
					parent[v] = u

	for u in range( n ) :
		for v , cost in G[u] :
			if d[v] > d[u] + cost :
				return None
	return d,parent

G = [
	[ (1, 5), (2, 2) ],
      [ (3, 1) ],
      [ (1, 1), (3, 7) ],
      [ ]
    ]
s = 0
print( bellman_ford( G, s ) )
