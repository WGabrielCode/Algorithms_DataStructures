
def lis( A ) :

	def bin_search( x ) :
		i = 0
		j = len( res )-1
		while i <= j :
			mid = (i+j) // 2
			if res[mid] < x :
				i = mid+1
			else :
				j = mid-1
		return i

	n = len( A )
	res =  [ A[0] ]
	res_max_i = 0
	for i in range( 1 , n ) :
		print( res , res_max_i , "|", i )
		numb = A[i]
		if res[res_max_i] < numb :
			res.append( numb )
			res_max_i += 1
		else :
			res[ bin_search( numb ) ] = numb
	print( res )
	return len( res )

A = [1,7,8,4,5,6,-1,9]
B = [ 2,7,6,4,2,24,-10]
print( lis( A ) )
print( lis( B ) )