# python3


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def hash_func(s):
    s = s[::-1]
    ans = 0
    for c in range(len(s)):
        ans += (307 ** c) * ord(s[c])
        ans %= 1000000007
    return ans

# this function will implement rabin-karp to
def get_occurrences(pattern, text):
    l = len(pattern)
    hv = hash_func(pattern)
    locales = []
    ih = hash_func(text[0:l])
    base = 307
    mx = base ** (l - 1)
    for i in range(len(text) - l + 1):
        if hv == ih:
            if text[i:(i + l)] == pattern:
                locales.append(i)
        if i + l != len(text):
            hv = base * (hv - ord(text[i]) * mx) + ord(text[i + l])
    return locales


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

