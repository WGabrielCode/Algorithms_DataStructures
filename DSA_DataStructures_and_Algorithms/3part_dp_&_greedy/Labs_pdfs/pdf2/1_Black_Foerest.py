# O(n)
def BF( A ) :
	n = len( A )
	if n > 1 and A[0] > A[1] :
		A[1] = A[0]

	for i in range( 2 , n ) :
		A[i] = max( A[i-2] + A[i] , A[i-1] )

	return A[ n-1 ]
"""
def rec_BF( A ) :

	n = len( A )

	def in_bf( max_i ) :
		if max_i == 0 :
			return A[0]
		if max_i == 1 :
			return max( A[0] , A[1] )
		return max( rec_BF( i-2 ) + A[i] , rec_BF(  i-1 ) )

	return max( in_bf( n-1 ) )

A = [ 7,2,5,0,6,3 ]
print( rec_BF( A ) )
"""
A = [ 7,2,5,0,6,3 ]
print( BF( A ) )


