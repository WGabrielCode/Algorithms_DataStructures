# egz2Btest_spec.py

import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


TEST_SPEC = [
        (25, 500, 21),
        (900, 110000, 857),
        (4900, 1100000, 3742),
        (7400, 1100000, 5000),
        (11000, 2200000, 5792),
        (300100, 11000000, 284),
        (760000, 22000000, 396),
        (1100000, 60000000, 310),
        (1250000, 200000000, 136),
]

def pseudo_shuffle(T):
    from testy import MY_random
    N = len(T)
    D = max(5, N//100)
    for _ in range(D):
        idx1 = MY_random() % N
        idx2 = idx1 + (MY_random() % D)
        if idx2 < N:
            T[idx1], T[idx2] = T[idx2], T[idx1]

def gentest(N, M, hint):
    from testy import MY_random
    T = [MY_random() % M + 1 for _ in range(N)]
    T.sort(reverse=True)
    pseudo_shuffle(T)
    return [T], hint

