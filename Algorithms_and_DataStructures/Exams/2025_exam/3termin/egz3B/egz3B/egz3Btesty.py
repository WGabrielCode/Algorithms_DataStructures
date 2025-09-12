# egz3Btesty.py
from testy import *
from egz3Btest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return arg #deepcopy(arg)


def printarg( X, Z, W ):
    print("Punkty zwyciestwa      : ", limit(X))
    print("Punkty zdrowia         : ", limit(Z))
    print("Limit punktow zdrowia  : ", W)


def printhint( hint ):
    print("Wynik poprawny       : ", hint)


def printsol( sol ):
    print("Wynik algorytmu     : ", sol)


def check( M, D, T, hint, sol ):
    return hint == sol

def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    X = [3, 2, 2, 3]
    Z = [1, 3, 2, 3]
    W = 5
    hint = 6
    newtest = {}
    newtest["arg"] = [X, Z, W]
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

