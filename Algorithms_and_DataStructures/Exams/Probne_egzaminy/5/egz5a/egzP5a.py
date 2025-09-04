from egzP5atesty import runtests 

def inwestor ( T ):

    n = len( T )

    stack = []
    result = 0

    for i in range( n ) :
        while stack and T[i] < T[ stack[-1] ] :

            height = T[ stack.pop() ]
            width = i if not stack else i - stack[-1] - 1

            result = max( result , height * width )

        stack.append( i )

    while stack :
        height = T[stack.pop() ]
        width = n if not stack else n - stack[-1] - 1
        result = max( result , height * width )

    return result

"""
T = [2, 1, 5, 6, 2, 3]
print( inwestor( T ) )
"""

runtests ( inwestor, all_tests=True )