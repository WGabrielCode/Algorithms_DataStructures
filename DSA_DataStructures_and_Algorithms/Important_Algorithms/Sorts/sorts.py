
def bb_sort( T ) :
	A = T.copy()

	n = len( A )
	for i in range( n ) :
		for j in range( 1 , n-i ) :
			if A[j] < A[j-1] :
				A[j-1] , A[j] = A[j] , A[j-1]

	return A


def select_sort( T ) :
	A = T.copy()

	return A


def insertion_sort( T ) :
	A = T.copy()
	n = len( A )
	for i in range( n ) :
		for j in range( i , 0 , -1 ) :
			if A[j] < A[j-1] :
				A[j] , A[j-1] = A[j-1] , A[j]
			else :
				break

	return A


def merge_sort( T ) :
	A = T.copy()

	R = [0] * len( A )
	def merge( left , mid , right ) :
		i = left
		j = mid + 1
		k = left
		R[left:right+1] = A[left:right+1]

		while i <= mid and j <= right :
			if R[i] < R[j] :
				A[k] = R[i]
				i += 1
			else :
				A[k] = R[j]
				j += 1
			k += 1

		while i <= mid :
			A[k] = R[i]
			i += 1
			k += 1

		while j <= right :
			A[k] = R[j]
			j += 1
			k += 1

	def in_merge_sort( left , right ) :
		if left < right :
			mid = ( left + right ) // 2

			in_merge_sort( left , mid )
			in_merge_sort( mid+1 , right )
			merge( left , mid , right )

	in_merge_sort( 0 , len( A ) - 1 )
	return A


def quick_sort( T ) :
	A = T.copy()
	n = len( A )

	def hoars( left , right ) :
		q = ( left +  right) // 2
		pivot = A[q]
		i = left
		j = right
		while True :
			while A[i] < pivot :
				i += 1
			while A[j] > pivot :
				j -= 1
			if i >= j :
				return j
			A[i] , A[j] = A[j] , A[i]
			i += 1
			j -= 1
	def lomuto( left , right ) :
		mid = ( left + right ) // 2
		A[mid] , A[right] = A[right] , A[mid]
		pivot = A[right]

		i = left
		for j in range( left , right ) :
			if pivot >= A[j] :
				A[i] , A[j] = A[j] , A[i]
				i += 1

		A[i] , A[right] = A[right] , A[i]
		return i

	def in_quick_sort( left , right ) :
		if left < right :
			#pivot_idx = hoars( left , right )
			pivot_idx = lomuto( left , right )
			in_quick_sort( left , pivot_idx -1 )
			in_quick_sort( pivot_idx +1 , right )
	in_quick_sort( 0 , n - 1 )
	return A


def count_sort( T ) :
	A = T.copy()

	return A


T = [ 17, -3, 0, 42, 8, 8, -3, 100, -999, 12, 0, 0, 1, 1, 1, 2, 3, 5, 8, 13 ]

T1 = [110, 100, 0]
print( bb_sort( T ) )
#"""
#print( select_sort( T ) )
print( insertion_sort( T ) )
print( merge_sort( T ) )
print( quick_sort( T ) )
#print( count_sort( T ) )
#"""