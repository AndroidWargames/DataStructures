# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.x = [0] * self.n

    def compute_height(self):

        for i in range(self.n):
            if self.x[i] == 0:
                self.parent_height(i)
        return max(self.x)

    def parent_height(self, i):
        v = self.x[self.parent[i]]
        if self.parent[i] == -1:
            self.x[i] = 1
        elif v != 0:
            self.x[i] = v + 1
        else:
            self.parent_height(self.parent[i])
            v = self.x[self.parent[i]]
            self.x[i] = v + 1


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
