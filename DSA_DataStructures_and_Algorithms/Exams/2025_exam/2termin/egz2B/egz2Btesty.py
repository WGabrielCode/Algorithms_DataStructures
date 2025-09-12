# egz2Btesty.py
from testy import *
from egz2Btest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return arg #deepcopy(arg)


def printarg( T ):
    print("Sekwencja gry    : ", limit(T))


def printhint( hint ):
    print("Wynik poprawny   : ", hint)


def printsol( sol ):
    print("Wynik algorytmu  : ", sol)


def check( T, hint, sol ):
    return hint == sol

def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    T =  [5, 4, 3, 2, 4, 3, 1] 
    hint = 3
    newtest = {}
    newtest["arg"] = [T]
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

