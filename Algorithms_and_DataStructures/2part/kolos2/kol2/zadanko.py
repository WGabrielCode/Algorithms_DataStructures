#Gabriel Wermninski
# znajduje lcizbe V z wiedza ze sa ponumerowane od 0 do V-1.
#zmieniam liste krawedzi na adj_list
# dzialanie algorytmu :
# 2 tryby ( in_resort_global )
# jesli False szukamy przejsc bezprosednio do resortow
# jesli True szukamy przejsc ktore nie trafiaja do resortow jesli parent jest resortem
#oparte na algorytmie dijkstry
# ElogV


def lets_roll( start_City, flights, resorts ) :
	from queue import PriorityQueue

	def v_cnt( flights ) :
		m_v = -1
		for u, v, cost in flights :
			m_v = max( m_v, u, v )
		return m_v + 1

	def e_to_adj( n ) :
		G = [ [ ] for i in range( n ) ]
		for u, v, cost in flights :

			if u in resorts :
				u_r = True
			else :
				u_r = False
			if v in resorts :
				v_r = True
			else :
				v_r = False

			G[ u ].append( (v, cost, v_r) )
			G[ v ].append( (u, cost, u_r) )
		return G

	n = v_cnt( flights )
	G = e_to_adj( n )
	inf = float( "inf" )
	d = [ inf ] * n
	parent = [ -1 ] * n
	d[ start_City ] = 0
	pq = PriorityQueue()
	pq.put( (0, start_City) )
	visited_resorts_cnt = 0
	in_resort_global = False

	while not pq.empty() :

		dist, u = pq.get()

		if visited_resorts_cnt == len( resorts ) :
			return d[u]

		for v , cost , in_r in G[u] :
			if not in_resort_global :
				if not in_r :
					continue
			else :
				if v in resorts or u in resorts :
					continue

			if d[v] > d[u] + cost + cost :
				d[v] = d[u] + cost + cost
				pq.put( (d[v] ,v ) )
				if not in_resort_global :
					in_resort_global = True
					if v in resorts :
						visited_resorts_cnt += 1
				else :
					in_resort_global = False
	return d


start_city = 0
flights = [ (0, 1, 2), (0, 2, 4), (0, 3, 8), (3, 4, 16), (1, 4, 1), (2, 4, 1) ]
resorts = [ 1, 2, 4 ]
print( lets_roll( start_city, flights, resorts ) )
