def unify(word):
    rword = word[::-1]
    if word > rword:
        word = rword
    return word

def find_prime( x ) :
    maybe = x + 1
    while not is_prime( maybe ) :
        maybe += 1
    return maybe

def merge_sort( T ) :
    B = [0] * len(T)
    def merge(T , left , mid , right ) :
        nonlocal B
        B[left : right +1 ] = T[ left : right +1 ]
        i = left
        j = mid+1
        k = left

        while i <= mid and j <= right :
            if B[i] < B[j]  :
                T[k] = B[i]
                i += 1
            else :
                T[k] = B[j]
                j += 1
            k += 1

        while i <= mid :
            T[k] = B[i]
            i += 1
            k += 1

        while j <= right :
            T[k] = B[j]
            j += 1
            k += 1
    #end merge

    def in_sort( T , left , right ):
       if left < right :
            mid = ( left + right ) // 2
            in_sort( T , left , mid )
            in_sort( T , mid +1 , right )
            merge( T , left , mid , right )
    in_sort( T , 0 , len( T ) -1 )

def word_number( word) :
    res = 0
    w = 1
    prime = 10**7+7
    for i in range( len( word ) ) :
        res =( res + ord( word[i] ) * w ) % prime
        w = (w * 31 ) % prime
    return res

def main( T ) :

    for i in range( len( T ) ) :
        T[i] = word_number( unify( T[i] ) )
    merge_sort( T )
    print( T )

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