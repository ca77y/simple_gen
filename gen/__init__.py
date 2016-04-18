from .population import init_population, multiply, mutate
from .gosia import kill_ugly, best_tofik
from pprint import pprint

MAX_GENERATIONS = 100


def find_match():
    pop = init_population()
    for gen in range(0, MAX_GENERATIONS):
        pop = kill_ugly(pop)
        kids = multiply(pop)
        kids = mutate(kids)
        pop.extend(kids)
    pprint(best_tofik)
    pprint(pop)
