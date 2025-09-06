from egz2Atesty import runtests

def kingnqueen( V, E, D, K, Q, B ) :
	def Edges_to_adj() :
		for u, v in E :
			A[ u ].append( v )
			A[ v ].append( u )

	A = [ [ ] for i in range( V ) ]
	Edges_to_adj()

	def dfs_tarjan( u, parent ) :
		visited[ u ] = True
		nonlocal time
		nonlocal ap
		nonlocal root_children

		d[ u ] = low[ u ] = time
		time += 1

		for v in A[ u ] :
			if v == parent :
				continue
			if not visited[ v ] :
				if parent == -1 :
					root_children += 1

				dfs_tarjan( v, u )
				low[ u ] = min( low[ u ], low[ v ] )

				if parent != -1 and low[ v ] >= d[ u ] :
					if not used[ u ] :
						used[ u ] = True
						ap[u] = 0
			else :
				low[ u ] = min( low[ u ], d[ v ] )

	d = [ -1 ] * V
	low = [ -1 ] * V
	visited = [ False ] * V
	used = [ False ] * V
	time = 0
	ap = {}

	for u in range( V ) :
		if not visited[ u ] :
			root_children = 0
			dfs_tarjan( u, -1 )
			if root_children > 1 :
				if not used[ u ] :
					used[ u ] = True
					ap[u] = 0

	def dfs( u ) :
		nonlocal id
		group_id[u] = id
		visited[ u ] = True
		for v in A[u] :
			if not visited[v] and not (v in ap) :
				dfs( v )

	visited = [False] * V
	group_id = {}
	id = -1
	for u in range( V ) :
		if not visited[u] and not( u in ap)  :
			id += 1
			dfs( u )

	result = 0
	for i in range( D ) :
		k = K[i]
		q = Q[i]
		print( group_id.items() , k , q )
		if group_id[k] == group_id[q] :
			result += 1

	return result
	return group_id.items()


V = 9
E = [ (0, 1), (0, 2), (2, 1), (2, 3), (5, 2), (4, 2), (3, 4), (4, 5), (5, 6), (8, 6), (7, 8), (6, 7) ]
D = 3
K = [ 0, 5, 7 ]
Q = [ 3, 6, 0 ]
B = [ 2, 2, 5 ]

print( kingnqueen( V, E, D, K, Q, B) )

#runtests( kingnqueen, all_tests = True )
