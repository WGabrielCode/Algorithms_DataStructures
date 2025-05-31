#lista na k przedzialow gdzie sume najiwekszego minimalizujemy

def lc( A , k ) :

	mem = {}

	def f( j,k ) :
		if (j,k) in mem :
			return mem[(j,k)]
		if k == 1 :
			return sum[ A[:j+1] ]
		if j+1<k :
			return -1
		result = -1
		for l in range( 0, j+1 ) :
			temp = min( f(l,k-1) ,A(l+1,j+1) )
			result = max( result , temp )
		mem[ (j,k) ] = result
		return result

A = [10,12,7,17,19,5,11,7]
k = 3
print( lc( A , k ) )