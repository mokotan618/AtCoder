# https://atcoder.jp/contests/abs/tasks/arc089_a

# 入力
# N
# t_1 x_1 y_1
# t_2 x_2 y_2
# :
# t_N x_N y_N

import sys

N = int(input())
txy_table = [[int(i) for i in input().split()] for num in range(N)]

# N = 4
# txy_table = [[3, 1, 2], [6, 1, 1], [8, 1, 1], [100, 1, 1]]

# 1からNまでの差分を考える
i = N-1
while(i > 0):
    txy_table[i][0] = txy_table[i][0] - txy_table[i-1][0]
    txy_table[i][1] = abs(txy_table[i][1] - txy_table[i-1][1])
    txy_table[i][2] = abs(txy_table[i][2] - txy_table[i-1][2])
    i -= 1

# print(txy_table)

# 以下if文はいけるかどうかの判定
# 初回は原点からの距離　２回目以降は相対座標で計算した
# 差分の処理をした時間、距離での和の偶奇が一致していればよい
for i in range(N):
    if(txy_table[i][0] >= txy_table[i][1] + txy_table[i][2]):
        if(txy_table[i][0] % 2 == ((txy_table[i][1] + txy_table[i][2]) % 2)):
            pass
        else:
            print("No")
            sys.exit()
    else:
        print("No")
        sys.exit()

print("Yes")