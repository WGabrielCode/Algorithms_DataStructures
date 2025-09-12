
def Lis( A ) :

	def bin_search( x ) :
		left = 0
		right = len( result ) - 1

		while left < right :
			mid = (left+right) // 2

			if result[mid] == x :
				return mid
			if result[mid] > x :
				right = mid
			else :
				left = mid + 1
		return left

	result = []

	for x in A :
		if not result or result[-1] < x :
			result.append( x )
		else :
			idx = bin_search( x )
			result[idx] = x

	return len( result )

A = [1,9,2,123,1,8,2,12,70]
print( Lis( A ) )



