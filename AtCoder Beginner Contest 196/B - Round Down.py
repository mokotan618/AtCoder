# https://atcoder.jp/contests/abc196/tasks/abc196_b

import math

X = input()

# A, B = map(int,input().split('.'))

L = list(X)

# math.floor(X)

if ('.' in L) == False:
    print(X)
else:
    A, B = map(int,X.split('.'))
    print(A)
# print(L)

