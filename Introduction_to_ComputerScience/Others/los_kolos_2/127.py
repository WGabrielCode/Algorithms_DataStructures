def is_rep( str ) :
    leng = len( str )

    for i in range( 1,leng//2 + 1) :
        if leng % i == 0 :
            tmp = ""
            while len( tmp ) < leng :
                tmp = tmp + str[:i]
            if tmp == str :
                return True
    return False
#end def is_rep ( funkcja sprawdzajaca czy string sklada sie z napisow wielokrotnych

def multi( t ) :
    maks = 0

    for i in t :
        if is_rep( i ) :
            maks = max ( maks , len( i ) )
    return maks
#end def multi

T = [ "BCABCABCA", "AAAA", "ABAABA" ]
print( multi( T ) )