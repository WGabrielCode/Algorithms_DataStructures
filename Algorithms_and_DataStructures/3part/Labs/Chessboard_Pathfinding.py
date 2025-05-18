def cp( A ):
	n = len( A )
	for i in range( n ) :
		for j in range( n ) :
			if i == 0 :
				if j != 0 :
					A[i][j] += A[i][j-1]
			elif j == 0 :
				A[i][j] += A[i-1][j]
			else :
				A[i][j] += min( A[i-1][j] , A[i][j-1] )
	print( A )
	n-=1
	return A[n][n]

A = [
	  [1,2,3,4],
      [7,5,2,1],
      [0,3,6,2],
	  [9,9,9,9]
    ]

print( cp( A ) )