
def LSS( A , B ) :

	an = len( A )
	bn = len( B )
	dp = [ [ False for i in range( an ) ] for i in range( bn ) ]

	for i in range(bn) :
		for j in range( an ) :
			if A[j] == B[i] :
				dp[i][j] = True

	i = 0
	jmin = 0
	cnt = 0
	print( dp )
	while i < bn :
		j = jmin
		while j < an :
			if dp[i][j] :
				i += 1
				jmin = i
				cnt += 1
			if i>=bn : break
			j += 1
		i += 1
	return cnt


A = [1,2,3,4]
B = [1,3,4]
print( LSS( A, B ) )