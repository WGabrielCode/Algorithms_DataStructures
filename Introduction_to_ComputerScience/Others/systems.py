def sys ( x , s ) :

    t = "0123456789ABCDEFG"
    tab = []
    i = 0

    while x > 0 :
        tab += t[ x % s ]
        i+=1
        x//=s
    return tab[::-1]
#end def

print ( sys ( 12 , 2 ) )

