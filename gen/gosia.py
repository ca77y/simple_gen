from collections import namedtuple
from .population import gen_tofik

RankedTofik = namedtuple('RankedTofik', ['tofik', 'rank'])
best_tofik = gen_tofik()

PERFECT_MATCH = 20


class MyGuy(Exception):

    def __init__(self, tofik):
        self.tofik = tofik


def _hot_meter(tofik):
    actual = tofik._asdict()
    best = best_tofik._asdict()
    result = 0
    for key in best:
        result += abs(actual[key] - best[key])
    if result < PERFECT_MATCH:
        raise MyGuy(tofik)
    return result


def _rank_pop(pop):
    ranked = [RankedTofik(tofik, _hot_meter(tofik)) for tofik in pop]
    return sorted(ranked, key=lambda t: t.rank)


def kill_ugly(pop):
    ranked = _rank_pop(pop)
    surviving = list(map(lambda t: t.tofik, ranked))
    return surviving[:int(len(ranked)/2)]
