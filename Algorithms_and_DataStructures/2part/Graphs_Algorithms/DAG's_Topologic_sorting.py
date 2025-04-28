def dfs( G ) :

	def dfsVisit( G , v ) :
		visited[v] = True
		for u in G[v] :
			if not visited[u] :
				dfsVisit( G , u )
		res.append( v )
	n = len( G )
	res = []
	visited = [ False for _ in range( n ) ]
	for v in range( n ) :
		for u in G[v] :
			if not visited[u] :
				dfsVisit( G , u )

	return res[::-1]

G = [ [ 0 ,1 ,2 ] ,
      [ 1  ],
      [ 2 ,3 ,4  ] ,
      [3,4] ,
      [4]
      ]

print( dfs( G ) )