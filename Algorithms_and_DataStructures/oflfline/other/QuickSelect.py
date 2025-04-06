def linearselect( A , k ) :

	def partition( A , left , right ) :
		mid = ( left + right ) // 2
		p_val = A[mid]
		i = left
		j = right
		while True :
			while A[i] < p_val :
				i += 1
			while A[j] > p_val :
				j -= 1
			if i >= j :
				return j
			A[i] , A[j] = A[j] , A[i]
			i += 1
			j -= 1

	def lomuto_partition( T , left , right ) :
		mid = ( left + right ) // 2
		T[mid] , T[right] = T[right] , T[mid]
		pivot = T[right]
		i = left -1
		for j in range( left , right ) :
			if T[j] < pivot :
				i += 1
				T[i] , T[j] = T[j] , T[i]
		T[i+1] , T[right] = T[right] , T[i+1]
		return i+1

	def main( A , k , left ,right  ) :
		if left < right :
			q = lomuto_partition( A , left , right )
			if q == k :
				return A[q]
			elif q > k :
				return main( A,k, left , q -1 )
			else :
				return main( A ,k, q+ 1 , right )
		return None

	return main( T, k , 0, len( T ) - 1 )


T = [ 6, 2, 1, 8, 3, 6,6, 8, 4, 2, 3 ]
#T = [1,2]
k = 9
print( linearselect( T, k ) )

for i in range( len( T ) -1 ) :
	print( i , end=" ,")