from queue import PriorityQueue

def dijkstra( G , s )  :
	n = len( G )
	d = [ 1e7 for i in range( n ) ]
	d[s] = 0
	visited = [ False for i in range(n ) ]

	for _ in range( n ) :
		min_d = 1e7
		k =- 1
		for v in range( n ) :
			if visited[v] and min_d > d[v] :
				min_d = d[v]
				k=v
		visited[u] = True
		for u in range( n ) :
			if d[u] > d[v] + G[u][v] :
				d[u] = d[v] + G[u][v]
