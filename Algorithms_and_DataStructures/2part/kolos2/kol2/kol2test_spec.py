from testy import MY_random, MY_modulus
ALLOWED_TIME = 3


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# (|cities|, |flights|, |resorts|, sol)
    (5, 6, 3, 60),
    (6, 8, 2, 18),
    (51, 90, 5, 199046262),
    (200, 600, 10, 352264166),
    (500, 10000, 10, 43584260),
    (1000, 50001, 100, 482881890),
    (2001, 200000, 100, 191398500),
    (3000, 300000, 1000, 3266931396),
    (4001, 500000, 1000, 2045797948),
    (5000, 900000, 1000, 2452412242)
]


def custom_test_A():
    start_city = 0
    flights = [(0, 1, 2), (0, 2, 4), (0, 3, 8), (3, 4, 16), (1, 4, 1), (2, 4, 1)]
    resorts = [1, 2, 4]
    hint = 60
    return (start_city, flights, resorts), hint

def custom_test_B():
    start_city = 0
    flights = [(0, 1, 2), (0, 2, 1), (0, 3, 10), (0, 4, 5), (5, 1, 6), (5, 2, 1), (5, 3, 10), (5, 4, 3)]
    resorts = [2, 5]
    hint = 18
    return (start_city, flights, resorts), hint

def gentest(cities_num, flights_num, res_num, hint):
    if cities_num == 5:
        return custom_test_A()
    if cities_num == 6:
        return custom_test_B()
    
    from testy import MY_random

    def get_random_cost():
        cost = MY_random() % 12348793
        while cost < 100000:
            cost = MY_random() % 12348793
        return cost
        #if cities_num <= 20:
        #    return MY_random() % 10 + 1
        #return MY_random() % min((2 ** 16), cities_num ** 2) + 1

    def get_random_city(lo = 0, hi = cities_num):
        if lo == hi:
            return lo
        return lo + MY_random() % (hi - lo)
    
    # create core flights
    flights = set()
    for city_id in range(cities_num - 1):
        flights.add((city_id, city_id + 1))

    not_visited = set(range(cities_num))
    resorts = set()

    # define resorts
    while len(resorts) < res_num:
        city = get_random_city(lo=1, hi=cities_num - 1)
        while city in resorts or city == 0:
            city = get_random_city(lo=1, hi=cities_num - 1)
        resorts.add(city)

    not_visited = not_visited - resorts

    # handle resorts cities
    for res_id in resorts:
        connection_city = get_random_city(hi=res_id - 1)
        while not connection_city in not_visited:
            connection_city = get_random_city(hi=res_id - 1)

        flights.add((connection_city, res_id))

    for _ in range(flights_num - len(flights)):
        city_A, city_B = get_random_city(), get_random_city()
        while city_A == city_B or (city_A, city_B) in flights or (city_B, city_A) in flights:
            city_A, city_B = get_random_city(), get_random_city()
        flights.add((city_A, city_B))

    # create permutation
    permutation = list(range(cities_num))
    for _ in range(3 * cities_num):
        city_A, city_B = get_random_city(), get_random_city()
        while city_A == city_B :
            city_A, city_B = get_random_city(), get_random_city()
        permutation[city_A], permutation[city_B] = permutation[city_B], permutation[city_A]

    # permutate flights
    flights = list(flights)
    for i in range(len(flights)):
        city_A, city_B = flights[i]
        flights[i] = (permutation[city_A], permutation[city_B], get_random_cost())

    city_start = permutation[0]

    # permutate resorts
    resorts = list(resorts)
    for i in range(len(resorts)):
        resorts[i] = permutation[resorts[i]]

    return (city_start, flights, resorts), hint