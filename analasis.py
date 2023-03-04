from numpy import copy


def get_moves(p):
    if p == 1:
        return [(1, -1), (1, 1)]
    if p == 2:
        return [(-1, -1), (-1, 1)]
    return [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def good(bd, x, y):
    if not (0 <= x < 8) or not (0 <= y < 8):
        return False
    return not bd[x, y]


def can_cap(bd, p, x, y, vx, vy):
    if not (0 <= x < 8) or not (0 <= y < 8):
        return False
    if bd[x, y] in [0, p, -p]:
        return False
    return good(bd, x + vx, y + vy)


def move(bd, x, y, cap, mv):
    for dx, dy in get_moves(bd[x, y]):
        nx, ny = x + dx, y + dy
        if good(bd, nx, ny) and not cap:
            mv.append((nx, ny, tuple()))
        elif can_cap(bd, bd[x, y], nx, ny, nx + dx, ny + dy):
            c = cap + ((nx, ny),)
            mv.append((nx, ny, c))
            cb = copy(bd)
            cb[x, y] = 0
            cb[nx, ny] = 0
            cb[nx + dx, ny + dy] = bd[x, y]
            move(cb, nx + dx, ny + dy, c, mv)


def all_moves(bd):
    ml = {}
    for x in range(8):
        for y in range(8):
            if not bd[x, y]:
                continue
            l = []
            move(bd, x, y, tuple(), l)
            if l:
                ml[(x, y)] = l
    return ml
