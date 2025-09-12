"""
przedzial jednostkowy - przedzial dl 1 domnkniety
idzemy po przedzialach jednostkowych po kolei i to tyle
"""

def intervals( A ) :
	cnt = 0
	n = len( A )
	i = 0
	while i < n :
		cnt += 1
		maxv = A[i] + 1
		j = i + 1
		while j < n and A[j] <= maxv :
			j += 1
		i = j

	return cnt
A = [0.25,0.5,1,6]
print( intervals( A ) )