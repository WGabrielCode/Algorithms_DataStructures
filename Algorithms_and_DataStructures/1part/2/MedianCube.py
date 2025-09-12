def print_cube( T ) :
	for line in T :
		print( *line , end = " ")
		print( )

def flatten( T ) :
	res =[]
	for line in T :
		res += line
	return res

def to_cube( T , n) :
	new_T = [ [ 0 for i in range( n ) ] for j in range( n) ]
	idx = 0
	for i in range( n-1 ) :
		for j in range( 1 + i , n) :
			new_T[j][i] = T[ idx ]
			idx += 1

	for i in range( n ) :
		new_T[i][i] = T[idx]
		idx += 1

	for i in range( 1 , n ) :
		for j in range( i ) :
			new_T[j][i] = T[ idx ]
			idx += 1
	return new_T

def quick_sort( T ) :
	def median_of_three( T , ia , ib , ic ) :
		a = T[ia]
		b = T[ib]
		c = T[ic]

		if a <= b <= c or c <= b <= a :
			return ib
		elif b <= a <= c or c <= a <= b :
			return ia
		else :
			return ic
		print(" ???? ")

	def partition( T , left , right ) :
		pivot = median_of_three( T , left , (left+right)//2 , right )
		#pivot = (left +right) // 2
		p_val = T[pivot]
		i = left
		j = right
		while True :
			while T[i] < p_val :
				i += 1
			while T[j] > p_val :
				j -= 1
			if i >= j :
				return j
			T[i] , T[j] = T[j] , T[i]
			i += 1
			j -= 1

	def in_quick( T , left , right ) :
		if left < right :
			q = partition( T, left , right )
			in_quick( T , left , q )
			in_quick( T , q+1 , right )

	in_quick( T , 0 , len( T ) -1 )


def partition( T , k , left , right ) :
	p_val = T[k]
	i = left
	j = right
	while True :
		while T[i] < p_val :
			i += 1
		while T[j] > p_val :
			j -= 1
		if i >= j :
			return j
		T[i] , T[j] = T[j] ,T[i]
		i += 1
		j -= 1

def partition_l( T , left , right ) :
	i = left -1
	k = (left + right ) // 2
	T[k] , T[right] = T[right] , T[k]
	p_val = T[right]
	for j in range( left, right ) :
		if T[j] <= p_val :
			i += 1
			T[i] , T[j] = T[j] , T[i]
	T[right] , T[i+1] = T[i+1] , T[right]
	return i+1

def quick_select( T , k , left , right ) :
	if left == right :
		return T[left]
	if left < right :
		q = partition_l( T , left ,right )
		if q == k :
			return T[k]
		elif q < k :
			return quick_select( T , k , q+1 , right )
		else :
			return quick_select( T , k , left , q-1 )

def mediana( T ) :
	n = len( T )
	T = flatten( T )
	maxi = (n*n - n) // 2
	mini = maxi + n - 1
	n = len( T )
	print( mini , maxi )
	minv = quick_select( T ,mini, 0 , n -1)
	maxv = quick_select( T, maxi , 0, n-1 )

	partition_l( T , 0 , n-1 )

def median( T ) :
	return to_cube( flatten( T ) , len( T ) )

T1 = [ [ 2,3,5],
      [7,11,13],
      [17,19,23] ]

T2 = [ [13,19,23],
	  [3,7,17],
      [5,2,11] ]

#print_cube( median( T) )

T = [1,6,3,2,7,4,7,21,122]
#print( quick_select( T , 7 , 0 ,len( T )-1 ) )
mediana( T1 )
T1_flat = flatten( T1 )
quick_sort( T1_flat )
print( T1_flat )













"""

def to_cube( Arr , n ) :
	z = 1
	flag = True
 	x , y = 0 , n -1
	T = [ [ [0 for i in range( n )] for j in range( n ) ]
	T[y][x] = 0
	while z != n :
		if True :
			if x == n-1 :
				y -= 1
			else :
				x += 1
			while x > 0 and y > 0 :
				T[y][x] = z
				z +=1
				x -= 1
				y -= 1
		if y == 0 :
			x += 1
		else :
			y -= 1
		while x < n and y < n :
			T[y][z] = z
			z += 1
			x += 1
			y += 1
	print



def print_matrix( matrix ) :
	if not matrix :
		return

	# Determine the maximum width needed for each column
	num_columns = max( len( row ) for row in matrix )
	col_widths = [ 0 ] * num_columns

	for row in matrix :
		for i, item in enumerate( row ) :
			col_widths[ i ] = max( col_widths[ i ], len( str( item ) ) )

	# Print each row with proper spacing
	for row in matrix :
		formatted_row = [ ]
		for i, item in enumerate( row ) :
			formatted_row.append( f"{str( item ):>{col_widths[ i ]}}" )
		print( " ".join( formatted_row ) )
"""