
def cnt_sort( A, k ) :
	n = len( A )
	B = [None] * n
	C = [0] * (k+1)
	for x in A :
		C[x] += 1
	for i in range( 1, k+1 ) :
		C[i] += C[i-1]

	for i in range( n-1 , -1 , -1 ) :
		B[ C[ A[i] ] -1 ] = A[i]
		C[ A[i] ] -= 1

	return B

T = [ 3, 7, 8, 4 , 5, 7, 5 ,5 , 5, 3, 9, 10  ]
k = 10

print( cnt_sort( T, k ) )
