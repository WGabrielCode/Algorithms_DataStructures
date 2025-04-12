# policz liczbe spojncyh skaldowych

def how_many( G ) :

	def dfs( G , v ) :
		def dfsVisit( G ,v ) :
			nonlocal n
			visited[v] = True
			for u in G[v]  :
				if not visited[u] :
					dfsVisit( G , u )
		n = len( G )
		for u in G[v] :
			if not visited[ u ] :
				dfsVisit( G , u)
	n = len( G )
	visited = [ False for _ in range( n ) ]

	cnt = 0
	for v in range( n ) :
		if not visited[ v ] :
			dfs( G , v )
			cnt += 1
	return cnt


G = [ [ 0, 1, 3 ], [ 1, 0, 2 ], [ 2, 1 , 3 ] , [ 3, 0 , 2 ] , [4] ]
print( how_many( G ) )
