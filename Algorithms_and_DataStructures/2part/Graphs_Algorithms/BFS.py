from queue import Queue

def BFS ( G , s ) :
	q = Queue()
	n = len( G )
	d = [ -1 for i in range( n) ]
	visit = [ False for i in range( n ) ]
	parent = [ None for i in range( n ) ]
	d[s] = 0
	q.put(s)
	visit[s] = True
	while not q.empty() :
		v = q.get()
		for u in G[v] :
			if not visit[u] :
				visit[u] = True
				parent[u] = v
				d[u] = d[v]+1
				q.put( u )
	return d , parent , visit

G = [ [ 0 ,1 ,2 ] ,
      [ 1 , 0 ],
      [ 2 , 0 ]  ]
print( BFS( G ,2 ) )

