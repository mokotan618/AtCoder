# https://atcoder.jp/contests/abc192/tasks/abc192_c

n, k = map(int,input().split())

def g1(n):
    s = list(str(n))
    s.sort(reverse=True)
    s = ''.join(map(str ,s))
    return int(s)

def g2(n):
    s = list(str(n))
    s.sort()
    s = ''.join(map(str ,s))
    return int(s)

def f(n):
    return g1(n) - g2(n)

# print(str(n))

# s = list(str(n))

# s.sort(reverse=True)
# print(s)
# print(''.join(map(str ,s)))
# s = ''.join(map(str ,s))

# print(int(s))

# print(g1(n))
# print(g2(n))
# print(f(n))

for i in range(k):
    n = f(n)

print(n)
