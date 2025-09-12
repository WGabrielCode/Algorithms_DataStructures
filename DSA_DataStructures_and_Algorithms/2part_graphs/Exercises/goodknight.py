from queue import PriorityQueue

def goodknight( G , s , t ) :
	def M_to_adj() :
		n = len( G )
		A = [ [] for i in range( n ) ]
		for i in range( n ) :
			for j in range( n ) :
				if G[i][j] != -1 :
					A[i].append(  ( G[i][j] , j ) )
		return A

	n = len( G )
	inf = float( "inf" )
	G = M_to_adj()

	d = [inf] * n
	d[s] = 0

	no_sleep = [0] * n

	pq = PriorityQueue()
	pq.put( ( 0, s ) )

	while not pq.empty() :
		dist , u = pq.get()

		for cost , v in G[u] :
			sleep_cost = 0

			if no_sleep[u] + cost > 16 :
				sleep_cost = 8

			if d[v] > d[u] + cost + sleep_cost :
				d[v] = d[u] + cost + sleep_cost
				if sleep_cost == 8 :
					no_sleep[v] = 0
				else :
					no_sleep[v] = no_sleep[u] + cost
				pq.put( (d[v] , v ) )

	return d[t]


#       0   1   2  3   4   5
G = [ [ -1, 3, 8, -1, -1, -1 ],  # 0
	  [ 3, -1, 3, 6, -1, -1 ],  # 1
	  [ 8, 3, -1, -1, 5, -1 ],  # 2
	  [ -1, 6, -1, -1, 7, 8 ],  # 3
	  [ -1, -1, 5, 7, -1, 8 ],  # 4
	  [ -1, -1, -1, 8, 8, -1 ] ]  # 5
s = 0
t = 5
print( goodknight( G , s , t ) )