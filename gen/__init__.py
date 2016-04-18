from .population import init_population
from .gosia import kill_ugly


def find_match():
    pop = init_population()
    pop = kill_ugly(pop)
    print(pop)
