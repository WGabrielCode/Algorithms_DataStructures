
def LIS( A ) :
	def F_to_x( x ) :
		for i in range( x-1 , -1 , -1 ) :
			if A[i] < A[x] :
				F[x] = max( F[i]+1 , F[x] )
	n = len( A )
	F = [1] * n
	for i in range( 1 , n ) :
		F_to_x( i )
	return max( F )

A = [2,1,4,3,4,8,5,7]
print( LIS( A ) )