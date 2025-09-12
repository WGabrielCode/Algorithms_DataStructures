from egzP3btesty import runtests 
from queue import PriorityQueue

# O(nlogm) , O( ElogV ) 0.34sec
# m - cnt of Vertices , n - cnt of Edges

def lufthansa ( G ):

    class UnionFind :
        def __init__(self):
            self.rank = 0
            self.parent = self

    def find( x ) :
        if x.parent != x :
            x.parent = find( x.parent )
        return x.parent

    def union( x , y ) :
        if x.rank < y.rank :
            x.parent = y
        else :
            if x.rank == y.rank :
                x.rank += 1
            y.parent = x

    def adj_to_edges() :
        for u in range( len( G ) ) :
            for v , flow  in G[u] :
                if u < v :
                    E.append( (flow,u,v) )

    E = []
    adj_to_edges()
    E.sort( reverse = True )
    S = [ UnionFind() for _ in range( len( G ) ) ]

    result = 0
    redundant_not_used = True

    for flow , u , v in E  :
        x = find( S[u] )
        y = find( S[v] )

        if x != y :
            union( x , y )
        else :
            if redundant_not_used :
                result -= flow
                redundant_not_used = False
            result += flow
    return result
"""
G = [
[(1, 15), (2, 5), (3, 10) ],
[(0, 15), (2, 8), (4, 5), (5, 12)],
[(0, 5), (1, 8), (3, 5), (4, 6) ],
[(0, 10), (2, 5), (4, 2), (5, 11)],
[(1, 5), (2, 6), (3, 2), (5, 2) ],
[(1, 12), (4, 2), (3, 11) ]
]
print( lufthansa( G ) )
"""
runtests ( lufthansa, all_tests=True  )