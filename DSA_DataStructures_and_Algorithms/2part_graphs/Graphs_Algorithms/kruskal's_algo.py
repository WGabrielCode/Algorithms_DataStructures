"""
class UnionFind() :
	def __init__(self , value):
		self.parent = self
		self.val = value
		self.rank = 0
def find( x ) :
	if x.parent != x :
		x.parent = find( x.parent )
	return x.parent

def union( x , y ) :
	x = find( x )
	y = find( y )
	if x.rank < y.rank :
		x.parent = y
	else :
		y.parent = x
		if x.rank == y.rank :
			x.rank += 1

def kruskal_algo( E ) :
	E.sort( key=lambda x: x[2] )
	res = []
	for x , y , cost in E :
		if find( x ) != find( y ) :
			union( x , y )
			res.append( (x.val , y.val) )
	return res

def AdjList_To_Edges( G ) :
	edges = []
	nodes = [ UnionFind( i ) for i in range( len( G ) ) ]

	for u in range( len( G ) ) :
		for v , cost in G[u] :
			if u < v  :
				edges.append( (nodes[u] ,nodes[v],cost))
	return edges
"""

def AdjList_To_Edges( G ) :
	E = []

	for u in range( len( G ) ) :
		for v , weight in G[u] :
			if u < v :
				E.append( ( weight , u , v ) )

	return E
class UnionFind() :
	def __init__( self ) :
		self.rank = 0
		self.parent = self

def kruskal_algo( E ) :


	def find( x ) :
		if x.parent != x :
			x.parent = find( x.parent )
		return x.parent

	def union( x , y ) :
		if x.rank < y.rank :
			x.parent = y
		else :
			if x.rank == y.rank  :
				x.rank += 1
			y.parent = x

	v_cnt = len( G )
	s = [ UnionFind() for i in range( v_cnt ) ]
	E.sort()
	res = []

	for weight , u , v in E :
		x = find( s[u] )
		y = find( s[v] )

		if x != y :
			union( x , y )
			res.append( (u,v) )

	return res

G = [
    [(1, 2), (2, 4)],
    [(0, 2), (2, 1), (3, 7)],
    [(0, 4), (1, 1), (3, 5)],
    [(1, 7), (2, 5)]
]
#print( AdjList_To_Edges( G ) )

print( kruskal_algo( AdjList_To_Edges( G ) ) )

