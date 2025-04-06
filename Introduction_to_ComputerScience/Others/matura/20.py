def fib21 ( a , b ) :
    il = b / a
    eps = 1e-6
    while True :
        a, b = b, a + b
        if  not abs(( b/a ) -il ) > eps :
            return il
        il = b / a
#end def

print ( fib21 ( 1, 1 )  )