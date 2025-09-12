from egzP2btesty import runtests
from math import log10

# O(nm+qm)
class Tree :
	def __init__( self ) :
		self.left = None
		self.right = None
		self.rank = 0


def kryptograf( D, Q ) :
	root = Tree( )
	for d in D :

		head = root
		for i in range( len( d ) - 1, -1, -1 ) :
			char = d[ i ]

			if char == "1" :
				if not head.left :
					head.left = Tree( )
				head = head.left
				head.rank += 1
			else :
				if not head.right :
					head.right = Tree()
				head = head.right
				head.rank += 1
	result = 1
	for q in Q :
		if q == "" :
			result *= len( D )
		else :
			head = root
			for i in range( len(q)-1 , -1 , -1 ) :
				char = q[i]
				if char == "1" :
					head = head.left
				else :
					head = head.right
			result *= head.rank
	return log10( result )


D = [ "1100", "100", "0", "1111", "1101", "1", "11", "00011", "00", "1010101001", "1001" ]
Q = [ "", "1", "11", "0", "1101" ]

D = ["1100", "100", "0", "1111", "1101"]
Q = ["", "1", "11", "0", "1101"]

# Q = ["", "1", "11", "0", "1101","1000","1111"]

print( kryptograf( D, Q ) )

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej

runtests(kryptograf, all_tests = 2 )
