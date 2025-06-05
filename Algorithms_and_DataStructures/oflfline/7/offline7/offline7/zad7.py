from zad7testy import runtests


def orchard(T, m):
    def orchard5( T, m ) :

        S = sum( T )
        if S % m == 0 : return 0

        S %= m

        n = len( T )
        inf = float( "inf" )
        dp = [ [ inf ] * ( m ) for _ in range( n ) ]

        for j in range( m ) :
            dp[ 0 ][ j ] = 1
        dp[ 0 ][ T[ 0 ] % m ] = 0

        for i in range( 1, n ) :
            for j in range( m ) :
                t_val = T[ i ] % m
                if j >= t_val and dp[ i - 1 ][ j - t_val ] < dp[ i ][ j ] :
                    dp[ i ][ j ] = dp[ i - 1 ][ j - t_val ]
                if dp[ i - 1 ][ j ] + 1 < dp[ i ][ j ] :
                    dp[ i ][ j ] = dp[ i - 1 ][ j ] + 1

        #	"""
        for i in range( n ) :
            print( dp[ i ], "\n" )
        # """
        res = inf
        while m > 0 :
            res = min( dp[ n - 1 ][ m ], res )
            S -= m

        return res
    return orchard5( T , m )


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
