class UnionFind :
	def __init__(self , value):
		self.parent = self
		self.val = value
		self.rank = 0

def find( x ):
	if x.parent != self :
		x.parent = find( x.parent)
	return x

def union( x , y ) :
	x = find( x )
	y = find( y )
	if x.rank > y.rank  :
		y.parent = x
	else :
		x.parent = y
		if x.rank == y.rank :
			y.rank += 1