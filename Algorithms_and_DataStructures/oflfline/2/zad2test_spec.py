# zad2test_spec.py

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n, hint
  (0, 0),
  (10, 22),
  (100,2451),
  (1000,248641),
  (10000,24987109),
  (100000,2493348404),
]


def gentest(n, hint):
    from testy import MY_random

    T = [MY_random() for _ in range(n)]

    return [T], hint

