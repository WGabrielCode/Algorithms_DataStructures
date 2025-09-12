
def abus(KR, OD, b, s, t):
    return -1


"""
Prosimy o niemodyfikowanie poniższego kodu :)
"""

line = input()
data = list(map(int, line.strip().split()))
E, V, b, s, t = data[:5]
KR = []
for i in range(5, 5 + E*3, 3):
    KR.append((data[i], data[i+1], data[i+2]))
OD = data[len(data) -  V: len(data)]
print(abus(KR, OD, b, s, t))