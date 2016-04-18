from .population import init_population, multiply, mutate
from .gosia import kill_ugly, best_tofik, MyGuy
from pprint import pprint

MAX_GENERATIONS = 1000


def find_match():
    pop = init_population()
    for gen in range(0, MAX_GENERATIONS):
        try:
            pop = kill_ugly(pop)
        except MyGuy as ex:
            print('my perfect guy %s' % str(best_tofik))
            print('match found %s' % str(ex.tofik))
            print('after %s generations' % gen)
            break
        kids = multiply(pop)
        kids = mutate(kids)
        pop.extend(kids)
    else:
        print('forever alone')
