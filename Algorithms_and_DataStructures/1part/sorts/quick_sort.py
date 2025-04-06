def quick_sort( T ) :

    def get_pivot( T , left , right ) :
        mid = (left + right ) // 2
        pivot = right

        if T[left] < T[mid] :
            if T[mid] < T[right] :
                return mid
            elif T[right] > T[left] :
                return right
            else :
                return left
        else :
            if T[left] > T[right] :
                return left
            elif T[mid] < T[right] :
                return right
            else :
                return mid


    def partition( T , left , right , pivot ) :
        T[pivot] , T[right] = T[right] , T[pivot]

        i = left -1
        for j in range( left, right ) :
            if T[right] >= T[j] :
                i += 1
                T[i] , T[j] = T[j] , T[i]

        T[i+1] , T[right] = T[right] , T[i+1]
        return i+1

    def hoar_partition( T , left , right , pivot ) :
        i = left
        j = right
        pivot_val = T[pivot]
        while True :
            while T[i] < pivot_val :
                i += 1
            while T[j] > pivot_val :
                j -= 1
            if i >= j :
                return j
            T[i] , T[j] = T[j] , T[i]
            i += 1
            j -= 1

    def in_quick( T , left , right ) :

        pivot = get_pivot( T , left , right )

        if left < right :
            #q = partition( T , left , right , pivot )
            q = hoar_partition( T , left , right , pivot )
            in_quick( T , left , q -1 )
            in_quick( T , q + 1  ,right )

    in_quick( T, 0, len( T ) -1 )

T = [64, 1, 2, 3, 4, 5, -123, 0, 8, 45, 46, 83, -2]
quick_sort( T )
print( T )


