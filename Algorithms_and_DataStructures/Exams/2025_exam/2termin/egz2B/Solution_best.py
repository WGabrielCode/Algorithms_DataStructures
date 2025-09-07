from egz2Btesty import runtests
"""
Orientacyjny łączny czas : 0.95 sek.
Status testów: A A A A A A A A A A
# O(n) 
"""
def bitgame2(T):

    Stack = []

    for x in T:
        popped = False
        while Stack and Stack[-1] <= x :
            Stack.pop()
            popped = True

        if not popped :
            Stack.append( x )

    return len( Stack )

runtests( bitgame2, all_tests = True )