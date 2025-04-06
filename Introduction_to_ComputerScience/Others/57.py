def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True
# end def


def dec_any(x, s):
    if x == 0:
        return 0
    r=0
    while x >0:
        r = r *10 + x%s
        x //= s
    #odwrocenie:
    w=0
    while r>0:
        w = w*10 +r%10
        r //= 10
    return w
#end def

def suma(x):
    s=0
    while x>0:
        s += x%10
        x //=10
    return s
#end def

def ilpi(x):
    for i in range(2,11):
        if is_prime(suma(dec_any(x,i))):
            return True
    return False
#end def

def main(n):
    x=str(n)
    cnt=0
    for mask in range(1,1<<len(x)):
        num=''
        for i in range(len(x)):
            if mask&(1<<i):
                num+=x[i]
        if num and ilpi(int(num)):
            cnt+=1
    return cnt
#end def

