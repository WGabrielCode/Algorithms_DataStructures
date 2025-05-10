# kol1testy.py
from testy import *
from kol2test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return arg #deepcopy(arg)

def printarg(T):
    start_city, flights, resorts = T
    print("\nMiasto startowe\t: ", start_city)
    print("Połączenia\t: ", limit(flights))
    print("Ośrodki wypoczynkowe\t: ", limit(resorts))


def printhint( hint ):
    print("\nWynik poprawny         : ", hint)


def printsol( sol ):
    print("Wynik algorytmu        : ", sol, end="\n\n")


def check( T, hint, sol ):
    return hint == sol

def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []


    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        #print(arg)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)
#        print(TESTS)
#    print(TESTS)
    return TESTS


def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

