# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
# n, m = 6, 4
# lines = [10, 0, 5, 0, 3, 3]
rank = [0] * n
parent = list(range(0, n))
mx = max(lines)


def getParent(table):
    if parent[table] != table:
        parent[table] = getParent(parent[table])
    return parent[table]


def merge(destination, source):
    global mx
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return mx

    if rank[realDestination] > rank[realSource]:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        if lines[realDestination] > mx:
            mx = lines[realDestination]
    else:
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        if lines[realSource] > mx:
            mx = lines[realSource]
        if rank[realSource] == rank[realDestination]:
            rank[realSource] += 1
    return mx


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    #destination, source = [6, 6, 5, 4][i], [6, 5, 4, 3][i]
    print(merge(destination - 1, source - 1))
