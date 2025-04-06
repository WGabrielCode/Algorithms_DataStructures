def factor ( x ) :

    l = []
    while x > 1 :
        for i in range ( 2 , x + 1 ) :
            if x % i == 0 :
                l.append( i )
                x//=i
    return l
#end def

print ( factor (int ( 13 )  ) )
