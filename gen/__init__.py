from .population import init_population, multiply, mutate
from .gosia import kill_ugly
from pprint import pprint


def find_match():
    pop = init_population()
    pop = kill_ugly(pop)
    kids = multiply(pop)
    kids = mutate(kids)
    pop.extend(kids)
    pprint(pop)
