class Node:
    def __init__(self , val = None ) :
        self.val = val
        self.next = None
    #end def
#end class

def sort( p , q ) :

    if p == None : return q
    if q == None : return p

    dummy = Node()
    current = dummy

    while p != None and q != None :
        if p.val < q.val :
           current.next = p
           p = p.next
        else :
            current.next = q
            q = q.next
        current = current.next
    #end while
    if p != None :
        current.next = p
    if q != None :
        current.next = q

    return dummy.next