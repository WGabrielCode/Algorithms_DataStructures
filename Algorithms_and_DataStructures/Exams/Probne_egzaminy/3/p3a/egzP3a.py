from egzP3atesty import runtests
from math import inf

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
    for i in range( len( T) ) :
        res = 0
        memo = { 0 : 0 }
        while T[i].x == None :
            val , cost , maximum = T[i].wyborcy , T[i].koszt , T[i].fundusze
            #print( sorted( list( memo.keys() ) ) )
            arr = sorted( list( memo.keys() ) )
            for idx in arr :
                #a = idx + cost
                if idx + cost <= maximum :
                    key = idx + cost
                    if key in memo :
                        memo[key] = max( memo[key] , memo[idx] + val )
                    else :
                        memo[key] = memo[idx] + val
                    res = max( res , memo[key] )
            if not T[i].next :
                T[i].x = True
            else :
                T[i] = T[i].next
        print( res )
        result += res
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

#runtests(wybory, all_tests = True)