from queue import PriorityQueue

def warrior( G, s, t ) :
	inf = float( 'inf' )

	def calculate_v() :
		n = 0
		for u , v , cost  in G :
			n = max( n , u , v )
		return n + 1
	def edges_to_adj( G , n  ) :
		res = [ [] for _ in range( n ) ]
		for u , v , cost in G :
			res[u].append( ( v , cost ) )
			res[v].append( ( u , cost ) )
		return res

	n = calculate_v()
	Adj_list = edges_to_adj( G , n )
	#print(Adj_list)
	d = [ inf for i in range( n ) ]
	d[s] = 0
	no_sleep = [ 0 for i in range( n ) ]

	pq = PriorityQueue()
	pq.put( ( 0 , s )  )

	while not pq.empty()  :
		dist , u = pq.get()

		if d[u] < dist  :
			continue

		for v , cost in Adj_list[u] :
			sleep_cost = 0
			if no_sleep[u] + cost > 16 :
				sleep_cost = 8

			if d[v] > d[u] + cost + sleep_cost :
				if sleep_cost == 8 :
					no_sleep[v] += no_sleep[u]
				no_sleep[v] += cost
				d[v] = d[u] + cost + sleep_cost
				pq.put( (d[v] , v ) )

	return d

G = [ (1, 5, 10), (4, 6, 12), (3, 2, 8),
      (2, 4, 4), (2, 0, 10), (1, 4, 5),
      (1, 0, 6), (5, 6, 8), (6, 3, 9)
    ]

s = 0
t = 6
print( warrior( G , s , t ) )
