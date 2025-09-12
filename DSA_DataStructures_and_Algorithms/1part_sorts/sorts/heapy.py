def heap_sort( T ) :
    def left( i ) :
        return i*2 + 1
    def right( i ) :
        return i*2 + 2
    def parent( i ) :
        return ( i - 1 ) // 2

    def swap( x , y ) :
        x , y = y , x
        return x , y

    def heapify( T , n , i ) :
        i_max = i
        l = left( i )
        r = right( i )

        if l <= n and T[l] > T[i_max] :
            T[l] , T[i_max] = swap( T[l] , T[i_max] )
        if r <= n and T[r] > T[i_max] :
            T[r] , T[i_max] = swap( T[r] , T[i_max] )
        if i != i_max :
            T[i_max] , T[i] = swap( T[i_max] , T[i] )
            heapify( T , n , i_max )

    def build_heap( T , n ) :
        for i in range( parent( n ) , -1 , -1 ) :
            heapify( T , n , i )

    n = len( T ) -1
    build_heap( T , n )
    for l in range( n , 0 , -1 ) :
        T[0] , T[l] = T[l] , T[0]
        heapify( T , l-1 , 0 )

T =[6,2,8,19]
#T = [8, 3, 1, 5, 8, 4, 2, 1, 5, 83, -123, 46, 3, 1, 64, 45, 45, 45, 45, 45, 1, 0, -2]

heap_sort(T)
print(T)

































