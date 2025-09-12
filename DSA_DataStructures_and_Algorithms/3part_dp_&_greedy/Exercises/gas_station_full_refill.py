"""
i =  ostatnia stacje do ktorej chcemy dojechac
x = liczba litrow paliwa z jaka konczymy na tej stacji

f(i,x ) - najtanszy koszt paliwa jaki mozemy uzyskac do stacji i


if x == L - ( D[i] - d[i-1] ) :
	a = min( f( i-1 , l ) + C[i-1] * ( L-l )  | dla l in range( 0 , L )
else : inf

b = f( i-1 , x + ( D[i-1] - D[i] )
f(i,x) = min( a , b )


lub dijkstra dla grafu z

"""