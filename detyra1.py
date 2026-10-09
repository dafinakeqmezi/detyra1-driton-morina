import itertools
import sys

# ---------------- 1. Social golfers (DFS) ----------------

N = 32


def week_ok(week, pairs):
    for g in week:
        for a, b in itertools.combinations(g, 2):
            if (a, b) in pairs:
                return False
    return True


def build_week(free, week, pairs):
    # DFS: marrim lojtarin e pare te lire dhe provojme te gjitha treshet me te
    if not free:
        return week
    first = free[0]
    for rest in itertools.combinations(free[1:], 3):
        g = (first,) + rest
        if all((a, b) not in pairs for a, b in itertools.combinations(g, 2)):
            res = build_week([p for p in free if p not in g], week + [g], pairs)
            if res:
                return res
    return None


def golfers(max_weeks=10):
    pairs, weeks = set(), []
    for _ in range(max_weeks):
        w = build_week(list(range(N)), [], pairs)
        if not w:
            break
        weeks.append(w)
        for g in w:
            pairs.update(itertools.combinations(g, 2))
    return weeks


