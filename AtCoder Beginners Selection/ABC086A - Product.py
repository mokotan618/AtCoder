# https://atcoder.jp/contests/abs/tasks/abc086_a
value_list = [int(s) for s in input().split()]
product_ab = value_list[0] * value_list[1]
if product_ab % 2 == 1:
    print("Odd")
else:
    print("Even")
