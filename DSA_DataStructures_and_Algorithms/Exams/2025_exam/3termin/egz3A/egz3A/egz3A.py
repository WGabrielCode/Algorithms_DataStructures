from egz3Atesty import runtests

"""
Orientacyjny łączny czas : 12.67 sek.
Status testów: A A A A A A A A A A A
"""

def treecut( H, k ) :

	n = len( H )
	dp = [ 0 ] * n

	for j in range( 1, n ) :
		for i in range( j - 1, -1, -1 ) :
			if H[ i ] > H[ j ] :
				dp[j] += 1
		dp[j] += dp[j-1]
		if dp[j] > k :
			return j
	return n

runtests( treecut, all_tests = True )
