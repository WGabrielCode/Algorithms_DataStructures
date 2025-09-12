
def Bfs( G , s ) :
	from collections import deque
	q = deque()

	n = len( G )
	visited = [False] * n
	d = [-1] * n
	d[s] = 0
	visited[s] = True
	q.append( s )

	while q :
		u = q.popleft()
		for v in G[u] :
			if not visited[v] :
				q.append( v )
				d[v] = d[u] + 1
				visited[v] = True
	return visited , d

def dfs( G ) :
	n = len( G )
	visited = [False] * n
	d = [-1] * n
	time = -1

	def in_( u ) :
		nonlocal time
		time += 1
		visited[u] = True
		d[u] = time
		for v in G[u] :
			if not visited[v] :
				in_( v )
	for u in range( n ) :
		if not visited[u] :
			in_( u )
	return visited , d , time

def dijstra( G , start ) :
	from queue import PriorityQueue

	n = len( G )
	visited = [False] * n
	inf = float( "inf" )
	d = [inf] * n
	d[start] = 0
	pq = PriorityQueue()
	pq.put( ( 0,start ) )

	while not pq.empty() :
		dist , u = pq.get()

		if dist > d[u] :
			continue

		for v , cost in G[ u ] :
			if d[v] > d[u] + cost :
				d[v] = d[u] + cost
				pq.put( ( d[v],v ) )

	return visited , d

class UnionFind :
	def __init__( self , val ) :
		self.val = val
		self.rank = 0
		self.parent = self

def kruskal( G )  :
	def find( x ) :
		if x.parent != x :
			x.parent = find(x.parent)
		return x.parent
	def union( x , y ) :
		if x.rank < y.rank :
			x.parent = y
		else :
			if x.rank == y.rank :
				x.rank += 1
			y.parent = x
	def adj_to_E() :
		E = []
		for u in range( len( G) ) :
			for v , cost in G[u] :
				if u < v :
					E.append( ( cost,u,v ) )
		return E
	def cost_sorting() :
		n = len( E )
		if n < 20 or True :
			for i in range( 0 , n ) :
				for j in range( i , 0 , -1 ) :
					if E[j] < E[j-1] :
						E[j] , E[j-1] = E[j-1] , E[j]

	s = [ UnionFind(i) for i in range( len( G ) ) ]

	E = adj_to_E()
	cost_sorting()

	res = []

	for cost , u , v in E :
		x = find( s[u] )
		y = find( s[v] )
		if x != y :
			union( x , y )
			res.append( (u,v) )
	return res
G = [
	[ 1  ],
    [ 0 , 2 ] ,
    [ 0 ,  1 ]
    ]


print( Bfs( G , 0  ) )
print( dfs( G ) )

Gdij = [
    [(1, 5), (2, 2)],
    [(3, 1)],
    [(1, 1), (3, 7)],
    []
]
print( dijstra( Gdij , 0 ) )

Gkruskal = [
    [(1, 2), (2, 4)],
    [(0, 2), (2, 1), (3, 7)],
    [(0, 4), (1, 1), (3, 5)],
    [(1, 7), (2, 5)]
]
print( kruskal( Gkruskal ) )