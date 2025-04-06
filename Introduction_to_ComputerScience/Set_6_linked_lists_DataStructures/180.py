class Node():
    def __init__(self , val = None ) :
        self.val = val
        self.next = None
#end class

def fun( p , x ) :
    n_node = Node( x )
    if p == None :
        return  n_node
    head = p
    while p.next != None  :
        p = p.next
    p.next = n_node

    return head
