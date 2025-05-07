from collections import deque

def linear_dijkstra_BFS( G , s ) :
	n = len( G )
	inf = float( "inf" )
	d = [inf] * n
	d[s] = 0
	q = deque()
	q.append( ( s , 0 ) )

	while q :
		u , time = q.popleft()
		if time != 0 :
			q.append( ( u , time - 1 ) )
			continue

		for v , cost in G[u] :
			if d[v] > d[u] + cost :
				d[v] = d[u] + cost

				d[v] = d[u] + cost
				q.append( ( v , 0 ) )

	return d
G = [
    [(1, 5), (2, 2)],
    [(3, 1) , (0,5) , (2,1)],
    [(0,2) ,(1, 1), (3, 7)],
    [ (2,7) , (1,1) ]
	]

s = 2
print( linear_dijkstra_BFS(G, s) )