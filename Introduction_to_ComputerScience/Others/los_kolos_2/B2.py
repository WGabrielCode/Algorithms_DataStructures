def rozklad(num):
    cnt = 0
    i = 2
    while num > 1:
        if num % i == 0:
            while num % i == 0:
                num //= i
            cnt += 1
        i += 1
    return cnt == 2
# end def

def square(t):
    leng = len(t)

    for size in range(2, leng +1 ):
        for i in range(leng - size + 1 ):
            for j in range(leng - size +1):
                if rozklad( t[i][j] * t[i + size - 1][j] * t[i + size - 1][j + size - 1] * t[i][j + size - 1] ):
                    return size
    return 0
# end def

T = [
    [9, 1, 1, 1, 1],
    [1, 9, 1, 1, 1],
    [1, 1, 3, 1, 1],
    [1, 1, 1, 3, 1],
    [1, 1, 1, 1, 4],
    ]
print( square( T ) )