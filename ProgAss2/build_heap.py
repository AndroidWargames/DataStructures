# python3


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        for i in reversed(range(1,len(self._data))):
            self.upswap(i)

    def upswap(self, a):
        if self._data[a] < self._data[(a-1)//2]:
            self._data[a], self._data[(a-1)//2] = self._data[(a-1)//2], self._data[a]
            self._swaps.append([(a-1)//2, a])
            if (a-1)//2 > 0:
                self.upswap((a-1)//2)
        self.downswap(a)

    def downswap(self, a):
        b = 2 * a + 1
        c = 2 * a + 2
        z = False

        if b < len(self._data):
            if c >= len(self._data):
                if self._data[a] > self._data[b]:
                    self._data[b], self._data[a] = self._data[a], self._data[b]
                    self._swaps.append([a,b])
                    self.downswap(b)
            else:
                if self._data[a] > min(self._data[b], self._data[c]):
                    if self._data[b] < self._data[c]:
                        self._data[b], self._data[a] = self._data[a], self._data[b]
                        self._swaps.append([a,b])
                        self.downswap(b)
                    else:
                        self._data[c], self._data[a] = self._data[a], self._data[c]
                        self._swaps.append([a, c])
                        self.downswap(c)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
