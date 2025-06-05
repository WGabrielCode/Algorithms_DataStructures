# sortujemy do wartosci i probojemy wlozyz w daedline o najwiekszej dacie a jesli jest zajety to szukamy mniejszego

def job_scheduling( T ) :
	n = len( T )
	for i in range( n ) :
		T[i] = ( T[i][0], T[i][1] , i )
	print("orignal T : " ,  T )
	T = sorted( T , key = lambda x : x[0] , reverse = True)
	print( "sorted T : " , T )
	dead = [ -1 for i in range( n) ]

	for val , deadline , original_idx in T :
		idx = deadline
		while idx >= 0 and dead[idx] >= 0 :
			idx -= 1
		if idx >= 0 :
			dead[idx] = original_idx

	return  dead

T = [(100, 2), (19, 1), (27, 2), (25, 1), (15, 3)]
	# val , deadline
print("res : " , job_scheduling( T ) )