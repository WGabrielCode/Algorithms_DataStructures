# policz liczbe spojncyh skaldowych

def dfs(  G ) :

	def dfsVisit( G ,v  ) :
		nonlocal time
		nonlocal n
		time += 1
		visited[v] = True
		for u in range( n )  :
			if G[v][u]==1 and not visited[u] :
				dfsvisit( G , u )

	time = 0
	n = len( G )
	visited = [ False for _ in range( n ) ]
	v = 0

	for u
