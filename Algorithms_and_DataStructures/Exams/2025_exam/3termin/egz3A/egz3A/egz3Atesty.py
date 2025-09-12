# egz3Atesty.py
from testy import *
from egz3Atest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return arg #deepcopy(arg)


def printarg( H, k ):
    print("Wysokosci drzew : ", limit(H))
    print("Liczba drzew    : ", len(H))
    print("Parametr k      : ", k)


def printhint( hint ):
    if hint < 0: hint = -hint
    print("Wynik poprawny  : ", hint)


def printsol( sol ):
    print("Wynik algorytmu : ", sol)


def check( H, k, hint, sol ):
    if hint < 0: hint = -hint
    return hint == sol

def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    H = [120, 105, 140, 190, 90]
    k = 1
    hint = 4
    newtest = {}
    newtest["arg"] = [H,k]
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

