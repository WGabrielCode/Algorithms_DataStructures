def find_components( G ) :
	def reverse_e() :
		n = len( G )
		rev = [ [ ] for _ in range( n ) ]
		for v in range( n ) :
			for u in G[ v ] :
				rev[ u ].append( v )
		return rev

	def dfs_time( v ) :
		visited[ v ] = True
		for u in G[ v ] :
			if not visited[ u ] :
				dfs_time( u )
		nonlocal time
		time_arr[ v ] = time, v
		time += 1

	def dfs_rev( v ) :
		visited[ v ] = True
		res.append( v )
		for u in G[ v ] :
			if not visited[ u ] :
				dfs_rev( u )

	n = len( G )
	time = 0
	time_arr = [ (-1, -1) ] * n
	visited = [ False ] * n

	for u in range( n ) :
		if not visited[ u ] :
			dfs_time( u )
	G = reverse_e()

	res_all = [ ]
	visited = [ False ] * n
	print( G )
	for time, v in sorted( time_arr, key = lambda x : x[ 0 ], reverse = True ) :
		#print( time, v )
		if not visited[ v ] :
			res = [ ]
			dfs_rev( v )
			res_all.append( res )

	return res_all


def SCC( G ) :
	def dfs_1() :
		def visit( u ) :
			visited[ u ] = True
			for v in G[ u ] :
				if not visited[ v ] :
					visit( v )
			nonlocal time
			d[ u ] = (time, u)
			time += 1

		time = 0
		n = len( G )
		visited = [ False ] * n
		d = [ (float( "inf" ), -1) ] * n
		for u in range( n ) :
			if not visited[ u ] :
				visit( u )
		return d
	def rev_e() :
		n = len( G )
		rev_G = [ [ ] for i in range( n ) ]

		for u in range( n ) :
			for v in G[ u ] :
				rev_G[v].append( u )
		return rev_G

	def rev_dfs() :
		n = len( G )
		visited = [False] * n
		def visito( u ) :
			res.append( u )
			visited[u] = True
			for v in G[u] :
				if not visited[v] :
					visito( v )
		res_all = []
		for time , u in sorted( time_arr , reverse = True) :
			if not visited[u] :
				res = []
				visito( u )
				res_all.append( res )
		return res_all

	time_arr = dfs_1()
	rev_G = rev_e()
	G = rev_G
	return( rev_dfs() )


G = [ [ 1, 2 ], [ 2, 3 ], [ 3 ], [ 0 ,4 ], [ 5], [4] ]
G2 = [ [ 1 ], [ 2 ], [ 0 ], [ 4 ], [ 5 ], [ 3 ], [ 6 ] ]
print( SCC( G.copy() ) )
print( find_components( G ) )
