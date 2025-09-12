# egz2Atest_spec.py
from testy import MY_random

import sys
sys.setrecursionlimit(1000000)

ALLOWED_TIME = 100


TEST_SPEC = [
    [3, 4, 9, 40, 60, 15, 6 ],
    [5, 20, 50, 10, 90, 100, 60 ],
    [15, 20, 50, 10, 90, 100, 81 ],
    [15, 50, 100, 50, 70, 20, 13 ],
    [15, 100, 200, 10, 90, 20, 14 ],
    [100, 100, 200, 10, 90, 50, 48 ],
    [100, 150, 300, 60, 80, 100, 87 ],
    [200, 100, 150, 60, 80, 300, 286 ],
    [300, 100, 150, 60, 80, 300, 294 ],
    [500, 90, 110, 30, 90, 1000, 976 ],
]


# wygeneruj skladowa majaca wierzcholki o numerach z tablicy V oraz ok. EDG dodatkowych krawedzi
def genCom( V, EDG ):
    n = len(V)
    C = [[False for _ in range(n)] for __ in range(n)]
    for i in range(n-1):
        C[i][i+1] = True
        C[i+1][i] = True

    for i in range(EDG):
        u = MY_random() % n
        v = MY_random() % n
        if u == v: continue
        C[u][v] = True
        C[v][u] = True
        
    E = []
    for u in range(n):
        for v in range(u+1,n):
            if C[u][v]:
                E.append((V[u],V[v]))
    return E


def howManyEdges( n, f0, f1 ):
    f = f0 + (MY_random() % (f1-f0+1))
    edg = ((n*(n-1)//2)*f)//100
    return edg

def permute( V ):
    VV = []
    while len(V) > 0:
        i = MY_random()% len(V)
        VV.append( V[i] )
        V[i] = V[-1]
        V.pop()
    return VV
    
    


# wygeneruj graf
def genInstance( c, n0, n1, f0, f1, D ):
    C = []  
    E = []  
    max_V = 0 

    A = []  

    
    for comp in range(c):
        n = n0 + (MY_random() % (n1-n0+1))
        if len(C) == 0:
            C.append( list(range(n)) )
            EDG = howManyEdges( n, f0, f1 )
            E_Comp = genCom( C[0], EDG )
            E.extend( E_Comp )
            max_V = n
        else:
            i = MY_random() % comp  
            j = MY_random() % len(C[i])
            COMP = list( range(max_V, max_V+n))
            COMP.append( C[i][j])
            A.append( C[i][j] )
            COMP = permute( COMP )
            C.append( COMP )
            EDG  = howManyEdges( n+1, f0, f1 )
            E_Comp = genCom( COMP, EDG )
            E.extend( E_Comp )
            max_V += n

    K = [ 0 for _ in range(D)]
    Q = [ 0 for _ in range(D)]
    B = [ 0 for _ in range(D)]

    for d in range(D):
        while True:
            ck = MY_random() % len(C)
            cq = MY_random() % len(C)
            b  = A[MY_random() % len(A)]
            k = C[ck][ MY_random() % len(C[ck])]
            q = C[cq][ MY_random() % len(C[cq])]
            if k != q and k != b and q != b:
                break
        K[d] = k
        Q[d] = q
        B[d] = b


    return max_V, E, K, Q, B

    

            

    
            
        


def gentest(c, n0, n1, f0, f1, D, hint):
    V, E, K, Q, B = genInstance( c, n0, n1, f0, f1, D )   
    return [V,E,D,K,Q,B], hint

