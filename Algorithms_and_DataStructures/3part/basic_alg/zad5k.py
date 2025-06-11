from zad5ktesty import runtests

def garek ( T ):
    memo = {}
    def f( i , j ) :
        if (i,j) in memo :
            return memo[ (i,j) ]

        if j - i == 1 :
            res = (T[i],T[j]) if T[i] > T[j] else (T[j] , T[i] )
        elif i == j :
            res = ( T[i] , 0 )
        else :
            left = f( i+1 , j )
            right = f(i , j-1 )
            if T[i] + left[1] > T[j] + right[1] :
                res = ( T[i] + left[1] , left[0] )
            else :
                res = ( T[j] + right[1] , right[0] )

        memo[ (i,j) ] = res
        return res

    return f( 0 , len( T )-1 )[0]

T = [8,15,3,7]
print( garek( T ) )
runtests ( garek )