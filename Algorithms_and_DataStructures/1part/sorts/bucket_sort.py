def bb_sort( A ) :
	n = len( A )
	for i in range( n - 1 ) :
		for j in range( n - i - 1 ) :
			if A[ j ] > A[ j + 1 ] :
				A[ j ], A[ j + 1 ] = A[ j + 1 ], A[ j ]


def bucket_sort( T ) :
	n = len( T )
	buckets = [ [ ] for _ in range( n ) ]
	minv = min( T )
	maxv = max( T )

	for num in T :
		unified_num = (num - minv) / (maxv - minv)
		idx = min( int( n * unified_num ), n - 1 )
		buckets[ idx ].append( num )
	res = [ ]
	for bucket in buckets :
		bb_sort( bucket )
		for num in bucket :
			res.append( num )

	return res


def merge_sort( T ) :
	A = [ 0 ] * len( T )

	def merge( T, left, mid, right ) :
		A[ left : right + 1 ] = T[ left :right + 1 ]
		i = left
		j = mid + 1
		k = left
		while i <= mid and j <= right :
			if A[ i ] <= A[ j ] :
				T[ k ] = A[ i ]
				i += 1
			else :
				T[ k ] = A[ j ]
				j += 1
			k += 1
		while i <= mid :
			T[ k ] = A[ i ]
			i += 1
			k += 1
		while j <= right :
			T[ k ] = A[ j ]
			j += 1
			k += 1

	def in_merge( T, left, right ) :
		if left < right :
			mid = (left + right) // 2
			in_merge( T, left, mid )
			in_merge( T, mid + 1, right )
			merge( T, left, mid, right )

	in_merge( T, 0, len( T ) - 1 )
	return T


def quick_sort( T ) :
	def median_3( T, ia, ib, ic ) :
		a = T[ ia ]
		b = T[ ib ]
		c = T[ ic ]
		if (b <= a <= c) or (c <= a <= b) :
			return ia
		elif (a <= b <= c) or (c <= b <= a) :
			return ib
		else :
			return ic

	def partition( T, left, right ) :
		i = left - 1
		p_idx = median_3( T, left, (left + right) // 2, right )
		# p_idx = (left + right)//2
		T[ right ], T[ p_idx ] = T[ p_idx ], T[ right ]
		p_val = T[ right ]
		for j in range( left, right ) :
			if p_val >= T[ j ] :
				i += 1
				T[ i ], T[ j ] = T[ j ], T[ i ]
		i += 1
		T[ right ], T[ i ] = T[ i ], T[ right ]
		return i

	def in_quick( T, left, right ) :
		if left < right :
			q = partition( T, left, right )
			in_quick( T, left, q - 1 )
			in_quick( T, q + 1, right )

	in_quick( T, 0, len( T ) - 1 )
	return T


def heap_sort( T ) :
	def left( i ) :
		return 2 * i + 1

	def right( i ) :
		return 2 * i + 2

	def parent( i ) :
		return (i - 1) // 2

	def heapify( T, n, i ) :
		l = left( i )
		r = right( i )
		i_max = i

		if l <= n and T[ l ] > T[ i_max ] :
			i_max = l

		if r <= n and T[ r ] > T[ i_max ] :
			i_max = r

		if i_max != i :
			T[ i_max ], T[ i ] = T[ i ], T[ i_max ]
			heapify( T, n, i_max )  # end heapify

	def build_heap( T, n ) :
		for i in range( parent( n ), -1, -1 ) :
			heapify( T, n, i )

	n = len( T ) - 1
	build_heap( T, n )
	for l in range( n, 0, -1 ) :
		T[ 0 ], T[ l ] = T[ l ], T[ 0 ]
		heapify( T, l - 1, 0 )


def hash( word ) :
	prime = 10 ** 7 + 7
	w = 1
	res = 0
	for char in word :
		res = (ord( char ) * w) % prime
		w = (w * 31) % prime
	return res


T = [ 0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434 ]
print( bucket_sort( T.copy() ) )
print( merge_sort( T.copy() ) )
print( quick_sort( T.copy() ) )

print( hash( "problem_solve" ) )
