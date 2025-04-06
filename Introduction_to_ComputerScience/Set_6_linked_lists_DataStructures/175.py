class Node :
	def __init__( self, val = None ) :
		self.val = val
		self.next = None


def wypisz( p ) :
	while p != None :
		print( p.val )
		p = p.next


def isinit( p, n ) :
	while p != None :
		if p.val == n :
			return True
		p = p.next
	return False


# end def

def delete( p, x ) :
	if not isinit( p, x ) :
		return p

	if p.val == x :
		return p.next

	first = p  # Store the head to return
	while p.next != None :
		if p.next.val == x :
			p.next = p.next.next
			return first
		p = p.next
	return first


# end def

def insert( p, x ) :
	first = p
	new_p = Node( x )
	if isinit( p, x ) :
		return first
	if first == None or first.val > x :
		new_p.next = first
		first = new_p
		return first

	while p.next != None and p.next.val < x :
		p = p.next
	new_p.next = p.next
	p.next = new_p
	return first


# end def

first = None
for i in range( 4 ) :
	x = int( input() )
	first = insert( first, x )

print()
wypisz( first )
print()
first = delete( first, 6 )
wypisz( first )
