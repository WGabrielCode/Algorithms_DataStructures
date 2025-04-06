def roz(x):
    l = []
    if x == 0:
        return l
    i = 2
    while x > 1:
        while x % i == 0:
            l.append(i)
            x = x // i
        i += 1
    return l

def sas(a, b):
    if roz(a) == roz(b):
        return True
    return False

def zgodne(T):
    count = 0
    n = len(T)
    for i in range(n):
        has_sas = False
        for j in range(max(0, i-2), min(n, i+3)):
            if i != j and sas(T[i], T[j]):
                has_sas = True
                break
        if not has_sas:
            count += 1
    return count

t = [2,3,4,5,7,6,23,24,12,13,14,15,16,45]
print(zgodne(t))