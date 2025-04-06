def rozklad ( x )  :
    tab = [ False for _ in range ( 999 ) ]
    i=2
    while x > 1 :
        if x % i == 0 :
            tab [ i ] = True
            x//=i
            i=1
        i+=1
    return tab
#end def

def main ( t ) :
    czydobra = [0 for _ in range ( len ( t ) ) ]

    for i in range ( 1 , len( t ) ) :
        for j in range ( max ( 0,i-2) , i ) :
            if rozklad( int (t[i]) ) == rozklad ( int (t[j]) ) :
                czydobra[i] = 1
                czydobra[j] = 1
    '''
    for i in range(0, len(t)):
        if czydobra[i]==1 :
            print( t[i], "")
    '''
    return sum (czydobra )
#end def

#T =  [6, 24]
T = [2,3,4,5,7,6,23,24,12,13,14,15,16,45]
print ( main ( T ) )