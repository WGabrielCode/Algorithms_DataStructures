def pijemy(k, PIWO):
    return None

"""
Prosimy nie modyfikować kodu poniżej :)
"""

k = int(input())
piwo = list(map(int, input().split(" ")))
n = len(piwo)
sol = [k, n] + pijemy(k, piwo)
print(" ".join(str(x) for x in sol))