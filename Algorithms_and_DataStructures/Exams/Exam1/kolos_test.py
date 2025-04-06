#Gabriel Werminski
"""
sortujemy Tablice T przez bucket sort z maksymalna wartoscia D dzieki czemu mozemy skutecznie normalizowac wartosci do zakresu od 0 do 1
kombajn nie moze przejechac palika dlatego roznica sasiednich wartosci palikow jest odlegloscia miedzy nimi, jesli jest wieksza,rowna D dodajemy do res 1 co bedzie naszym wynikiem
"""

def bb_sort( T ) :
	n = len( T )
	for i in range( n-1 ) :
		for j in range( n-i-1 ) :
			if T[j] > T[j+1] :
				T[j+1] , T[j] = T[j] , T[j+1]

def bucket_sort( T , M ) :
	n = len( T )
	buckets = [ [] for _ in range( n ) ]
	for num in T :
		idx = min( n-1 , int ( num / M ) * n ) # normalizacja oraz wyznaczanie idx w buckets
		buckets[idx].append( num )
	res = []

	for bucket in buckets :
		bb_sort( bucket )
		for val in bucket :
			res.append( val )
	return res

def ogrodzenie( M , D , T ) :
	T = bucket_sort( T , M  )
	n = len( T )
	res = 0
	for i in range( n-1 ) :
		if T[i+1]-T[i] >= D :
			res += 1
	return res

T =[3.55,7.12,1.3,0.6]
print( ogrodzenie( 10 ,0.9 , T) )

print( bucket_sort( T , 10 ) )
