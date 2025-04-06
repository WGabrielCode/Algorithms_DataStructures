def sys4(x):
    r = 0
    while x > 0:
        r = r*10 + x%4
        x //= 4
    w = 0
    #odwrocenie liczby r
    while r > 0:
        w = w*10 + r%10
        r //= 10
    return w

def zgodna(a, b):
    for i in range(10):
        if sys4(a) % 10 == sys4(b) % 10:
            return True
        a //= 4
        b //= 4
    return False

print(zgodna(int(input()), int(input())))