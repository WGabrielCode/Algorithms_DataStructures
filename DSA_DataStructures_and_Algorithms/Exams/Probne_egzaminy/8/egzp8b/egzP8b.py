from egzP8btesty import runtests

"""
Orientacyjny łączny czas : 3.33 sek.
Status testów: A A A A A A A A A A
O(nlogn)
"""
def robot_3D( G, P ):

    from queue import PriorityQueue
    pq = PriorityQueue()

    n = len( G )
    inf = float("inf")

    d = [ [ inf for i in range( n ) ] for i in range( len( P ) ) ]
    d[0][P[0]] = 0

    is_p = { p:0 for p in P }

    pq.put( (0,P[0] , 0 ) )

    while not pq.empty() :

        dist , u , p_idx = pq.get()

        if dist > d[p_idx][u] or ( u == P[-1] and p_idx == len( P ) - 1 ):
            continue

        for v , weight in G[u] :

            new_dist = d[ p_idx][ u ] + weight

            if v in is_p and p_idx+1 < len( P ) and v == P[p_idx+1] :
                    if d[p_idx+1 ][ v ] > new_dist :
                        d[  p_idx+1  ][ v ] = new_dist
                        pq.put( ( new_dist , v , p_idx+1 ) )

            elif d[ p_idx ][v] > new_dist :
                d[ p_idx ][v] = new_dist
                pq.put( ( new_dist, v , p_idx ) )

    return d[-1][ P[-1] ]

"""
Orientacyjny łączny czas : 1.96 sek.
Status testów: A A A A A A A A A A
O( n^3logn ) 
"""
def robot( G , P ) :

    from queue import PriorityQueue

    def dijkstra( start , finish ) :


        inf = float( "inf" )

        d = [inf for i in range( len( G ) ) ]
        d[start] = 0

        pq = PriorityQueue()
        pq.put( (0 , start ) )

        while not pq.empty() :
            dist , u = pq.get()

            if dist > d[u] or u == finish :
                continue

            for v , weight in G[u] :
                #if v in is_p and v != finish :
                #    continue
                new_dist = d[u] + weight
                if d[v] > new_dist :
                    d[v] = new_dist
                    pq.put( (new_dist , v ) )
        #print( start , finish , d )
        return d[finish]

    is_p = { p : 0 for p in P }

    result = 0

    for i in range( 1, len( P ) ) :
        result += dijkstra( P[i-1] , P[i] )
        # print( result )
    return result

G = [
[(1, 3), (2, 3)],
[(0, 3), (4, 4)],
[(0, 3), (3, 1), (4, 4)],
[(2, 1), (4, 2)],
[(1, 4), (2, 4), (3, 2)]
]
P = [0, 3, 4]

#print( robot(G, P) )

runtests(robot_3D ,  all_tests = True  )
