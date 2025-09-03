from egzP3atesty import runtests
from math import inf

# O( n*m*p  ) 0.53 sek.
class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

def wybory(T):
    from collections import deque
    result = 0
    for i in range( len( T ) ) :
        res = 0
        memo = { 0 : 0 }

        while T[i] is not None : # n
            val , cost , maximum = T[i].wyborcy , T[i].koszt , T[i].fundusze # p
            new_memo = memo.copy()
            for idx in memo.keys() :
                if idx + cost <= maximum :
                    key = idx + cost
                    new_val = memo[idx] + val
                    if key in new_memo :
                        new_memo[key] = max( new_memo[key] , new_val )
                    else :
                        new_memo[key] = new_val
            memo = new_memo
            T[i] = T[i].next # m

        if memo :
            result += max( memo.values() )
    return result

wyb1okr1 = Node(3, 8, 15)
wyb1okr2 = Node(2, 7, 15)
wyb1okr3 = Node(4, 5, 15)
wyb1okr1.next = wyb1okr2
wyb1okr2.next = wyb1okr3
wyb2okr1 = Node(4, 7, 8)
wyb2okr2 = Node(5, 2, 8)
wyb2okr1.next = wyb2okr2
wyb3okr1 = Node(3, 5, 10)
wyb3okr2 = Node(3, 5, 10)
wyb3okr1.next = wyb3okr2

T = [wyb1okr1, wyb2okr1, wyb3okr1]
print( wybory( T ) )

runtests(wybory, all_tests = True )