from zad2testy import runtests

def count_inversions(A):
    def count_invertions( T ) :
        A = [ 0 ] * (len( T ) - 1)
        count = 0

        def merge( T, left, mid, right ) :
            nonlocal A
            nonlocal count
            A[ left : right + 1 ] = T[ left : right + 1 ]
            i = left
            j = mid + 1
            k = left
            while i <= mid and j <= right :
                if A[ i ] <= A[ j ] :
                    T[ k ] = A[ i ]
                    i += 1
                else :
                    count += ( mid -i + 1 )
                    T[ k ] = A[ j ]
                    j += 1
                k += 1

            while i <= mid :
                T[ k ] = A[ i ]
                k += 1
                i += 1
            while j <= right :
                T[ k ] = A[ j ]
                k += 1
                j += 1

        def merge_count( T, left, right ) :
            if left < right :
                mid = (left + right) // 2
                merge_count( T, left, mid )
                merge_count( T, mid + 1, right )
                merge( T, left, mid, right )

        merge_count( T, 0, len( T ) - 1 )
        return count

    return count_invertions( A )


# Odkomentuj by uruchomic duze testy
# runtests( strong_string, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
runtests( count_inversions, all_tests=True )
