class Node():
    def __init__(self , val = None ) :
        self.val = val
        self.next = None
#end class
def reverse( p ) :
    prev = None
    current = p

    while current != None :
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev