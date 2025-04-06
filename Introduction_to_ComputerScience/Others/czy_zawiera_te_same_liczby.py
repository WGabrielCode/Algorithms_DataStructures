def yorn ( x , y ) :
    if len ( x ) != len ( y ) :
       return False

    for i in range (len ( x )):
        b = 1
        for j in range (len ( y)):
            if x[i] == y[j] :
                b = 0
                break
        if b :
            return False
    return True


     #   if x[i] not in y:



print ( yorn ( str (123)  , str ( 321 ) ) )