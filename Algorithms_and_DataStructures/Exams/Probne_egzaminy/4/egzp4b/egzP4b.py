from egzP4btesty import runtests
"""
Orientacyjny łączny czas : 0.34 sek.
Status testów: A A A A A A A T T T
O( n+q )  
"""

class Node :
	def __init__( self, key, parent ) :
		self.left = None
		self.right = None
		self.parent = parent
		self.key = key
		self.x = None

def sol( root, T ) :

	head = root
	arr = []
	def emp( head ) :

		if head.left :
			emp( head.left )
		arr.append( head.key )
		if head.right :
			emp( head.right )

	emp( head )
	memo = {}
	for w in T :
		memo[w.key] = 0

	result = 0
	for i in range( 1 , len( arr)-1 ) :
		if arr[i] in memo and (arr[i-1]+arr[i+1])/2 == arr[i] :
			result += arr[i]

	return result

"""
w11 = Node( 11, None )
w5 = Node( 5, w11 )
w11.left = w5
w15 = Node( 15, w11 )
w11.right = w15
w3 = Node( 3, w5 )
w5.left = w3
w8 = Node( 8, w5 )
w5.right = w8
w12 = Node( 12, w15 )
w15.left = w12
w7 = Node( 7, w8 )
w8.left = w7
w10 = Node( 10, w8 )
w8.right = w10
T = [ w5, w7, w8, w11, w12 ]

print( sol( w11, T ) )
"""

runtests(sol, all_tests = True)
