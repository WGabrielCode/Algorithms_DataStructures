"""
Proszę rozwiązać dwa następujące zadania:
1. Jak wykorzystać algorytm dla problemu najdłuższego wspólnego podciągu do rozwiązania zadania
najdłuższego rosnącego podciągu?
2. Na wykładzie podaliśmy algorytm działający w czasie O(n2). Proszę podać algorytm o złożoności
O(n log n)
"""

def lis_using_Lss_1( A ) :

	n = len( A )
	dp = [ [ False for i in range( n ) ] for i in range( n ) ]
	B = sorted( A )

	for i in range(n) :
		for j in range( n ) :
			if A[j] == B[i] :
				dp[i][j] = True

	i = 0
	jmin = 0
	cnt = 0
	while i < n :
		j = jmin
		while j < n :
			if dp[i][j] :
				i += 1
				jmin = i
				cnt += 1
			if i>=n : break
			j += 1
		i += 1
	return cnt

A = [1,2,9,6,4,6,7]

print( lis_using_Lss_1( A ) )

def 