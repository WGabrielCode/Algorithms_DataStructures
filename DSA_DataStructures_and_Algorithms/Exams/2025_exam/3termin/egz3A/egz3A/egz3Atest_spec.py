# egz3Atest_spec.py

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
    (4,1,2),
    (10,10,6),
    (100,20,9),
    (1000,100000,619),
    (1000,1000000,1000),
    (3000,2000000,2827),
    (5000,10000000,5000),
    (15000,60000000,-10954),
    (16000,50000000,14037),
    (17000,60000000,-10954),
#    (10000,20000,-1),
#    (10000,200000,-1),
#    (10000,9000000,-1),
#    (100000,100000,-1),
]


def gentest(n,k, hint):
    from testy import MY_random
    notgood = True
    while notgood:
        H = [100 + (MY_random() % (10000*n)) for _ in range(n)]
        notgood = False
        HH = H.copy()
        HH.sort()
        for i in range(n-1):
            if HH[i] == HH[i+1]:
                notgood = True
                break

    if hint < 0: H.sort( reverse = True)
    
    return [H,k], hint

