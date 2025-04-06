#sortowania

def insertion( t ) :
    for i in range( 1 , len( t ) ) :
        for j in range( i , 0 , -1 ) :
            if t[j] < t[j-1] :
                t[j] , t[j-1] = t[j-1] , t[j]
            else :
                break
    print( t , "insertion sort ")
    #end def

def insertion2( t ) :
    for i in range( 1 , len( t ) ) :
        for j in range( i-1, -1 , -1 ) :
            if t[j] > t[j+1] :
                t[j] ,t[j+1] = t[j+1] , t[j]
            else :
                break
    print( t , "insertion 2 ")
    #end def

def swapping_insert(t):
    for i in range(1, len(t)):
        curNum = t[i]
        j = i
        while j > 0 and t[j-1] > curNum:
            t[j] = t[j-1]
            j -= 1
        t[j] = curNum
    print(t, "swap")

def bb( t ) :
    for i in range( len(t) ) :
        for j in range( len( t ) -1-i ) :
            if t[j] > t[j+1] :
                t[j] , t[j+1] = t[j+1] , t[j]
    print( t , " bb")
def mm( t ) :
    min_g = max_g = t[-1]


    for i in range( 0 , len( t ) -1 , 2 ) :
        if t[i] > t[i+1] :
            min_g = min( t[i+1] , min_g)
            max_g = max( t[i] , max_g )
        else :
            max_g = max(t[i + 1], max_g)
            min_g = min(t[i], min_g)

    print( min_g , max_g )

T = [8,3,1,5,8,4,2,1,5,83,-123,46,3,1,64,45,45,45,45,45,1,0,-2,-200,-210]
insertion( T.copy() )
insertion2( T.copy() )
swapping_insert( T.copy() )
bb( T.copy() )
mm( T.copy() )