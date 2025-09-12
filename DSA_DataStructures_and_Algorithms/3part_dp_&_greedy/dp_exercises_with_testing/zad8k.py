from zad8ktesty import runtests 

def napraw ( s, t ):
    sn = len( s )
    tn = len( t )
    inf = float( "inf" )
    dp = [ [inf]*tn for i in range( sn ) ]
    if s[0] == t[0] :
        dp[0][0] = 0
    else : dp[0][0] = 1


    for j in range( sn ) :
        dp[]
    return

s = "swidry"
t = "kawiory"

print( napraw( s , t ) )
runtests ( napraw )