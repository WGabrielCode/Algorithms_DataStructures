def bin_search( t, x ) :
	left = 0
	right = len( t ) - 1
	while left <= right :
		mid = (left + right) // 2
		if t[ mid ] == x :
			return mid
		elif x > t[ mid ] :
			left = mid + 1
		else :
			right = mid - 1
	return None


# end


T = [ 64, 1, 2, 3, 4, 5, -123, 0, 8, 45, 46, 83, -2 ]

print( T, " | ", bin_search( T, 1 ) )
