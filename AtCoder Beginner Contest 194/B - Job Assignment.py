# https://atcoder.jp/contests/abc194/tasks/abc194_b

n = int(input())

ab_list = [[int(i) for i in input().split()] for j in range(n)]

c_list = []

# print(ab_list)

for i in range(n):
    for j in range(n):
        if i == j:
            c_list.append(ab_list[i][0]+ab_list[j][1])
        else:
            c_list.append(max(ab_list[i][0],ab_list[j][1]))
    # print(c_list)


c_list.sort()

# print(c_list)

print(c_list[0])