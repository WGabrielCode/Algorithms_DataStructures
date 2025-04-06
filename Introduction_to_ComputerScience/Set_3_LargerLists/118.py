def ile(t, i, j):
    count = 0
    for k in range(len(t)):
        if k != i and k != j and t[i][k] == t[j][k]:
            count += 1
    return count

def main(t, N):
    leng = len(t)
    bl = [[True for _ in range(leng)] for _ in range(leng)]
    suma = 0

    for i in range(leng):
        for j in range(i + 1, leng):
            if N[i] == N[j]:
                common = ile(t, i, j)
                if bl[N[i]][i] and bl[N[j]][j]:
                    suma += common
                    bl[N[i]][i] = False
                    bl[N[j]][j] = False
    return suma

T = [
    [5, 6, 8, 12, 15],
    [10, 9, 8, 12, 15],
    [6, 6, 9, 12, 15],
    [12, 6, 8, 12, 15],
    [1, 6, 36, 12, 16]
]
N = [1, 3, 4, 0, 3]
print(main(T, N))