def rev ( r ) :
    w = ""
    for i in range(len(r) - 1, -1, -1):
        w += r[i]
    return w
#end def

def dec_any( x, s ) :
    tab = "0123456789ABCDEFG"
    r =""
    while x > 0 :
        r += tab[ x%s ]
        x //= s
    r=rev(r)
    return r
#end def
def fun( x , y ) :
    for i in range( len( x ) ) :
        for j in range ( len( y ) ) :
            if x[i] == y[j] :
                return False
    return True
#end def

def main( a , b ) :
    for i in range ( 2 ,17 ) :
        if  fun ( dec_any( a , i ) , dec_any( b , i ) ) :
            return i
    return -1
#end def

print( main(123 ,522  )  )


