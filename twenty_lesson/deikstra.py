

def deikstra(graph: list, start: int, p=None, u=None, d=None):
    if d is None:
        d = {}
    if u is None:
        u = []
    if p is None:
        p = {}
    if len(p) == 0:
        p[start] = 0  # start
    for x in graph[start]:
        if x not in u and x != start:
            if x not in p.keys() or (graph[start][x] + p[start]) < p[x]:
                p[x] = graph[start][x] + p[start]

    u.append(start)

    min_v = 0
    min_x = None
    for x in p:
        if (p[x] < min_v or min_v == 0) and x not in u:
            min_x = x
            min_v = p[x]

    if len(u) < len(graph) and min_x:
        return deikstra(graph, min_x, p, u)
    else:
        return p


if __name__ == '__main__':
    # graph init
    a, b, c, d, e, f, g, h = range(8)
    N = [
        {b: 7, c: 9, f: 14},
        {a: 7, c: 10, d: 15},
        {a: 9, b: 10, d: 11, f: 2},
        {b: 15, c: 11, e: 6},
        {d: 6, f: 9},
        {a: 14, c: 2, e: 9},
        {h: 2},
        {g: 2},
    ]
    for i in range(1):
        print(deikstra(N, a))
