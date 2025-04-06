# Gabriel Werminski
"""
sortujemy Tablice T przez bucket sort z maksymalna wartoscia D dzieki czemu mozemy skutecznie normalizowac wartosci do zakresu od 0 do 1
kombajn nie moze przejechac palika dlatego roznica sasiednich wartosci palikow jest odlegloscia miedzy nimi, jesli jest wieksza,rowna D dodajemy do res 1 co bedzie naszym wynikiem

zlozonsc :
bb_sort to ( n^2 ) dla malych liczb nie wplywa na zlozosc algorytmu
bucket_sort O(n)
ogrodzenia  O(n)
"""
from kol1testy import runtests

def ogrodzenie( M, D, T ) :

	def quick_select( T ) :
		x = len( T ) // 2

		def partition( T, left, right ) :
			mid = (left + right) // 2
			T[ right ], T[ mid ] = T[ mid ], T[ right ]
			i = left - 1
			pivot = T[ right ]
			for j in range( left, right ) :
				if pivot <= T[ j ] :
					i += 1
					T[ i ], T[ j ] = T[ j ], T[ i ]
			T[ right ], T[ mid ] = T[ mid ], T[ right ]

		def quick( T, left, right, x ) :
			if left == right :
				return T[ left ]

			q = partition( T, left, right )
			if q == x :
				return T[ x ]
			if q < x :
				quick( T, q + 1, right )
			else :
				quick( T, left, q - 1 )

	def partition2( T, left, right ) :
		pivot = quick_select( T )
		mid = (left + right) // 2
		T[ right ], T[ mid ] = T[ mid ], T[ right ]
		i = left - 1
		pivot = T[ right ]
		for j in range( left, right ) :
			if pivot <= T[ j ] :
				i += 1
				T[ i ], T[ j ] = T[ j ], T[ i ]
		T[ right ], T[ mid ] = T[ mid ], T[ right ]

	def insertion_sort( T ) :
		n = len( T )
		for i in range( 1, n ) :
			for j in range( i - 1, -1, -1 ) :
				if T[ j ] > T[ j + 1 ] :
					T[ j ], T[ j + 1 ] = T[ j + 1 ], T[ j ]
				else :
					break

	def bucket_sort( T, M ) :
		n = len( T )
		buckets = [ [ ] for _ in range( n ) ]
		for num in T :
			idx = min( n - 1, int( num / M ) * n )  # normalizacja oraz wyznaczanie idx w buckets
			buckets[ idx ].append( num )
		res = [ ]

		for bucket in buckets :
			insertion_sort( bucket )
			for val in bucket :
				res.append( val )
		return res

	def main( M, D, T ) :
		n = len( T )
		partition2( T , 0 , n )
		T[0:p+1] = bucket_sort( T[0:p+1], M )
		T[p+1:n] = bucket_sort( T[p+1:n] , M )
		res = 0
		for i in range( n - 1 ) :
			if T[ i + 1 ] - T[ i ] >= D :
				res += 1
		return res
	return main( M, D, T )

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ogrodzenie, all_tests = False )
