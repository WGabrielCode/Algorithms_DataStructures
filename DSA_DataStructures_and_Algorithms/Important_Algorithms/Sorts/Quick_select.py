def quick_select( T, x ) :
	n = len( T )

	def lomuto( left, mid, right ) :
		T[ mid ], T[ right ] = T[ right ], T[ mid ]
		pivot = T[ right ]
		i = left
		for j in range( left, right ) :
			if pivot >= T[ j ] :
				T[ i ], T[ j ] = T[ j ], T[ i ]
				i += 1
		T[ i ], T[ right ] = T[ right ], T[ i ]
		return i

	def in_quick( left, right, x ) :
		if left == right :
			return T[ left ]
		if left < right :
			q = (left + right) // 2
			p_idx = lomuto( left, q, right )
			if p_idx == x :
				return T[ p_idx ]
			elif x < p_idx :
				return in_quick( left, p_idx - 1, x )
			else :
				return in_quick( p_idx + 1, right, x )

	return in_quick( 0, n - 1, x )

def selection_sort( A ) :
	T = A.copy()
	n = len( T )
	for i in range( n ) :
		for j in range( i , 0 , -1 ) :
			if T[j] < T[j-1] :
				T[j] , T[j-1] = T[j-1] , T[j]
			else :
				break
	print( T )

T = [ 1, 9, 2, 6, 3, 10, 4, 8, 5, 7 ]
selection_sort( T )
print( T )
print( quick_select( T, 6 ) )
