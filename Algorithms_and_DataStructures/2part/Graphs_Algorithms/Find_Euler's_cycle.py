from copy import deepcopy
def dfs( G ) :

	def dfsVisit( v ) :
		nonlocal flag
		if flag :
			while v in
		flag = False

		if not flag :
			res.append( v )

	res = []
	T = deepcopy( G )
	n = len( G )
	visited = [ False for _ in range(n) ]
	for v in range( n ) :
		for u in G[v] :
			if not visited[u] :
				flag = True
				dfsVisit( G , u , v )
	return res

G = [
    [1, 2],     # 0 → 1, 0 → 2
    [0, 2],      # 1 → 0, 1 → 2
    [0, 1, 3, 4],# 2 → 0, 2 → 1, 2 → 3, 2 → 4
    [2, 4],      # 3 → 2, 3 → 4
    [2, 3]# 4 → 2, 4 → 3
]
print( dfs( G ) )