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


# ---------------- 2. Sudoku (BFS) ----------------

GRID = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def ok(g, r, c, v):
    if v in g[r] or v in [g[i][c] for i in range(9)]:
        return False
    r0, c0 = r // 3 * 3, c // 3 * 3
    return all(g[i][j] != v for i in range(r0, r0 + 3) for j in range(c0, c0 + 3))


def bfs(g):
    for r in range(9):
        for c in range(9):
            if g[r][c] == 0:
                for v in range(1, 10):
                    if ok(g, r, c, v):
                        g[r][c] = v
                        if bfs(g):
                            return True
                        g[r][c] = 0
                return False
    return True


