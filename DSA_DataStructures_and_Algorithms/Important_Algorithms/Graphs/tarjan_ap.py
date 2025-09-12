def dfs( u, parent ) :
	visited[ u ] = True
	nonlocal time
	nonlocal result
	nonlocal root_children

	d[ u ] = low[ u ] = time
	time += 1

	for v in B[ u ] :
		if v == parent :
			continue
		if not visited[ v ] :
			if parent == -1 :
				root_children += 1

			dfs( v, u )
			low[ u ] = min( low[ u ], low[ v ] )

			if parent != -1 and low[ v ] >= d[ u ] :
				if not used[ u ] :
					used[ u ] = True
					result += 1
		else :
			low[ u ] = min( low[ u ], d[ v ] )


d = [ -1 ] * n
low = [ -1 ] * n
visited = [ False ] * n
used = [ False ] * n
time = 0
result = 0

for u in range( n ) :
	if not visited[ u ] :
		root_children = 0
		dfs( u, -1 )
		if root_children > 1 :
			if not used[ u ] :
				used[ u ] = True
				result += 1
