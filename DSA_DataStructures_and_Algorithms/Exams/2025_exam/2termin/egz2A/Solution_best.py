from egz2Atesty import runtests

def kingnqueen( V, E, D, K, Q, B ) :
	def Edges_to_adj() :
		for u, v in E :
			A[ u ].append( v )
			A[ v ].append( u )

	A = [ [ ] for i in range( V ) ]
	Edges_to_adj()

	def dfs_tarjan( u, parent ) :
		visited[ u ] = True
		nonlocal time
		nonlocal ap
		nonlocal root_children

		d[ u ] = low[ u ] = time
		time += 1

		for v in A[ u ] :
			if v == parent :
				continue
			if not visited[ v ] :
				if parent == -1 :
					root_children += 1

				dfs_tarjan( v, u )
				low[ u ] = min( low[ u ], low[ v ] )

				if parent != -1 and low[ v ] >= d[ u ] :
					if not used[ u ] :
						used[ u ] = True
						ap[u] = {}
			else :
				low[ u ] = min( low[ u ], d[ v ] )

	d = [ -1 ] * V
	low = [ -1 ] * V
	visited = [ False ] * V
	used = [ False ] * V
	time = 0
	ap = {}

	for u in range( V ) :
		if not visited[ u ] :
			root_children = 0
			dfs_tarjan( u, -1 )
			if root_children > 1 :
				if not used[ u ] :
					used[ u ] = True
					ap[u] = {}


	def dfs( u ) :
		nonlocal id
		group_id[u] = id
		visited[ u ] = True

		for v in A[u] :
			if v in ap :
				if not id in ap[v] :
					ap[v][id] = 0

			elif not visited[v] and not (v in ap) :
				dfs( v )

	visited = [False] * V
	group_id = {}
	id = -1

	for u in range( V ) :
		if not visited[u] and not( u in ap)  :
			id += 1
			dfs( u )

	return ap
	for a_point in ap.keys() :
		for v in A[a_point] :
			if v in ap and len( ap[v] ) == 1 :
				ap[a_point].update( ap[v] )
				ap[v] = ap[a_point]

	return ap
	result = 0

	for i in range( D ) :
		k = K[i]
		q = Q[i]
		b = B[i]

		print( group_id.keys() , k , q )

		if not k in ap and not q in ap :
			if group_id[k] == group_id[q] :
				result += 1
				continue

		for a_point in ap.keys() :
			if a_point == b :
				if k in ap[a_point] and q in ap[a_point] :
					#ne da se
					break
			if k in ap[a_point] and q in ap[a_point] :
				result += 1
				break


	return result


def kingnqueen2( V, E, D, K, Q, B ) :
	# Tworzenie listy sąsiedztwa
	A = [ [ ] for _ in range( V ) ]
	for u, v in E :
		A[ u ].append( v )
		A[ v ].append( u )

	# --- Faza 1: Znajdowanie APs i BCCs (Block-Cut Components) ---
	d = [ -1 ] * V
	low = [ -1 ] * V
	is_ap = [ False ] * V
	time = 0
	edge_stack = [ ]

	blocks = [ ]

	def ap_dfs( u, parent ) :
		nonlocal time
		d[ u ] = low[ u ] = time
		time += 1
		children_count = 0

		for v in A[ u ] :
			if v == parent :
				continue
			if d[ v ] == -1 :
				children_count += 1
				edge_stack.append( (u, v) )
				ap_dfs( v, u )
				low[ u ] = min( low[ u ], low[ v ] )

				if parent != -1 and low[ v ] >= d[ u ] :
					is_ap[ u ] = True
					new_block = [ ]
					while True :
						edge = edge_stack.pop()
						new_block.append( edge )
						if edge == (u, v) or edge == (v, u) :
							break
					blocks.append( new_block )
			elif d[ v ] < d[ u ] :
				edge_stack.append( (u, v) )
				low[ u ] = min( low[ u ], d[ v ] )

		if parent == -1 and children_count > 1 :
			is_ap[ u ] = True

	for i in range( V ) :
		if d[ i ] == -1 :
			ap_dfs( i, -1 )

	if edge_stack :
		blocks.append( edge_stack )

	# --- Faza 2: Budowa Block-Cut Tree ---
	num_blocks = len( blocks )
	num_aps = sum( is_ap )

	new_V = num_blocks + num_aps
	new_A = [ [ ] for _ in range( new_V ) ]

	ap_map = { }
	ap_idx_counter = num_blocks

	for i in range( V ) :
		if is_ap[ i ] :
			ap_map[ i ] = ap_idx_counter
			ap_idx_counter += 1

	return ap_map

	node_to_block = { }
	for block_idx, block in enumerate( blocks ) :
		block_nodes = set()
		for u, v in block :
			block_nodes.add( u )
			block_nodes.add( v )

		for node in block_nodes :
			if is_ap[ node ] :
				ap_node_idx = ap_map[ node ]
				new_A[ block_idx ].append( ap_node_idx )
				new_A[ ap_node_idx ].append( block_idx )
			else :
				node_to_block[ node ] = block_idx

	# --- Faza 3: Sprawdzanie warunków ---
	result = 0
	for i in range( D ) :
		k, q, b = K[ i ], Q[ i ], B[ i ]

		if not is_ap[ b ] :
			result += 1
			continue

		if is_ap[ k ] :
			k_node = ap_map[ k ]
		else :
			k_node = node_to_block.get( k, -1 )

		if is_ap[ q ] :
			q_node = ap_map[ q ]
		else :
			q_node = node_to_block.get( q, -1 )

		b_node = ap_map[ b ]

		if k_node == q_node :
			result += 1
			continue

		# Sprawdzanie, czy Bajtoci jest na ścieżce
		# Używamy BFS do znalezienia ścieżki
		visited_bfs = { b_node }
		q_bfs = [ k_node ]

		can_reach_q = False
		while q_bfs :
			curr_node = q_bfs.pop( 0 )
			if curr_node == q_node :
				can_reach_q = True
				break

			for neighbor in new_A[ curr_node ] :
				if neighbor not in visited_bfs :
					visited_bfs.add( neighbor )
					q_bfs.append( neighbor )

		if can_reach_q :
			result += 1

	return result

V = 9
E = [ (0, 1), (0, 2), (2, 1), (2, 3), (5, 2), (4, 2), (3, 4), (4, 5), (5, 6), (8, 6), (7, 8), (6, 7) ]
D = 3
K = [ 0, 5, 7 ]
Q = [ 3, 6, 0 ]
B = [ 2, 2, 5 ]

print( kingnqueen2( V, E, D, K, Q, B) )

runtests( kingnqueen2, all_tests = True )
