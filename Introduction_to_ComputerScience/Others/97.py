def main(t1, t2):
    leng = len(t1)
    maxi = 0

    for i in range(leng):
        for j in range(leng):
            temp = t1[i][j]
            if maxi < temp:
                maxi = temp

    arr = [0 for _ in range(maxi + 1)]
    print(arr[t1[2][4]])

    for i in range(leng):
        for j in range(leng):
            arr[t1[i][j]] += 1

    c = 0

    for i in range(maxi + 1):
        if arr[i] == 1:
            t2[c] = i
            c += 1

    return t2[:c]

t1 = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [2,5,7,9,124],
    [6,8,47,56,120],
    [1,6,9,12,16]
    ]
t2 = [0 for _ in range(25)]
print(t1[2][4])
print(main(t1, t2))