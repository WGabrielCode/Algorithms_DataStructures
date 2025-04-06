# z kazdego mozna do niego dojsc a zniego nie da sie wyjsc na macierzy

def steam( G , ) :
	n = len(  G )
	cnt_1 = 0
	for i in range( n ) :
		for j in range( n ) :
			if G[i][j] == 1 :
				cnt_1 += 1

G = [ [ 0 , 1 , 1 , 1 ] ,
	  [ 0, 0 , 0 , 0 ] ,
	  [ 1 , 1 , 0 , 0 ] ,
	  [ 1 , 1 , 0 , 0 ]  ]

G2 = [ [ 0 , 1 , 1 , 1 ] ,
	  [ 1, 0 , 0 , 0 ] ,
	  [ 0 , 1 , 0 , 0 ] ,
	  [ 1 , 1 , 0 , 0 ]  ]

