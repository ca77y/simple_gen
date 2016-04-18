from collections import namedtuple
from .population import gen_tofik

RankedTofik = namedtuple('RankedTofik', ['tofik', 'rank'])
best_tofik = gen_tofik()


def _hot_meter(tofik):
    tofik = tofik._asdict()
    best = best_tofik._asdict()
    result = 0
    for key in best:
        result += abs(tofik[key] - best[key])
    return result


def _rank_pop(pop):
    ranked = [RankedTofik(tofik, _hot_meter(tofik)) for tofik in pop]
    return sorted(ranked, key=lambda t: t.rank)


def kill_ugly(pop):
    ranked = _rank_pop(pop)
    surviving = list(map(lambda t: t.tofik, ranked))
    return surviving[:int(len(ranked)/2)]
