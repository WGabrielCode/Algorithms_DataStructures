class Node :
	def __init__( self , val ) :
		self.next = None
		self.val = val

def append_list( head , T ) :
	for i in range( len( T ) -1 , -1 , -1 ) :
		n = T[i]
		new = Node( n )
		new.next = head
		head = new
	return head

def print_list( head ) :
	while head :
		print( head.val , end =" ")
		head = head.next

def quick_list( head ) :

	def partition( head , end ) :
		pivot = head.val
		pivot_node = head
		curr = head.next

		while curr != end :
			if curr.val < pivot :
				pivot_node = pivot_node.next
				pivot_node.val , curr.val = curr.val , pivot_node.val
			curr = curr.next

		head.val , pivot_node.val = pivot_node.val , head.val
		return pivot_node

	def in_quick( head , end ) :
		if  head != end :
			q = partition( head , end )
			in_quick( head , q )
			in_quick( q.next , end )

	in_quick( head , None )


T = [1,8,9,2,6,1,7,3,-1]
head = append_list( None , T )
quick_list( head )
print_list( head )

