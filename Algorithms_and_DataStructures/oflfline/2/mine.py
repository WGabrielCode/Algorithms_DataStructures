def count_invertions( T ) :
	A = [0] * ( len( T ) -1 )
	count = 0
	def merge( T , left , mid ,  right ) :
		nonlocal A
		nonlocal count
		mid = ( left + right ) // 2
		A[left : right +1 ] = T[left : right+1]
		i = left
		j = mid +1
		k = left
		while i <= mid and j <= right :
			if A[i] < A[j] :
				T[k] = A[i]
				i += 1
			else :
				count += 1
				T[k] = A[j]
				j +=1
		while i <= mid :
			T[k] = T[i]
			k += 1
			i += 1
		while j <= right :
			count += 1
			T[k] = T[j]
			k += 1
			j += 1

	def merge_count( T , left , right ) :
		if left < right :
			mid = ( left + right ) // 2
			merge_count( T , left , mid )
			merge_count( T , mid +1 , right )
			merge( T , left , mid , right )
	merge_count( T , 0 , len( T ) -1 )
	return count

T = [3,1,2]
print( count_invertions( T ) )
