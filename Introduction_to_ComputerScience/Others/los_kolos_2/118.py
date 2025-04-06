def sumy( t , leng ) :
    suma_w = [0 for i in range(leng)]
    suma_k = [0 for i in range(leng)]
    for i in range(leng):
        for j in range(leng):
            suma_w[i] += t[i][j]
            suma_k[j] += t[i][j]
    return suma_w , suma_k
#end def sumy

def main(t, w):
    leng = len( t )
    suma_w , suma_k = sumy( t , leng )
    min_suma = float( 'inf' )
    usun = (-1,-1)

    for i in range( leng ) :
        for j in range( i+1, leng ) :
            suma = 0
            for k in range( leng ) :

                if k!=i and k!=j :
                    suma += suma_w[ w[k] ] + suma_k[ k ] - t[ w[k] ][k]
            if min_suma > suma :
                min_suma = suma
                usun = ( i , j )
    return usun
#end def

t = [
    [9, 1, 7, 5, 3],
    [1, 8, 1, 123, 1],
    [1, 1, 6, 1, 1],
    [1, 126, 1, 1, 1],
    [1, 1, 1, 1, 9]
    ]
w = [ 1,2,3,2,1 ]
print( main( t,w ) )