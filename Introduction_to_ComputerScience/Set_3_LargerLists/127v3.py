
def fun( arr ) :
    leng = len( arr )
    for i in range( 1 , leng // 2 + 1 ) :
        if leng % i == 0 :
            template = arr[ :i ]
            if template * ( leng // i ) == arr :
                return True
    return False
#end def
def multi( t ) :
    maxc = 0
    for i in range( len( t ) ) :
        if fun( t[ i ] ) :
            maxc = max( maxc , len( t ) )
    return maxc
#end def

T = ["ABCABCABC", "AAAA", "ABABA", "asdasdczxasdwqe"]
print(multi(T))