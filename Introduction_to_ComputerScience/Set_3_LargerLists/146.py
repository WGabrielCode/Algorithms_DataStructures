
def main( x , n = 1 , arr = [] ) :
    if x == 0 :
        return [ arr ]
    results = []
    for i in range( n ,  x +1 ) :
        results +=main( x - i , i , arr + [i] )
    return results
#end def main

print( main( 4 ) )