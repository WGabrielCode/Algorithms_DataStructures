# Gabriel Wermiński
"""
algorytm przechodzi po kazdeym elemencie tablicy, O( n )
 dla tego elementu lower_bound() - wyznacza pozycje w posortowanej liscie- Stack O( logn )
 insert  O(n)
 # co daje nam O( n * ( logn + n ) ) = O(n^2) chyba bo dziala duzo szybciej od n^2 ponizej tego rozwiania, zapewne przez optymalizacje insert

Orientacyjny łączny czas : 9.02 sek.
Status testów: A A A A A A A A A A
"""

from egz2Btesty import runtests
T = [5,4,3,2,4,3,1]

def bitgame2(T):
    def lower_bound(x):
        left, right = 0, len(Stack)
        while left < right:
            mid = (left + right) // 2
            if Stack[mid] > x:
                left = mid + 1
            else:
                right = mid
        return left

    Stack = []
    for x in T:
        pos = lower_bound(x)
        Stack = Stack[:pos]
        Stack.append(x)

    return len(Stack)



runtests( bitgame2, all_tests = False )

"""
from egz2Btesty import runtests
def bitgame( T ) :
	def lower_bound( x ) :
		left, right = 0, len( Stack )
		while left < right :
			mid = (left + right) // 2
			if Stack[ mid ] <= x :
				left = mid + 1
			else :
				right = mid
		return left

	Stack = [ ]
	for x in T :
		pos = lower_bound( x )
		Stack = Stack[ pos : ]
		if pos == 0 :
			Stack.insert( 0, x )

	return len( Stack )
runtests( bitgame, all_tests = True )

"""

"""
rozwiazanie O(n^2)
O(n^2)
algorytm iteruje po kazdym z elementow T po czym spradza czy w stack znajduje sie element mniejszy lub rowny niemu jesli tak usowa go,
 jesli nie znalazl zdnego takiego elementu dodajego aktualnie sprawdzany co daje O(n) * O(n)
zalicza 5 testow potem runtime error

def bitgame( T ) :
	n = len( T )

	stack = [ T[ 0 ] ]
	inf = float( "inf" )
	result = 1

	for i in range( 1, n ) :
		current = T[ i ]
		found_not = True
		for j in range( len( stack ) ) :
			if stack[ j ] <= current :
				found_not = False
				stack[ j ] = inf
				result -= 1
		if found_not :
			result += 1
			stack.append( current )

	return result
"""
