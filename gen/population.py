from random import randint
from collections import namedtuple


MAX_POPULATION = 10

Tofik = namedtuple('Tofik', ['eyes', 'hair', 'nose', 'skin'])


def gen_tofik():
    return Tofik(
        randint(0, 100),
        randint(0, 100),
        randint(0, 100),
        randint(0, 100)
    )


def init_population():
    return [gen_tofik() for i in range(0, MAX_POPULATION)]
