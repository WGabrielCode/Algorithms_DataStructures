# kol1testy.py
from testy import *
from kol1test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return arg #deepcopy(arg)


def printarg( M, D, T ):
    print("Dlugosc ogrodzenia     : ", M)
    print("Szerokosc dla kombajnu : ", D)
    print("Lokalizacje palikow    : ", limit(T))


def printhint( hint ):
    print("Wynik poprawny       : ", hint)


def printsol( sol ):
    print("Wynik algorytmu     : ", sol)


def check( M, D, T, hint, sol ):
    return hint == sol

def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    M = 10
    D = 0.9
    T = [3.55, 7.12, 1.3, 0.6]
    hint = 2
    newtest = {}
    newtest["arg"] = [M, D, T]
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

