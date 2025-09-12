from egz3Btesty import runtests

"""
Orientacyjny łączny czas : 1.86 sek.
Status testów: A A A A A A A A A A
"""

def kom( X, Z, W ) :
	memo = { }

	def rec( i, z ) :

		if i >= len( X ) :
			return 0

		if z < 0 :
			return -float("inf")

		key = (i,z)
		if key in memo :
			return memo[key]

		wp = X[i]
		health = Z[i]

		#skip
		res =  max ( 0 , rec( i+1 , z ) )

		#Bierze udzial
		if z - health >= 0 :
			res = max( res ,  wp + rec( i+1 , z-health ) )

		# Spa
		nonlocal W
		if z + health <= W :
			res = max( res , rec( i+1 , z + health ) - wp  )

		memo[key] = res
		return res

	return rec( 0 , W )

runtests( kom, all_tests = True )
