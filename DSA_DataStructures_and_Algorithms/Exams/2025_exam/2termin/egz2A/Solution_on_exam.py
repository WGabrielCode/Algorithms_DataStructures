#Gabriel Wermiński
"""
O(E + D(V+E)) = O(DV + E)
zamieniamy liste krawedzi na liste adjacecji O(E)
algorytym dla kadzego dnia czyli O(D) :
razy szuka przejscia od krola do krolowej gdy nie mozna przejsc przez B[i],robimy to poprzez bfs O(V+E)
co daje nam O( E + D(V+E) ) = O( DV + E )

Orientacyjny łączny czas : 57.08 sek.
Status testów: A A A A A A A A A A A
"""

from egz2Atesty import runtests
def kingnqueen( V, E, D, K, Q, B ) :
	def Edges_to_adj() :
		for u, v in E :
			A[ u ].append( v )
			A[ v ].append( u )

	from collections import deque

	def bfs( start , finish , not_available , V ) :
		visited = [False] * V
		visited[not_available] = True

		q = deque()
		q.append( start )
		visited[start] = True

		while q :
			u = q.popleft()

			for v in A[u] :
				if v == finish :
					return True

				if not visited[v] :
					visited[v] = True
					q.append( v )
		return False

	A = [ [ ] for i in range( V ) ]
	Edges_to_adj()

	result = 0
	for i in range( D ) :
		if bfs( K[i] , Q[i] , B[i] , V ) :
			result += 1

	return result

runtests( kingnqueen, all_tests = True )
