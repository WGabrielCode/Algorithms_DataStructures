# minimalna liczba ladunkow zeby znalezc najwiessza wage zbiegajaca do k

def loading( A,  k ) :
	A = sorted( A , reverse = True )
	i = 0
	n = len( A )
	cnt = 0
	while k > 0 and i < n :
		print( A[i] , k)
		if k >= A[i] :
			k -= A[i]
			cnt += 1
		i += 1

	return cnt

A = [ 2, 2, 4, 8, 8, 16 ]
k = 27
print( loading( A , k ) )