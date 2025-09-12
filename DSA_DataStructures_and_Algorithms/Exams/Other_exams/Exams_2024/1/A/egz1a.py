from egz1atesty import runtests

def armstrong( B, G, s, t ) :
	from queue import PriorityQueue

	def V_cnt() :
		V = 0
		for u , v , w in G :
			V = max( V , u , v )
		return V+1
	def E_to_Adj() :
		for u , v , w in G :
			A[u].append( (v,w) )
			A[v].append( (u,w) )

	n = V_cnt()

	A = [ [] for i in range( n ) ]
	E_to_Adj()

	bikes = { u : p/q for u , p , q in B }
	inf = float("inf")
	d = [ [ inf for i in range( n ) ] for i in range( 2 ) ]
	pq = PriorityQueue()

	d[0][s] = 0
	pq.put( (0,s,-1 ) )

	while not pq.empty() :

		dist , u , bike = pq.get()

		is_b = ( bike in bikes )
		idx = 1 if is_b else 0


		if u == t :
			continue
		"""
		if d[ idx ][u] < dist :
			continue
		"""

		for v , weight in A[u] :


			multi = bikes[bike] if is_b else 1

			new_dist = d[idx][u] + ( weight * multi )

			if d[idx][v] > new_dist :
				d[idx][v] = new_dist
				pq.put( (new_dist , v , bike ) )

			if not is_b and v in bikes :
				d[1][v] = min( d[0][v] , d[1][v] )
				pq.put( ( d[1][v] , v , v ) )


	return int( min( d[0][t] , d[1][t] ) )

B = [ (1, 1, 2), (2, 2, 3) ]
G = [ (0, 1, 6), (1, 4, 7), (4, 3, 4), (3, 2, 4), (2, 0, 3), (0, 3, 6) ]
s = 0
t = 4

print( armstrong( B, G, s, t ) )

runtests( armstrong, all_tests = True )