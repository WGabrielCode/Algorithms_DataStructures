def heap_sort( T ) :

    def left( i ) :
        return 2*i + 1
    def right( i ) :
        return 2*i + 2
    def parent( i ) :
        return (i -1) // 2

    def heapify( T , n , i )  :
        l = left( i )
        r = right( i )
        i_max = i

        if l <= n and T[l] > T[i_max] :
            i_max = l

        if r <= n and T[r] > T[i_max] :
            i_max = r

        if i_max != i :
            T[i_max] , T[i] = T[i] , T[i_max]
            heapify( T , n , i_max )
        #end heapify

    def build_heap( T , n ) :
        for i in range( parent( n ) , -1 , -1 ) :
            heapify( T , n , i)

    n = len( T ) -1
    build_heap( T , n )
    for l in range( n , 0 , -1 ) :
        T[0] , T[l] = T[l] , T[0]
        heapify( T , l-1 , 0 )

#end heapSort

T = [64, 1, 2, 3, 4, 5, -123, 0, 8, 45, 46, 83, -2]
heap_sort( T )
print( T )