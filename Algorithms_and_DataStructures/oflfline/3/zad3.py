from zad3testy import runtests


def longer( G, s, t ) :
	from collections import deque

	def bfs( G, s, t ) :
		q = deque()
		n = len( G )
		parent = [ None ] * n
		distance = [ None ] * n
		distance[ s ] = 0
		visited = [ False ] * n
		q.append( s )
		while q :
			v = q.popleft()
			for u in G[ v ] :
				if not visited[ u ] :
					visited[ u ] = True
					q.append( u )
					parent[ u ] = v
					distance[ u ] = distance[ v ] + 1
				if u == t :
					return parent, distance[ t ]
		return parent, float( "inf" )

	def length( G, s, t ) :
		moves, distance = bfs( G, s, t )
		# print(moves,distance)
		cur = t
		while cur :
			removed = cur, moves[ cur ]
			G[ removed[ 1 ] ].remove( removed[ 0 ] )
			G[ removed[ 0 ] ].remove( removed[ 1 ] )
			newD = bfs( G, s, t )[ 1 ]
			if newD > distance :
				return removed
			G[ removed[ 1 ] ].append( removed[ 0 ] )
			G[ removed[ 0 ] ].append( removed[ 1 ] )
			cur = moves[ cur ]
		return None

	# length(G,s,t)
	return length( G, s, t )


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
