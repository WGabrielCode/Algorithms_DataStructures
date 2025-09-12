# egz2Atesty.py
from testy import *
from egz2Atest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return arg #deepcopy(arg)


def printarg( V,E,D,K,Q,B ):
    print("Liczba miast    : ", V)
    print("Drogi           : ", limit(E) )
    print("Liczba dni      : ", D )
    print("Miasta krola    : ", limit(K) )
    print("Miasta krolowej : ", limit(Q) )
    print("Miasta dywersji : ", limit(B) )


def printhint( hint ):
    print("Wynik poprawny  : ", hint)


def printsol( sol ):
    print("Wynik algorytmu : ", sol)


def check( V,E,D,K,Q,B, hint, sol ):
    return hint == sol

def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    V = 9
    E = [(0,1),(0,2),(2,1), (2,3),(5,2),(4,2),
         (3,4),(4,5),(5,6), (8,6),(7,8),(6,7) ]
    D = 3
    K = [0,5,7]
    Q = [3,6,0]
    B = [2,2,5]
    
    hint = 1
    newtest = {}
    newtest["arg"] = [V,E,D,K,Q,B]
    newtest["hint"] = hint
    TESTS.append(newtest)

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    return TESTS


def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

