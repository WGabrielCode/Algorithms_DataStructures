class Node:
    def __init__(self, val=None):  # Wartość domyślna val to None
        self.val = val
        self.next = None

def wypisz1(p):
    while p != None:
        print(p.val)
        p = p.next

first = None
for i in range(4):
    s = int(input('>>'))
    p = Node()  # Możemy tworzyć węzeł bez podania wartości
    p.val = s   # Przypisanie wartości
    p.next = first
    first = p

wypisz1(first)



"""
def wypisz1(p):
    while p != None:
        print(p.val)
    p = p.next

class Node:
    def __init__(self, val):
        self.val = None
        self.next = None

first = None
for i in range(4):
    s = int(input('>>'))
    p = Node()
    p.val = s
    p.next = first
    first = p
wypisz1(first)
"""