
def wm( T , M ) :
	n = T + 1
	dp = [ float("inf") for _ in range( n ) ]
	dp[0] = 0

	for i in range( n ) :
		for m in M :
			if i - m >= 0 :
				if dp[i] > dp[i-m] + 1
					dp[i] = dp[i-m] + 1
	return dp[T]
def rec_wm( T , M ) :
	memory = {}
	def lm( t ) :

		if t in memory :
			return memory[t]
		if t == 0 :
			result = 0
		elif t<0 :
			result = 1e7
		else :
			result = 1e7
			for m in M :
				x = lm( t-m ) + 1
				if result > x :
					result = x
		memory[t]  = result
		return result

T = 12
M = [ 1 , 4 ,5 ]
print( wm( T, M ) )