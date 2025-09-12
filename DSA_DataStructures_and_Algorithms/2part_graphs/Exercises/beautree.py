class UnionFind :
	def __init__( self, value ) :
		self.parent = self
		self.val = value
		self.rank = 0

def find( x ) :
	if x.parent != x :
		x.parent = find( x.parent )
	return x.parent


def union( a , b  ) :
	if a.rank < b.rank :
		a.parent = b
	else :
		if a.rank == b.rank :
			a.rank += 1
		b.parent = a


def beautree( G ) :
	def adj_to_E( ) :
		E = [ ]
		for u in range( len( G ) ) :
			for v , cost in G[u] :
				if u < v :
					E.append( ( cost , u , v , ) )
		return E

	n = len( G )

	E = sorted( adj_to_E() )
	elen = len( E )

	for i in range( elen ) :
		S = [ UnionFind( i ) for i in range( n ) ]
		res = 0
		#A_res = []
		#flag = True
		ver_cnt = [0] * len( G )
		for j in range( i , elen ) :
			cost , u , v = E[j]
			x = find( S[u] )
			y = find( S[v] )
			if x == y :
				break
			union( x , y )
		#	A_res.append( ( u,v ) )
			res += cost
			ver_cnt[u] = 1
			ver_cnt[v] = 1

		#print( ver_cnt , n  , A_res )
		if sum(ver_cnt) == n :
			return res
	return None

def beautree2( G ) :
	def adj_to_E( ) :
		E = [ ]
		for u in range( len( G ) ) :
			for v , cost in G[u] :
				if u < v :
					E.append( ( cost , u , v , ) )
		return E

	n = len( G )

	E = sorted( adj_to_E() )
	elen = len( E )

	for i in range( elen ) :
		S = [ UnionFind( i ) for i in range( n ) ]
		res = 0
		#A_res = []
		#flag = True
		ver_cnt = [0] * len( G )
		for j in range( i , elen ) :
			cost , u , v = E[j]
			x = find( S[u] )
			y = find( S[v] )
			if x == y :
				break
			union( x , y )
		#	A_res.append( ( u,v ) )
			res += cost
			ver_cnt[u] = 1
			ver_cnt[v] = 1

		#print( ver_cnt , n  , A_res )
		if sum(ver_cnt) == n :
			return res
	return None
G = [ [ (1, 3), (2, 1), (4, 2) ],  # 0
      [ (0, 3), (2, 5) ],  # 1
      [ (1, 5), (0, 1), (3, 6) ],  # 2
      [ (2, 6), (4, 4) ],  # 3
      [ (3, 4), (0, 2) ] ]  # 4
print( beautree2( G ) )
