# https://atcoder.jp/contests/abc190/tasks/abc190_b
N, S, D = [int(i) for i in input().split()]
table = [[int(i) for i in input().split()] for N in range(N)]
# spell_list = [[int(i) for i in input().split()] for N in range(N)]

i = 0
count = 0

# whileの意味を書く
# 各呪文がOKかどうかを、呪文数(=N)分確認する
while i < N:
    # if文の意味を書く（↓のifは、OKな場合をチェック）
    # 呪文がOKかどうか（NGかどうか）
    if (S > table[i][0]) and (table[i][1] > D):
        count = 1
        # print('Yes')
        # sys.exit() # コード頭でimport sysが必要
    # if書くなら必ずelseも書く
    else:
        pass
    i += 1

# if count != 0:
if count == 1:
    print("Yes")
else:
    print("No")
