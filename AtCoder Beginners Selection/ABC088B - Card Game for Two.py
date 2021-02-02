# https://atcoder.jp/contests/abs/tasks/abc088_b
N = int(input())
value_list = [int(s) for s in input().split()]

Alice_sum = 0
Bob_sum = 0

value_list.sort()

if N % 2 ==1:
    Alice_sum = value_list.pop()
    while value_list != []:
        Bob_sum += value_list.pop()
        Alice_sum += value_list.pop()
else:
    while value_list != []:
        Alice_sum += value_list.pop()
        Bob_sum += value_list.pop()

ans = Alice_sum - Bob_sum

print(ans)