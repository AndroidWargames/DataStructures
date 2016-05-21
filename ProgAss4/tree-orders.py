# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.parent = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            if b != -1:
                self.parent[self.left[i]] = i
            self.right[i] = c
            if c != -1:
                self.parent[self.right[i]] = i

    def inOrder(self):
        self.result = []
        self.digLeft(0)
        return self.result

    def digLeft(self, i):
        if self.left[i] > -1:
            self.digLeft(self.left[i])
        self.result.append(self.key[i])
        if self.right[i] > -1:
            self.digLeft(self.right[i])

    def preOrder(self):
        self.result = []
        self.digDown(0)
        return self.result

    def digDown(self, i):
        self.result.append(self.key[i])
        if self.left[i] > -1:
            self.digDown(self.left[i])
        if self.right[i] > -1:
            self.digDown(self.right[i])

    def postOrder(self):
        self.result = []
        self.digUp(0)
        return self.result

    def digUp(self, i):
        if self.left[i] > -1:
            self.digUp(self.left[i])
        if self.right[i] > -1:
            self.digUp(self.right[i])
        self.result.append(self.key[i])


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
