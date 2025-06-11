
def f( T , gas , destination ) :
	idx = 0
	n = len( T )
	i = 0
	cnt = 0
	while idx + gas < destination :
		res_idx = -1
		while i < n and T[i] <= idx + gas :
			res_idx = T[i]
			i += 1
		if res_idx == -1 :
			return -1
		cnt += 1
		idx = res_idx
	return cnt
T = [ 0,5,7,9 ]
L = 4
D = 13

print( f( T , L , D ) )
