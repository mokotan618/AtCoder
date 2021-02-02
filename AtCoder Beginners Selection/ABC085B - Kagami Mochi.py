# https://atcoder.jp/contests/abs/tasks/abc085_b

# ソート済みの餅は差をとることで大きさが等しかったら
# ０になることを利用して
# ０でないときif文の中身でカウントする

N = int(input())
moti_list = []
count = 0

# 餅を入れていく
for num in range(N):
    moti_list.append(int(input()))

# 餅を並べ替える
moti_list.sort()

# 確認
# print(moti_list)

# 階差を計算して0ソートしなおす
# [6, 8, 8, 10] -> [6, 2, 0, 2] ちゃんと３枚でカウントできている
i = i = N-1
while i > 0:
    moti_list[i] = moti_list[i] -moti_list[i-1]
    i -=1

# 餅を並べ替える
moti_list.sort()

# 先頭から見てif文の条件分が０でないとき餅のカウントをする

for num in range(N):
    if(moti_list.pop() != 0):
        # 確認
        # print(moti_list)
        count += 1
    else:
        pass

print(count)
