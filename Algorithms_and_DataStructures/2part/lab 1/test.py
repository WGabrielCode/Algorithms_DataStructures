from copy import deepcopy

def find_euler_cycle( G ) :
	def dfs( v ) :
		nonlocal flag
		if flag :
			print( v )
			while T[ v ] :
				if not flag : break
				u = T[ v ].pop(0)
				T[ u ].remove( v )
				dfs( u )
			else :
				flag = False
				finished[v] = True
				res.append(v)

	for line in G :
		if len( line ) % 2 != 0 :
			return None

	T = deepcopy( G )
	# T = G.copy()
	n = len( G )
	res = [ ]
	finished = [False] * n
	for v in range( n ) :
		for u in G[ v ] :
			if not finished[u] :

				flag = True
				dfs( u )
	return res


# Example graph (Eulerian)
G = [ [ 1, 2 ],  # 0 → 1, 0 → 2
	[ 0, 2, 3, 4 ],  # 1 → 0, 1 → 2
	[0,1 ],  # 2 → 0, 2 → 1, 2 → 3, 2 → 4
	[ 1, 4 ],  # 3 → 2, 3 → 4
	[ 1, 3 ]  # 4 → 2, 4 → 3]
]

G = [ [1,4],
      [0,5],
      [4,3],
      [2,5],
      [0,2,5,5],
      [1,3,4,4]]

print( find_euler_cycle( G ) )
