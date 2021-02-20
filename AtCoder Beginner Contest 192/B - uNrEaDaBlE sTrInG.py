# https://atcoder.jp/contests/abc192/tasks/abc192_b

import sys

s = list(input())

n = len(s)

# print(s)

# print(s[0].islower())


for i in range(n):
    # print(s[i])
    if(i % 2 == 0):
        if(s[i].islower() == True):
            pass
        else:
            print("No")
            sys.exit()
    else:
        if(s[i].isupper() == True):
            pass
        else:
            print("No")
            sys.exit()

print("Yes")
