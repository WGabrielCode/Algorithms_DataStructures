def prime( x ) :
    if x<2 :
        return False
    i=2
    while i * i <= x :
        if x % i == 0 :
            return False
        i += 1
    return True
#end def

def suma( x ) :
    s=0
    while x > 0 :
        s += x%10
        x //= 10
    return s
#end def

def is_rising ( n ) :
    while n > 0:
        t = n % 10
        n //= 10
        if n % 10 >= t :
            return True
    return False
#end def

def not_rising(x):

    while x > 0:
        t = x % 10
        x //= 10
        if x == 0 :
            break
        if t > x % 10 :
            return False
    return True


def main( x ) :
    i = 11
    while True:
        if prime(i) and not_rising(i) and suma(i) == x :
            return i
        i+=1
#end def

print( main( int ( 101 )  ) )

