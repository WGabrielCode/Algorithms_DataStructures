def main(t1, t2):
    leng = len(t1)
    indx = [0 for _ in range(leng)]
    location = [0 for _ in range(leng)]
    z = 0

    while z < len(t2):
        mini = float('inf')
        mini_pos = -1

        for i in range(leng):
            if indx[i] < leng and t1[i][indx[i]] < mini:
                mini = t1[i][indx[i]]
                mini_pos = i

        if mini_pos == -1:
            break

        t2[z] = mini
        z += 1
        indx[mini_pos] += 1

    return t2

T1 = [
    [4, 9, 11, 16, 213],
    [1, 6, 8, 12, 15],
    [1, 6, 45, 16, 15],
    [5, 6, 65, 69, 70],
    [10, 61, 71, 81, 91]
]
T2 = [0 for _ in range(len(T1)**2)]
print(main(T1, T2))