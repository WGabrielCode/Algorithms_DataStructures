def is_prime ( x ) :
    if x < 2 :
        return False
    i=2
    while i * i <= x :
        if  x % i == 0  :
            return False
        i+=1
    return True
#end def

def is_rising ( n ) :
    while n > 0:
        t = n % 10
        n //= 10
        if x==0 :
            break
        if n % 10 >= t :
            return False
    return True
#end def

def suma( x ) :
    s=0
    while x > 0 :
        s += x%10
        x//=10
    return s
#end def
def re_silnia( x ) :
    t=0
    while x > 0  :
        t = t*10 + x%10
        x-=1
    r=0
    while t > 0 :
        r = r*10  +t%10
        t//=10
    return r

def main( n ) :
    for i in range( 29, re_silnia(n) ) :
        if is_prime(i) :
            if suma(i) == n :
                if is_rising(i) :
                    return i
#end def
print  (main(20) )