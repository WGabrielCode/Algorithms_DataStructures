class Employee :
	def __init__( self, fun ) :
		self.emp = []
		self.f = -1
		self.g = -1
		self.fun = fun

def f( v ) :
	if v.f >= 0 : return v.f
	x = g( v )
	y = v.fun
	for u in v.emp :
		y += g( u )
	v.f = max( x , y )
	return v.f

def g( v ) :
	if v.g >= 0 : return v.g
	v.g = 0
	for u in v.emp :
		 v.g += f( u )
	return v.g

v = Employee( 50 )
w = Employee( 10 )
x = Employee( 150 )
y = Employee( 100 )
v.emp.append( w )
v.emp.append( x )
x.emp.append( y )

print( f( v ) )