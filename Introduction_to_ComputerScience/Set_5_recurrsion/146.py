def main( x , n = 1 , str = '' ) :
    if x == 0 and '+' in str[:-1]:
        print( str[:-1] )
        return

    for i in range( n , x +1 ) :
        main( x - i , i , str + f"{i}+" )
#end def

main( 4 )