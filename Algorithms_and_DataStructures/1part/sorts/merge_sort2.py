def merge_sort( A ) :
	B = [ 0 for _ in range( len( A ) ) ]

	def merge( A, left, mid, right ) :
		nonlocal B
		for i in range( left, right + 1 ) :
			B[ i ] = A[ i ]

		i = left
		j = mid + 1
		k = left

		while i <= mid and j <= right :

			if B[ i ] < B[ j ] :
				A[ k ] = B[ i ]
				i += 1
			else :
				A[ k ] = B[ j ]
				j += 1
			k += 1
		# end while

		while i <= mid :
			A[ k ] = B[ i ]
			i += 1
			k += 1
		while j <= right :
			A[ k ] = B[ j ]
			j += 1
			k += 1

	# end merge

	def in_merge_sort( A, left, right ) :
		if left != right :
			mid = (left + right) // 2

			in_merge_sort( A, left, mid )
			in_merge_sort( A, mid + 1, right )
			merge( A, left, mid, right )

	# end in_merge_sort

	in_merge_sort( A, 0, len( A ) - 1 )


# end merge_sort

T = [ 8, 3, 1, 5, 8, 4, 2, 1, 5, 83, -123, 46, 3, 1, 64, 45, 45, 45, 45, 45, 1, 0, -2 ]
print( T )
merge_sort( T )
print( T )
