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


def koleje( B ) :
    def E_to_adj() :
        n = 0
        for u , v in B :
            n = max( n , u , v )
        n += 1

        A = [ [] for i in range( n ) ]
        memo = {}
        for u , v in B :
            u , v = min( u,v ) , max( u,v )

            if not (u,v) in memo  :
                A[u].append( v )
                A[v].append( u )
                memo[ (u,v) ] = 0
        return A , n
    B , n  = E_to_adj()

    def dfs( u , parent ) :





B = [
(3, 1), (0, 1), (4, 2),
(1, 2), (0, 1), (2, 4),
(2, 4), (0, 3), (2, 4),
(1, 0), (2, 1)
]
print( koleje( B ) )

runtests ( koleje, all_tests=True  )