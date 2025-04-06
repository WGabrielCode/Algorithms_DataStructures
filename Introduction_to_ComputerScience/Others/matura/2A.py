def napraw ( t ) :
    return t
#end def

ogrod = [ [" "," "," "," "," "],
          [" ","\\"," ","\\"," "],
          [" "," "," "," "," "],
          ["\\"," "," ","/"," "],
          [" ","\\"," "," ","/"] ]
ogrod = ( napraw ( ogrod ) )


for i in range ( 5 )  :
    for j in range ( 5 ) :
        print ( ogrod[i][j], end = ' ' )
    print ()
