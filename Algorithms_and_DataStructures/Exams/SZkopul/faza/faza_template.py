def wyprawy (WI):
    return 0


"""
Uprzejmie prosimy o niemodyfikowanie poniższego kodu :)
"""

line = input()
data = list(map(int, line.strip().split()))
n = len(data) // 3
WI = [None] * n
for i in range(n):
    WI[i] = (data[i*3], data[i*3+1], data[i*3+2])
print(wyprawy(WI))