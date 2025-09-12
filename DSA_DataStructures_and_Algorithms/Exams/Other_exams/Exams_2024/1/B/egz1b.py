from egz1btesty import runtests

import math

import heapq


def kstrong( T, k ) :
	n = len( T )
	if n == 0 :
		return 0

	# dp[j] przechowuje maksymalną sumę k-silnego podciągu z j usunięciami
	# Jest to zoptymalizowana wersja z wykorzystaniem tylko jednego wiersza
	# tablicy DP, aby zmniejszyć złożoność pamięciową do O(k).
	inf  = float("inf")
	dp = [ -inf ] * (k + 1)

	# Wzorce dla zerowego elementu (bez usunięć)
	dp[ 0 ] = max( 0, T[ 0 ] )  # Startujemy z T[0] lub 0, jeśli jest ujemne

	max_sum = max( 0, dp[ 0 ] )

	for i in range( 1, n ) :
		# Nowe wartości dp dla bieżącego elementu T[i]
		new_dp = [ -inf  ] * (k + 1)

		# Przypadek 0 usunięć: dołączamy T[i] do podciągu
		new_dp[ 0 ] = max( dp[ 0 ] + T[ i ], T[ i ] )

		# Rozważamy od 1 do k usunięć
		for j in range( 1, k + 1 ) :

			# Opcja 1: Dołączamy T[i]
			option1 = dp[ j ] + T[ i ] if dp[ j ] != -float( 'inf' ) else -float( 'inf' )

			# Opcja 2: Pomiń T[i] (usuwamy)
			option2 = dp[ j - 1 ] if dp[ j - 1 ] != -float( 'inf' ) else -float( 'inf' )

			# Wybieramy lepszą opcję i upewniamy się, że podciąg nie jest pusty
			new_dp[ j ] = max( option1, option2 )

		dp = new_dp

		# Zawsze aktualizujemy globalną maksymalną sumę,
		# ponieważ rozwiązanie może kończyć się na dowolnym indeksie.
		max_sum = max( max_sum, max( dp ) )

	return max_sum

runtests( kstrong, all_tests = True )
