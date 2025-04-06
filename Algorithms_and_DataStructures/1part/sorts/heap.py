def left( indx ) :
	return 2 * indx + 1


def right( indx ) :
	return 2 * indx + 2


def parent( indx ) :
	return (indx - 1) // 2


def heapify( arr, i, n ) :
	i_max = i
	i_left = left( i )
	i_right = right( i )

	if i_left < n and arr[ i_left ] > arr[ i_max ] :
		i_max = i_left
	if i_right < n and arr[ i_right ] > arr[ i_max ] :
		i_max = i_right

	if i_max != i :
		arr[ i ], arr[ i_max ] = arr[ i_max ], arr[ i ]
		heapify( arr, i_max, n )


def build_heap( arr, n ) :
	start = parent( n - 1 )
	for i in range( start, -1, -1 ) :
		heapify( arr, i, n )


def heap_sort( arr ) :
	n = len( arr )

	build_heap( arr, n )

	for i in range( n - 1, 0, -1 ) :
		arr[ 0 ], arr[ i ] = arr[ i ], arr[ 0 ]
		heapify( arr, 0, i )

	print( arr, "heap_sort" )


# Test cases
T = [ 8, 3, 1, 5, 8, 4, 2, 1, 5, 83, -123, 46, 3, 1, 64, 45, 45, 45, 45, 45, 1, 0, -2 ]
print( T )
heap_sort( T )
