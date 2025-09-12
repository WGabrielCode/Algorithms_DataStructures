from egzP6atesty import runtests

"""
Orientacyjny łączny czas : 0.37 sek.
Status testów: A A A A A A A T T T
O(nk + nlogn)
"""
def google( H, s ) :
	memo = {}
	for h in H :
		cnt = 0
		for char in h :
			if "0" <= char <= "9" :
				cnt += 1
		memo[ h ] = ( len(h)-cnt )

	def merge( left , mid , right ) :
		T[left:right+1] = H[left:right+1]
		i = left
		j = mid+1
		k = left
		while i <= mid and j <= right :
			if len( T[i] ) > len( T[j] ) :
				H[ k ] = T[ i ]
				k += 1
				i += 1
			elif len( T[i] ) == len( T[j] ) :
				if memo[T[i]] > memo[T[j]] :
					H[k] = T[i]
					k += 1
					i += 1
				else :
					H[k] = T[j]
					j += 1
					k += 1
			else :
				H[ k ] = T[ j ]
				j += 1
				k += 1



		while i <= mid :
			H[k] = T[i]
			i += 1
			k += 1
		while j <= right :
			H[k] = T[j]
			k += 1
			j += 1

	def merge_sort(left ,right ) :
		if left < right :
			mid = (left+right)//2
			merge_sort( left , mid )
			merge_sort( mid+1 , right )
			merge( left , mid , right )

	n = len(H)
	T = [0] * n

	merge_sort( 0 , n-1 )

	return H[s-1]

#"""
H = [ 'aba', 'abc', 'ab1', 'abab', 'a1a1', 'aa12a']
s = 3
print( google( H, s ) )
#"""

#runtests ( google, all_tests=True  )
