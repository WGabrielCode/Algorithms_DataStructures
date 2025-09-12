from collections import deque

def enlarge( G, s, t ) :
	def shortest_g( s, t ) :
		def bfs( s ) :
			inf = float( "inf" )
			n = len( G )
			visited = [ False ] * n
			d = [ inf for i in range( n ) ]
			d[ s ] = 0
			visited[ s ] = True
			q = deque()
			q.append( s )
			while q :
				u = q.popleft()
				for v in G[ u ] :
					if not visited[ v ] :
						q.append( v )
						visited[ v ] = True
						d[ v ] = d[ u ] + 1
			return d

		n = len( G )
		d_s = bfs( s )
		d_t = bfs( t )
		New_G = [ [ ] for i in range( n ) ]
		for u in range( n ) :
			for v in G[ u ] :
				if d_s[ u ] + 1 + d_t[ v ] == d_s[ t ] :
					New_G[ u ].append( v )
		return New_G

	def tarjans_bridge( A ) :
		inf = float( "inf" )
		n = len( A )
		d = [ inf ] * n
		low = [ -1 ] * n
		visited = [ False ] * n
		time = 0
		bridges = []

		def dfs( u, parent ) :
			nonlocal time
			d[ u ] = low[ u ] = time
			time += 1
			visited[ u ] = True
			for v in A[ u ] :
				if not visited[ v ] :
					dfs( v, u )

					low[ u ] = min( low[ v ], low[ u ] )
					if d[ u ] < low[ v ] :
						return (u,v)

				elif v != parent :
					low[ u ] = min( low[ v ], low[ u ] )
			return None


		for u in range( n ) :
			if not visited[ u ] :
				res = dfs( u, -1 )
			if res != None :
				return res
		return None


	return tarjans_bridge( shortest_g( s, t ) )


G = [ [ 1, 2 ], [ 0, 2 ], [ 0, 1, 3 ], [ 2, 4, 5 ], [ 3, 5 ], [ 3, 4 ] ]
s = 0
t = 5

print( enlarge( G, s, t ) )
G1 = [[1, 2],
      [0, 2],
      [0, 1]]
s1 = 0
t1 = 2
r1 = (0, 2)

G2 = [[1, 4],  # 0
      [0, 2],  # 1
      [1, 3],  # 2
      [2, 5],  # 3
      [0, 5],  # 4
      [4, 3]]  # 5
s2 = 0
t2 = 3
r2 = None

s3 = 0
t3 = 2
r3 = [(0, 1), (1, 2)]

G4 = [[1, 4, 3],  # 0
      [0, 2],  # 1
      [1, 3],  # 2
      [2, 5, 0],  # 3
      [0, 5],  # 4
      [4, 3]]  # 5
s4 = 0
t4 = 2
r4 = None

TESTS = [(G1, s1, t1, r1),
         (G2, s2, t2, r2),
         (G2, s3, t3, r3),
         (G4, s4, t4, r4)
         ]


def runtests(f):
    OK = True
    for (G, s, t, r) in TESTS:
        print("----------------------")
        print("G: ", G)
        print("s: ", s)
        print("t: ", t)
        print("oczekiwany wynik: ", r)
        sol = f(G, s, t)
        print("uzyskany wynik  : ", sol)
        if not ((sol == r) or (sol in r)):
            print("PROBLEM!!!!!!")
            OK = False

    print("----------------------")
    if not OK:
        print("PROBLEMY!")
    else:
        print("OK")

runtests( enlarge )