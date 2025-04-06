class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None


# end class

def first(p):
    if p == None:
        return p
    slow = p
    fast = p

    while fast.next and fast.next.next :
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow2 = p
            prev = p
            slow = slow.next
            slow2 = slow2.next
            while True:
                if slow == slow2:
                    return prev
                prev = slow2
                slow = slow.next
                slow2 = slow2.next

# end def