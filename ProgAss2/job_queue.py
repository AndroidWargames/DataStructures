# python3


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)
        self.size = 0
        self.H = [0]*self.num_workers
        self.W = list(range(self.num_workers))

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        self.assigned_workers = []
        self.start_times = []
        time = 0
        j = 0
        while len(self.start_times) < len(self.jobs):
            while time >= self.H(0):
                self.assigned_workers[j] = self.W[j]
                self.start_times[j] = time
                self.extractmax()
                self.insert(time + self.jobs[j], self.assigned_workers[j])
                j += 1
            time += 1

    def parent(self, i):
        return (i - 1) // 2

    def leftchild(self, i):
        return 2 * i + 1

    def rightchild(self, i):
        return 2 * i + 2

    def swap(self, a, b):
        self.H[a], self.H[b] = self.H[b], self.H[a]
        self.W[a], self.W[b] = self.W[b], self.W[a]

    def siftup(self, i):
        while i > 0 and (self.H[self.parent(i)] > self.H[i] or (self.H[self.parent(i)] == self.H(i) and self.W[self.parent(i)] > self.W[i])):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def siftDown(self, i):
        maxindex = i
        l = self.leftchild(i)
        if l < self.size:
            if self.H[l] < self.H[maxindex]:
                maxindex = l
            elif self.H[l] == self.H[maxindex] and self.W[l] < self.H[maxindex]:
                maxindex = l
        r = self.rightchild(i)
        if r < self.size:
            if self.H[r] < self.H[maxindex]:
                maxindex = r
            elif self.H[r] == self.H[maxindex] and self.W[r] < self.H[maxindex]:
                maxindex = r
        if i != maxindex:
            self.swap(self.H[i], self.H[maxindex])
            self.siftDown(maxindex)

    def insert(self, p, w):
        self.size += 1
        self.H[self.size] = p
        self.W[self.size] = w
        self.siftup(self.size)

    def extractmax(self):
        result = self.H[0]
        self.H[0] = self.H[self.size - 1]
        self.W[0] = self.W[self.size - 1]
        self.size -= 1
        self.siftDown(1)
        return result

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

