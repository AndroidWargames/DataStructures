# python3


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for x in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in range(len(s)):
            ans += (self._multiplier**c * ord(s[c]))
            ans %= self._prime
        return ans % self.bucket_count

    def write_search_result(self, inp):
        hh = self._hash_func(inp)
        if len(self.elems[hh]) == 0:
            print('no')
        else:
            print('yes' if inp in self.elems[hh] else 'no')

    def write_chain(self, chain):
        print(' '.join(reversed(self.elems[chain])))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(query.ind)
        elif query.type == 'find':
            self.write_search_result(query.s)
        elif query.type == 'add':
            hh = self._hash_func(query.s)
            if not (query.s in self.elems[hh]):
                self.elems[hh].append(query.s)
        elif query.type == 'del':
            hh = self._hash_func(query.s)
            if len(self.elems[hh]) > 0:
                for i in range(len(self.elems[hh])):
                    if self.elems[hh][i] == query.s:
                        del self.elems[hh][i]
                        break

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()