from queue import PriorityQueue


def dijkstra_adj_list( adj_list, start ) :
	n = len( adj_list )
	dist = [ float( 'inf' ) ] * n
	dist[ start ] = 0
	pq = PriorityQueue()
	pq.put( (0, start) )
	vis = [ False ] * n

	while not pq.empty() :
		cur_dist, cur = pq.get()

		if vis[ cur ] :
			continue

		vis[ cur ] = True

		for neighbor, weight in adj_list[ cur ] :
			if not vis[ neighbor ] :
				new_dist = cur_dist + weight

				if new_dist < dist[ neighbor ] :
					dist[ neighbor ] = new_dist
					pq.put( (new_dist, neighbor) )

	return dist


adj_list = [
			 [ (1, 4), (7, 8) ],
             [ (0, 4), (2, 8), (7, 11) ],
             [ (1, 8), (3, 7), (5, 4), (8, 2) ],
             [ (2, 7), (4, 9), (5, 14) ],
             [ (3, 9), (5, 10) ],
             [ (2, 4), (3, 14), (4, 10), (6, 2) ],
             [ (5, 2), (7, 1), (8, 6) ],
             [ (0, 8), (1, 11), (6, 1), (8, 7) ],
             [ (2, 2), (6, 6), (7, 7) ]
             ]

result = dijkstra_adj_list( adj_list, 0 )
print( result )
