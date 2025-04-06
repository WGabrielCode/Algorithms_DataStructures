def dev ( x ) :
    l = [1]
    for i in range(2, x):
        if x % i == 0:
            l.append(i)
    return list ( set ( l )  )
#end def
def sum1 ( l ) :
    r=0
    while len(l) :
        r+=l[-1]
        l.pop()

    return r
#end def
def is_perf ( x ) :
    if x == sum1( dev ( x ) ) :
        return True
    return False
#end def

print ( is_perf ( 6 ) )