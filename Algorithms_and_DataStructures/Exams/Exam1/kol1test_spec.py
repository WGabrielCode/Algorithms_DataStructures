# kol1test_spec.py

import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
        (101, 0.3, 10, 18),
        (10092, 160.5, 100, 17),
        (90071, 98.8, 1000, 313),
        (900001, 89.3, 10000, 3661),
        (211, 0.0007, 200000, 103123),
        (3000, 0.3, 300000, 0),
        (4000, 0.01, 400000, 44041),
        (5000, 0.025, 500000, 1),
        (6000, 0.015, 600000, 65),
]

def random_float():
    from testy import MY_random, MY_modulus
    return MY_random() / MY_modulus

def random_in_range(a, b):
    from testy import MY_random
    r = random_float()
    while r == 0:
        r = random_float()
    return a + (b - a) * r

def random_shuffle(T):
    from testy import MY_random
    N = len(T)
    for _ in range(N):
        idx1 = MY_random() % N
        idx2 = MY_random() % N
        T[idx1], T[idx2] = T[idx2], T[idx1]

def gentest(M, D, N, hint):
    p = random_in_range(0, M)
    if M%10 > 0:
        T = [random_in_range(0, p) for _ in range(N)]
        T.extend([random_in_range(p, M) for _ in range(N)])
        random_shuffle(T)
    else:
        T = [p-p/(N+1)*(i+1) for i in range(N)]
        T.extend([random_in_range(p, M) for _ in range(N)])
    return [M, D, T], hint

