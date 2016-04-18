from random import randint
from collections import namedtuple
from math import log


MAX_POPULATION = 8
MUTATION_CHANCE = 33
FEATURE_SIZE = 1023

Tofik = namedtuple('Tofik', ['eyes', 'hair', 'nose', 'skin'])


def gen_tofik():
    return Tofik(
        randint(0, FEATURE_SIZE),
        randint(0, FEATURE_SIZE),
        randint(0, FEATURE_SIZE),
        randint(0, FEATURE_SIZE)
    )


def init_population():
    return [gen_tofik() for i in range(0, MAX_POPULATION)]


def _sex(t1, t2):
    return Tofik(
        t1.eyes,
        t1.hair,
        t2.nose,
        t2.skin
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
        result.append(kid)
    return result


def _mutate_feature(value):
    return value ^ pow(2, randint(0, int(log(FEATURE_SIZE + 1, 2)) - 1))


def _mutate(tofik):
    return Tofik(
        tofik.eyes if randint(0, 100) > MUTATION_CHANCE else _mutate_feature(tofik.eyes),
        tofik.hair if randint(0, 100) > MUTATION_CHANCE else _mutate_feature(tofik.hair),
        tofik.nose if randint(0, 100) > MUTATION_CHANCE else _mutate_feature(tofik.nose),
        tofik.skin if randint(0, 100) > MUTATION_CHANCE else _mutate_feature(tofik.skin)
    )


def mutate(pop):
    return [_mutate(p) for p in pop]
