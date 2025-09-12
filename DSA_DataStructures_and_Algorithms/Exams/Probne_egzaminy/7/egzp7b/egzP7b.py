from egzP7btesty import runtests


def ogrod( S, V ) :
    n = len( S )
    m = len( V )

    # Precomputation of prefix sums (your `times_used` array)
    prefix_counts = [ [ 0 ] * m for _ in range( n + 1 ) ]
    for i in range( n ) :
        for j in range( m ) :
            prefix_counts[ i + 1 ][ j ] = prefix_counts[ i ][ j ]
        prefix_counts[ i + 1 ][ S[ i ] - 1 ] += 1

    max_profit = 0

    # Iterate through all subsegments
    for i in range( n ) :  # start of segment
        for j in range( i, n ) :  # end of segment

            # Now we have the counts for the segment S[i..j]
            # Use the precomputed array to get counts efficiently
            segment_counts = [ prefix_counts[ j ][ k ] - prefix_counts[ i ][ k ] for k in range( m ) ]

            # Iterate through all fruit types to "remove"
            for removed_type in range( m ) :  # 0-indexed types

                current_profit = 0
                for fruit_type in range( m ) :
                    if fruit_type != removed_type :
                        # Profit is count of fruit_type * its value
                        current_profit += segment_counts[ fruit_type ] * V[ fruit_type ]

                max_profit = max( max_profit, current_profit )
    return max_profit

S = [2, 3, 1, 1, 4, 1, 2, 4, 1]
V = [5, 3, 6, 6]
print( ogrod( S , V ) )

#runtests( ogrod, all_tests = True)