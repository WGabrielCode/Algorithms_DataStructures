# egz3Btest_spec.py

import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
    (10, 5, 5, 5, 13),
    (50, 10, 10, 10, 130),
    (250, 10, 10, 10, 530),
    (1000, 10, 10, 10, 2281),
    (5000, 20, 20, 20, 22653),
    (10000, 20, 20, 20, 44925),
    (20000, 20, 20, 20, 91234),
    (20000, 50, 50, 20, 93173),
    (20000, 50, 50, 50, 231322),
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

def randint_in_range(a, b):
    from testy import MY_random
    return a + MY_random() % (b-a)

def random_shuffle(T):
    from testy import MY_random
    N = len(T)
    for _ in range(N):
        idx1 = MY_random() % N
        idx2 = MY_random() % N
        T[idx1], T[idx2] = T[idx2], T[idx1]

def gentest(n, x, z, W, hint):
    X = [randint_in_range(1, x+1) for _ in range(n)]
    Z = [randint_in_range(1, z+1) for _ in range(n)] 
    return [X, Z, W], hint