def is_( str ) :
    leng = len( str )
    for i in range( 1, leng // 2 +1 ) :
        if leng % i == 0 :
            template = str[ :i]
            if template * (leng // i ) == str :
                return True
    return False
#end def

def multi( t ) :
    maxc = 0
    for str in t :
        if is_( str ) :
            maxc = max( maxc, len( str ) )
    return maxc

#end def

T = ["ABCABCABC", "AAAA", "ABABA", "asdasdczxasdwqe"]
print( multi( T ) )