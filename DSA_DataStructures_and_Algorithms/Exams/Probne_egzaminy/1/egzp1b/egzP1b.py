from egzP1btesty import runtests 

#O(ElogV) 1.23sec
def turysta( G, D, L ):

    def edges_to_adj() :
        for u ,v , weight in G :
            A[u].append( (v,weight) )
            A[v].append( (u,weight) )

    def counter() :
        v_cnt = 0
        for u , v , weight in G :
            v_cnt = max( v_cnt , u , v )
        return v_cnt + 1

    n = counter()
    A = [ [ ] for i in range( n ) ]
    edges_to_adj()

    inf = float( "inf" )

    d = [ [inf for i in range( 5 ) ] for j in range( n ) ]

    d[D][0] = 0

    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put( (0 , D , 0 ) )

    while not pq.empty() :

        dist, u , time   = pq.get()
        if time <= 3 :
            for v , dist in A[u] :
                if v == D or (v == L and time != 3 ) :
                    continue
                new_time = time + 1
                if d[v][new_time] > d[u][time] + dist :
                    d[v][new_time] = d[u][time] + dist
                    pq.put( (d[v][new_time] , v , new_time ) )

    return min( d[L] )

G = [
(0, 1, 9), (0, 2, 1),
(1, 2, 2), (1, 3, 8),
(1, 4, 3), (2, 4, 7),
(2, 5, 1), (3, 4, 7),
(4, 5, 6), (3, 6, 8),
(4, 6, 1), (5, 6, 1)
]
D = 0
L = 6
print( turysta(G, D, L) )
runtests ( turysta )