#lista na k przedzialow gdzie sume najiwekszego minimalizujemy

def lc_2( nums, k ) :

	n = len( nums )
	pre_sum = [0] * n
	pre_sum[0] = nums[0]

	for i in range( 1 , n ) :
		pre_sum[i] = pre_sum[i-1] + nums[i]

	memo = {}
	def f( i , parts ) :
		if (i,parts) in memo :
			return memo[ (i,parts) ]

		if parts == 1 :
			memo[ (i,parts) ] = pre_sum[i]  # sum ( nums[ :i + 1 ] )
			return memo[ ( i,parts) ]

		result = float("inf")
		for j in range( parts-1 , i + 1 ) :
			tmp = max( f( j-1 , parts-1 ),  pre_sum[i] - pre_sum[j-1] ) #sum(  nums[ j :i + 1 ] ) )
			result = min( result ,  tmp)
		memo[ (i,parts) ] = result
		print( memo )
		return result
	return f( len( nums ) - 1, k )

A = [10,12,7,17,19,5,11,7]
B = [1,2,3,4,5]
k = 2
print( lc_2( B , k ) )