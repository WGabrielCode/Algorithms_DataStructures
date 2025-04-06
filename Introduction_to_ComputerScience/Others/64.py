def mak10(a, n):
    for i in range(1, n+1):
        for j in range(1, n-i+1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
        if i == 10:
            return a[n-i]
#end def

arr = [0 for _ in range(10**5)]
i = 0
while True:
    x = int(input())
    if x == 0:
        break
    arr[i] = x
    i += 1
print(mak10(arr, i))
