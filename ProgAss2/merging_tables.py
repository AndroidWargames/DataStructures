# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
#n, m = 5, 5
#lines = [1, 1, 1, 1, 1]
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)


def getParent(table):
    if parent[table] != table:
        parent[table] = getParent(parent[table])
    return parent[table]


def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    parent[source] = destination
    rank[realDestination] += rank[realSource]

    return True

for i in range(m):
    # destination, source = map(int, sys.stdin.readline().split())
    destination, source = [3, 2, 1, 5, 5][i], [5, 4, 4, 4, 3][i]
    merge(destination - 1, source - 1)

    print(max(rank))
