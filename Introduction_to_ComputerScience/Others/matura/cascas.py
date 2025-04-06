def nwd ( x ,y ) :
    if x == y :
        return y

    if x > y :
        return nwd ( x-y , y)
    return nwd ( y-x, x )
#end def
def nww ( x , y ) :
    return ( x * y ) // nwd( x , y )
#end def

a , b = 122 , 16

print ( nwd ( a , b ) )
print ( nww ( a , b ) )
if nww ( a,b )%a==0 and nww ( a,b )%b==0 :
    print ( "t" )
print ( )