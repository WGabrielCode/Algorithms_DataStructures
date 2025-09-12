
def find_bridges( G ) :

	n = len( G )
	d = [ -1 for i in range( n ) ]
	low = [-1 for i in range( n ) ]
	time = 1
	visited = [ False for i in range( n ) ]
	bridges = []

	def DfsVisit( u , parent ) :
		nonlocal time
		visited[u] = True
		d[u] = time
		low[u] = time
		time += 1

		for v in G[u] :
			if not visited[v] :
				DfsVisit( v , u )
				low[u] = min( low[v] , low[u] )

				if low[v] > d[u] :
					bridges.append( ( u ,v ) )
			elif v != parent :
				low[u] = min( low[u] , d[v] )

	for u in range( n ) :
		if not visited[u] :
			DfsVisit( u , -1)
	print( low )
	return bridges

def tarjan_bridge_2( G ) :

	n = len( G )
	inf = float( "inf" )
	visited = [ False ] *n
	d = [ inf ] *n
	bridges = []
	time =  0
	low = [-1] *n

	def dfs( u , parent ) :
		visited[u] = True
		nonlocal time
		d[u] = low[u] = time
		time += 1
		for v in G[u] :
			if not visited[v] :
				dfs( v , u)

				low[ u ] = min( low[ u ], low[ v ] )

				if d[u] < low[v] :
					bridges.append( (u,v) )

			elif v != parent :
				low[u] = min( low[u] , low[v] )

	for u in range( n ) :
		if not visited[u]  :
			dfs( u , -1 )

	return bridges

def find_bridge_test( G ) :
	def dfs( u , parent ) :
		visited[u] = True
		nonlocal time
		low[u] = d[u] = time
		time += 1
		for v in G[u] :
			if not visited[v] :
				dfs( v , u )

				low[u] = min( low[u] , low[v] )
				if low[v] > d[u] :
					bridges.append( (u,v) )
			elif v != parent :
				low[u] = min( low[u] , low[v] )

	n = len( G )
	inf = float( "inf" )
	visited = [False] * n
	low = [-1] * n
	d = [inf] * n
	bridges = []
	time = 0
	start = 0
	dfs( start , -1 )
	return bridges

def tarjan_bridges( G ) :

	def dfs( u , parent ) :
		visited[u] = True
		nonlocal time
		low[u] = d[u] = time
		time += 1

		for v in G[u] :
			if v == parent :
				continue
			if not visited[v] :

				dfs( v , u )

				low[u] = min( low[u] , low[v] )
				if low[v] > d[u] :
					bridges.append( (u,v) )

			elif v != parent :
				low[u] = min( low[u] , low[v] )
	n = len( G )
	inf = float( "inf" )
	bridges =[]
	visited = [False] * n
	low = [inf] * n
	d = [inf] * n
	time = 0

	for u in range( n ) :
		if not visited[u] :
			dfs( u , -1 )
	return bridges

G1 = [[1, 2],
      [0, 2],
      [0, 1 , 3],
      [2 ,4 ],
      [3]]

G2 = [[1, 4],  # 0
      [0, 2],  # 1
      [1, 3],  # 2
      [2, 5],  # 3
      [0, 5],  # 4
      [4, 3]]  # 5
#print( find_bridges( G1 ) )
#print( tarjan_bridge_2( G1 ) )
print( find_bridge_test( G1 ) )
print( tarjan_bridges( G1 ) )


