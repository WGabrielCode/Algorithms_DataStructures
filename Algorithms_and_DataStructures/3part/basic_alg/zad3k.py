from zad3ktesty import runtests

def ksuma( T, k ):
    n = len( T )
    for i in range( 1 , n ) :
        if i < k :
            if T[i] > T[i-1] :
                T[i] = T[i-1]
        else :
            tmp = float("inf")
            for j in range( i-k,i):
                if tmp > T[j] :
                    tmp = T[j]
            T[i] += tmp
    #print( T )
    min_sum = float("inf")
    for i in range( n-1 , n-k-1 , -1 ) :
        if min_sum > T[i] :
            min_sum = T[i]


    return min_sum

T1=[1, 1, 1, 7, 26, 3, 56, 34, 24, 92]
T = [ 1, 2, 3, 4, 6, 15, 8, 7 , 2 , 2]
k = 3

print( ksuma( T1 , k ) )
runtests ( ksuma )