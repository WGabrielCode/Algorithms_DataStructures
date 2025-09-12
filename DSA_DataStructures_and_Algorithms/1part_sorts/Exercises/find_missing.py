#( znajdz najmniejsza nie zawierajaca sie w lsiscie liczbe )
# #posortowana lista o dlugosci len(t) = n , zawiera wartosci {0,...,m} , m>n

def quick_sort( T ) :
    def hoars_partiton( T , left , right ) :
        pivot = T[ ( left + right ) // 2 ]
        i = left
        j = right
        while True :
            while pivot > T[i] :
                i += 1
            while pivot < T[j] :
                j -= 1
            if i >= j :
                return j
            T[i] , T[j] = T[j] , T[i]
            i += 1
            j -= 1

    def in_quick( T , left , right ) :
        if left < right  :
            q = hoars_partiton( T , left , right )
            in_quick( T , left , q )
            in_quick( T , q+1 , right )
    in_quick( T , 0 , len( T )-1 )

def find_missing( t  ) :
   quick_sort( t )
   n = len( t )
   i = t[0]
   for num in t :
       if i == num :
           i += 1
       else :
           return i

#end

T = [8,3,1,5,8,4,2,1,5,83,-123,46,3,1,64,45,45,45,45,45,1,0,-2]
print( find_missing( T ) )