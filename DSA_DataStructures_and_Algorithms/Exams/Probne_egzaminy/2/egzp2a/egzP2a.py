from egzP2atesty import runtests 

# no ja nwm jak zdrowy czlowiek moze zrobic cos takiego innemu czlowiekowi
def zdjecie(T, m, k):
    if k == 0 :
        k += 1
        m -= 1


    start = [ 0 for i in range( m ) ]
    finish = [ 0 for i in range( m ) ]
    current_top = k + m-1
    current_end = -1

    for i in range( m ) :
        start[i] = current_end + 1
        current_end += current_top
        finish[i] = current_end
        current_top -= 1

    return start , finish

    ends = [ k+i for i in range( m ) ]

    print( ends )
    return
    T.sort( key= lambda x : x[1] , reverse = True )
    res = [0] * n
    q = 0

    for row_nr in range( m ) :
        idx = row_nr
        for i in range( current_top ) :
            res[idx] = T[q]
            idx += m
            q += 1
        current_top -= 1

    T = res
    return T

m = 2 #Ilość rzędów
k = 2 #Ilość osób w najniższym rzędzie
T = [ (1001, 154),(1002, 176),(1003, 189),(1004, 165),(1005, 162) ]
print( zdjecie(T, m, k) )

#runtests ( zdjecie, all_tests=False )