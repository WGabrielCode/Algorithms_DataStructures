def main(a, b):
    x = int(a/b)
    y = (a/b - int(a/b))
    l = len(str(y)) - 2
    y = int(y * 10**l)
    return y
#end def

print(main(2,3))