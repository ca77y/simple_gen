from random import randint
from collections import namedtuple


MAX_POPULATION = 8

Tofik = namedtuple('Tofik', ['eyes', 'hair', 'nose', 'skin'])


def gen_tofik():
    return Tofik(
        randint(0, 127),
        randint(0, 127),
        randint(0, 127),
        randint(0, 127)
    )


def init_population():
    return [gen_tofik() for i in range(0, MAX_POPULATION)]


def _sex(t1, t2):
    return Tofik(
        t1.eyes ^ t2.eyes,
        t1.hair ^ t2.hair,
        t1.nose ^ t2.nose,
        t1.skin ^ t2.skin
    )


def multiply(pop):
    result = []
    while len(result) + len(pop) < MAX_POPULATION:
        k1 = randint(0, len(pop) - 1)
        k2 = randint(0, len(pop) - 1)
        k2 = k2 if k1 != k2 else (k2 + 1) % int(MAX_POPULATION / 2)

        t1 = pop[k1]
        t2 = pop[k2]
        kid = _sex(t1, t2)
        if kid not in result:
            result.append(kid)
    return result
