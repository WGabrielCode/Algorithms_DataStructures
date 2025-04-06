class Node() :
    def __init__(self , val = None , next = None ) :
        self.val = val
        self.next = next
#end class

def cykl( p ) :
    if p == None :
        return 0
    slow = p
    fast = p

    while fast.next and fast.next.next :
        slow = slow.next
        fast = fast.next.next
        if slow == fast :
            cnt = 0
            while slow.next :
                slow = slow.next
                cnt+=1
                if slow == fast  :
                    return cnt
    return 0
#end def cykl

d = Node (6)
c = Node(4,d)
b = Node(3,c)
a = Node(2,b)
d.next = b
print( cykl( a ) )