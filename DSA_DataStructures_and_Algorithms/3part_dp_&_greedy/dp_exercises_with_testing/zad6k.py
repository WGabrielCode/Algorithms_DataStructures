from zad6ktesty import runtests 

def haslo ( S ):
    memo = {}

    def f( i,j ) :
        if (i,j) in memo :
            return memo[ (i,j) ]

        if i + 1 == j :
            if S[i] >= "2" and S[j] >= "7":
                res = 1
            else :
                res = 2
        elif i == j :
            return 1
        else :
            if S[j-1] == "2" and S[j] >= "7" :
                res = 0
            elif S[j-1] == 
            else :
                res = 1
            res += f( i , j-1 )
        memo[ (i,j) ] = res
        return res


    return f(0,len(S)-1)
TEST_SPEC = [
  # S (ciąg znaków S), hint (poprawna odpowiedź)
  ("27", 1),
  ("123", 3),
  ("18758", 2),
  ("12519", 6),
  ("1111019", 6),
  ("472031421512", 12),
  ("512300412351165151", 0),
  ("619873241351034132207161", 32),
  ("21311023232031235112045151", 144),
  ("61723430313251123513241611231", 0)
]
print( haslo( "18" ) )
print( haslo( TEST_SPEC[2][0] ) )
#runtests ( haslo )