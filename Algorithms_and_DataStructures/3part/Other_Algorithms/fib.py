
def Fibb_List( n ) :
	F = [0] * n
	F[0] = F[1] = 1
	for i in range( 2 , n ) :
		F[i] = F[i-1] + F[i-2]
	return F[n-1]

def FibbVar( n ) :
	if n <= 1 : return 1
	a = b = 1
	for i in range( 2 , n ) :
		a , b = b , a + b
	return b

def fib_mem( n ) :

	memo = {}

	def in_fib( n ) :
		if n <= 1 :
			memo[n] = 1
			return 1
		if n in memo :
			return memo[n]

		memo[n] = in_fib( n-1) + in_fib( n-2 )
		return memo[n]

	return in_fib( n-1 )

n = 7
print( fib_mem( n) )
print( FibbVar( n ) )
print( Fibb_List( n ) )