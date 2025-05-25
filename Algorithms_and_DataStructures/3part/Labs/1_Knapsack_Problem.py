#classical knapsack problem 0/1

def Knapsack_Problem( w , T ) :
	T_size = len( T )
	K = [ [ 0 for _ in range(w+1)] for _ in range( T_size ) ]

	for i in range( T_size) :
		for curr_w in range( 1 , w+1 ) :
			weight , val = T[i]

			if i == 0 :
				if weight >= curr_w :
					K[i][curr_w] = val

			else :
				if weight > curr_w :
					K[i][curr_w] = K[i-1][curr_w]
				else :
					K[i][curr_w] = max( K[i-1][curr_w] , val + K[i-1][curr_w-weight] )

	return K[T_size-1][w]

bc_w = 120
T = [ (10,60), (20,100), (30,120), (40,200), (15,50) ,(25,90) ]
# w , val

print( Knapsack_Problem( bc_w , T ) )