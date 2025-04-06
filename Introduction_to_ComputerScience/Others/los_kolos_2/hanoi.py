def hanoi(x):
    def infun(x, a, b, c):
        nonlocal i
        if x == 1:
            i += 1
            return
        else:
            infun(x - 1, a, c, b)
            i += 1
            infun(x - 1, c, b, a)
    i = 0
    infun(x, 'a', 'c', 'b')
    return i
# end def
print(hanoi(3))
