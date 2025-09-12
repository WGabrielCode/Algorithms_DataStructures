def grand_prix(D, C, k, s):
    return None


"""
Uprzejmie prosimy o niemodyfikowanie kodu poniżej :)
"""

line = input()
data = list(map(int, line.strip().split()))
n = data[0]
k = data[1]
s = data[2]
D = data[3 : 3+n]
C = data[3+n:3+2*n]
sol = grand_prix(D, C, k, s)
print(sol)