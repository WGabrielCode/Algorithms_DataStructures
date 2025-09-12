from egzP5btesty import runtests 

"""
Orientacyjny łączny czas : 2.71 sek.
Status testów: A A A A A A T T T T
O( n^2 ) 
"""
def koleje2 ( B ) :
    def E_to_adj() :
        n = 0
        for u , v in B :
            n = max( n , u , v )
        n += 1

        A = [ [] for i in range( n ) ]
        memo = {}
        for u , v in B :
            if not( (u,v) in memo or (v,u) in memo )  :
                A[u].append( v )
                A[v].append( u )
                memo[ (u,v) ] = 0
        return A , n

    B , n  = E_to_adj()

    from collections import deque
    q = deque()

    result = 0

    for i in range( n ) :

        cnt = 1
        visited = [False] * n
        visited[i] = True
        q.append( 0 if i != 0 else 1 )

        while q :
            u = q.popleft()

            for v in B[u] :
                if not visited[v] :
                    visited[v] = True
                    cnt += 1
                    q.append( v )
        if cnt != n :
            result += 1

    return result

"""
Orientacyjny łączny czas : 0.06 sek.
Status testów: A A A A A A A A A A
o(nlogn)
"""
def koleje( B ) :
    def E_to_adj() :
        n = 0
        for u, v in B :
            n = max( n, u, v )
        n += 1
        A = [ [ ] for i in range( n ) ]
        memo = { }
        for u, v in B :
            u, v = min( u, v ), max( u, v )
            if not (u, v) in memo :
                A[ u ].append( v )
                A[ v ].append( u )
                memo[ (u, v) ] = 0
        return A, n

    B, n = E_to_adj()

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

    return result

B = [
(3, 1), (0, 1), (4, 2),
(1, 2), (0, 1), (2, 4),
(2, 4), (0, 3), (2, 4),
(1, 0), (2, 1)
]
print( koleje( B ) )

runtests ( koleje, all_tests=True  )