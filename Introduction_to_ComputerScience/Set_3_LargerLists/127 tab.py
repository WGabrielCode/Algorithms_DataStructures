def is_( arr ) :
    leng = len( arr )
    for i in range( 1 , leng // 2 + 1 ) :
        if leng % i == 0 :
            template = [0] * leng
            for j in range( i ) :
                template += arr[ j ]
            if arr == template * ( leng // i ) :
                return True
    return False
#end def

def multi( t ) :
    maxc = 0
    for i in range( len( t ) ) :
        if is_( t[ i ] ) :
            maxc = max( maxc , len( t[ i ] ) )
    return maxc
#end def

T = [  ['A', 'B', 'C', 'A', 'B', 'C', 'B', 'B', 'C'],
  ['1', '1', '1', '1'],
  ['A', 'B', 'A', 'B', 'A'],
  ['a', 's', 'd', 'a', 's', 'd', 'c', 'z', 'x', 'a', 's', 'd', 'w', 'q', 'e']
]
print( multi( T ) )