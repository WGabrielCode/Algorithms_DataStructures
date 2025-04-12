
def find_components( G ) :

	def reverse_e() :
		n = len( G )
		rev = [ [] for _ in range( n ) ]
		for v in range( n ):
			for u in G[v] :
				rev[u].append( v )
		return rev

	def dfs_time( v ) :
		visited[v] = True
		for u in G[v] :
			if not visited[u] :
				dfs_time( u )
		nonlocal time
		time_arr[v] = time , v
		time += 1

	def dfs_rev( v ) :
		visited[v] = True
		res.append( v )
		for u in G[v] :
			if not visited[u] :
				dfs_rev( u )

	n = len( G )
	time = 0
	time_arr = [ ( -1 , -1) ] * n
	visited = [False] * n

	for u in range( n ) :
		if not visited[u] :
			dfs_time( u )
	G = reverse_e()
	res_all = []
	visited = [False] * n
	for time , v in sorted( time_arr , key =lambda x: x[0] , reverse = True ) :
		if not visited[v] :
			res = []
			dfs_rev( v )
			res_all.append( res )
			
	return res_all

G = [ [ 1,2],
      [2,3],
      [3],
      [0]
	]
G2 = [
    [1],
    [2],
    [0],
    [4],
    [5],
    [3],
    [6]
]
print( find_components( G2 ) )