from queue import Queue

def DFS( G ) :

	def visit( G , v ) :
		nonlocal time
		time += 1
		visited[v] = True
		for u in G[v] :
			if not visited[u] :
				visit( G , u )

	n = len( G )
	visited = [False] * n
	time = 0

	for i in range( n ) :
		v = G[i][0]
		for u in G[v] :
			if not visited[u] :
				visit( G , u )
	return time , visited


G = [ [ 0 ,1 ,2 ] ,
      [ 1 , 0 ],
      [ 2 , 0 ]  ]
print( DFS( G ) )