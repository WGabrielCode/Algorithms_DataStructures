
def sort_policzbach( T ) :

    B = [0 for i in range( len( T ) ) ]

    def merge( T , left , mid , right ) :
        nonlocal B
        B[left : right+1 ] = T[left : right+1 ]

        i = left
        j = mid +1
        k = left

        while i <= mid and j <= right :

            if len( B[i] ) < len( B[j] ) :
                T[k] = B[i]
                i += 1
            else :
                T[k] = B[j]
                j += 1
            k += 1

        while j <= right :
            T[k] = B[j]
            j+=1
            k+=1

        while i <= mid :
            T[k] =B[i]
            i+=1
            k+=1
    #end merge

    def in_merge( T , left , right ) :
        if left < right :
            mid = ( left + right ) // 2

            in_merge( T , left , mid )
            in_merge( T , mid +1 , right )
            merge( T , left , mid , right )
    #end in

    in_merge( T , 0 , len( T )-1 )
 #end

def str_sort( T ) :

    B = [0 for i in range( len( T ) ) ]

    def merge( T , left , mid , right ) :
        nonlocal B
        B[left : right+1 ] = T[left : right+1 ]

        i = left
        j = mid +1
        k = left

        while i <= mid and j <= right :

            if B[i] < B[j] :
                T[k] = B[i]
                i += 1
            else :
                T[k] = B[j]
                j += 1
            k += 1

        while j <= right :
            T[k] = B[j]
            j+=1
            k+=1

        while i <= mid :
            T[k] =B[i]
            i+=1
            k+=1
    #end merge

    def in_merge( T , left , right ) :
        if left < right :
            mid = ( left + right ) // 2

            in_merge( T , left , mid )
            in_merge( T , mid +1 , right )
            merge( T , left , mid , right )
    #end in

    def unify(word):
        rword = word[::-1]
        if word > rword:
            word = rword
        return word

    start = 0
    for i in range( 1 , len( T ) ) :
        T[ i-1 ] = unify( T[i-1] )
        if len( T[i-1] ) != len( T[i] ) :
            in_merge( T , start , i-1 )
            start = i
    T[-1] = unify( T[-1] )
    in_merge( T , start , len( T ) -1 )
 #end

def main( T ) :
    sort_policzbach( T )
    str_sort( T )
    max_c = 0
    c = 1
    for i in range( 1 , len( T ) ) :

        if T[i-1] != T[i] :
            c = 0
        c+=1

        max_c = max( max_c , c )
    return max_c


T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
#T = ["kot"]*10
print( main( T ) )


