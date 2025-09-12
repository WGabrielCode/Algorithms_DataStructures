# bst kolory
from queue import Queue

def czy2( G ) :
	Q = Queue()
	n = len( G )
	color = [ -1 for _ in range( n ) ]
	color[0] = 1
	Q.put( 0 )

	while not Q.empty() :
		v = Q.get()
		for u in G[v] :
			if color[u] == -1 :
				Q.put(u)
				if color[v] == 1 :
					color[u] = 0
				else :
					color[u] = 1
			elif u != v and color[u] == color[v] :
				return False
	return True

G = [ [ 0, 1, 3 ], [ 1, 0, 2 ], [ 2, 1 , 3 ] , [ 3, 0 , 2 ] ]
print( czy2( G ) )