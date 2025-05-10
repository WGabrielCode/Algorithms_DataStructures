# Gabriel Wermninski
# znajduje lcizbe V z wiedza ze sa ponumerowane od 0 do V-1.
# zmieniam liste krawedzi na adj_list
# dzialanie algorytmu :
# 2 tryby ( in_resort_global )
# jesli False szukamy przejsc bezprosednio do resortow
# jesli True szukamy przejsc ktore nie trafiaja do resortow jesli parent jest resortem

# oparte na algorytmie dijkstry
# program nie dziala :(
# ElogV

from kol2testy import runtests

def lets_roll( start_City, flights, resorts ) :
    from queue import PriorityQueue

    def v_cnt( flights ) :
        m_v = -1
        for u, v, cost in flights :
            m_v = max( m_v, u, v )
        return m_v + 1

    def e_to_adj( n ) :
        G = [ [ ] for i in range( n ) ]
        for u, v, cost in flights :
            G[ u ].append( (v, cost) )
            G[ v ].append( (u, cost) )
        return G

    n = v_cnt( flights )
    G = e_to_adj( n )
    inf = float( "inf" )
    d = [ inf ] * n
    parent = [ -1 ] * n
    d[ start_City ] = 0
    pq = PriorityQueue()
    pq.put( (0, start_City) )
    is_resort_list = [ False ] * n
    for i in range( n ) :
        if i in resorts :
            is_resort_list[ i ] = True
    visited_resorts_cnt = 0


    while not pq.empty() :

        dist, u = pq.get()
        for v , cost in G[u] :

            if d[ v ] > d[ u ] + cost + cost :
                d[ v ] = d[ u ] + cost + cost
                if not is_resort_list[v] :
                    pq.put( (d[ v ], v) )
    res = 0
    for u in range( n ) :
        if is_resort_list[u] :
            res += d[u]
    return res
runtests(lets_roll, all_tests = True )
