class Node() :
    def __init__(self , val = None , next = None ) :
        self.val = val
        self.next = next
#end class

def cnt_of( p ) :
    if p == None :
        return 0
    fast = p
    slow = p

    while fast.next != None and fast.next.next != None :
        fast = fast.next.next
        slow = slow.next

        if slow == fast :
            slow2 = p
            cnt = 0
            while slow2 != slow :
                cnt+=1
                slow2 = slow2.next
                slow = slow.next
            return cnt
    return 0
#end def cnt_of

d = Node (6)
c = Node(4,d)
b = Node(3,c)
a = Node(2,b)
d.next = b

print( cnt_of( a ) )