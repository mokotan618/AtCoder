# https://atcoder.jp/contests/abc193/tasks/abc193_a

a, b = map(float,input().split())

discount = (1 - b/a) * 100

print(discount)