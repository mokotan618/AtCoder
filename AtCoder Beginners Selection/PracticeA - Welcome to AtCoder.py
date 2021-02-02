# https://atcoder.jp/contests/abs/tasks/practice_1
a = int(input())
b_c = [int(s) for s in input().split()]
s = input()

# print(a)
# #print(b_c[0])
# #print(b_c[1])
# #print(s)
sum_abc = a + b_c[0] + b_c[1]
print(f'{sum_abc} {s}')