def nwd ( x , y ) :
    while x != y  :
        if x < y  :
            x, y = y-x , x
        else :
            x ,y = x - y , y
    return x
#end def
def nww ( x, y ) :
    return ( x * y ) // nwd (x , y )

def main ( a , b , c ) :
    return nww ( a , nww ( b , c ) )

#end def

print ( main ( 12, 13 , 14  ) )