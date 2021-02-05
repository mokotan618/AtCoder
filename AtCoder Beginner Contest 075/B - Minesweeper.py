# https://atcoder.jp/contests/abc075/tasks/abc075_b

H, W = [int(s) for s in input().split()]

S = []
for i in range(H):
    S.append(list(input()))

# print(S)

i=1
j=1

H_list = []
W_list = []

for i in range(H-1):
    H_list.append(i)
for i in range(W-1):
    W_list.append(i)
H_list.pop(0)
W_list.pop(0)

# print(H_list)
# print(W_list)

# 中身
for i in H_list:
    for j in W_list:
        if(S[i][j] == '.'):
            count = 0
            if(S[i-1][j-1] == '#'):
                count += 1
            if(S[i-1][j] == '#'):
                count += 1
            if(S[i-1][j+1] == '#'):
                count += 1    
            if(S[i][j-1] == '#'):
                count += 1
            if(S[i][j+1] == '#'):
                count += 1
            if(S[i+1][j-1] == '#'):
                count += 1
            if(S[i+1][j] == '#'):
                count += 1
            if(S[i+1][j+1] == '#'):
                count += 1
            # print(S[i][j])
            S[i][j] = str(count)

# 四隅左上
if(S[0][0] == '.'):
    count = 0
    if(S[0][1] == '#'):
        count += 1
    if(S[1][0] == '#'):
        count += 1
    if(S[1][1] == '#'):
        count += 1
    # print(S[i][j])
    S[0][0] = str(count)

# 四隅左下
if(S[H-1][0] == '.'):
    count = 0
    if(S[H-2][0] == '#'):
        count += 1
    if(S[H-2][1] == '#'):
        count += 1
    if(S[H-1][1] == '#'):
        count += 1
    # print(S[i][j])
    S[H-1][0] = str(count)

# 四隅右下
if(S[H-1][W-1] == '.'):
    count = 0
    if(S[H-2][W-1] == '#'):
        count += 1
    if(S[H-2][W-2] == '#'):
        count += 1
    if(S[H-1][W-2] == '#'):
        count += 1
    # print(S[i][j])
    S[H-1][W-1] = str(count)

# 四隅右上
if(S[0][W-1] == '.'):
    count = 0
    if(S[0][W-2] == '#'):
        count += 1
    if(S[1][W-2] == '#'):
        count += 1
    if(S[1][W-1] == '#'):
        count += 1
    # print(S[i][j])
    S[0][W-1] = str(count)

# 上辺
for j in W_list:
    if(S[0][j] == '.'):
        count = 0
        if(S[0][j-1] == '#'):
            count += 1
        if(S[0][j+1] == '#'):
            count += 1
        if(S[1][j-1] == '#'):
            count += 1
        if(S[1][j] == '#'):
            count += 1
        if(S[1][j+1] == '#'):
            count += 1
        # print(S[i][j])
        S[0][j] = str(count)

# 左辺
for i in H_list:
    if(S[i][0] == '.'):
        count = 0
        if(S[i-1][0] == '#'):
            count += 1
        if(S[i+1][0] == '#'):
            count += 1
        if(S[i-1][1] == '#'):
            count += 1
        if(S[i][1] == '#'):
            count += 1
        if(S[i+1][1] == '#'):
            count += 1
        # print(S[i][j])
        S[i][0] = str(count)

# 底辺
for j in W_list:
    if(S[H-1][j] == '.'):
        count = 0
        if(S[H-1][j-1] == '#'):
            count += 1
        if(S[H-1][j+1] == '#'):
            count += 1
        if(S[H-2][j-1] == '#'):
            count += 1
        if(S[H-2][j] == '#'):
            count += 1
        if(S[H-2][j+1] == '#'):
            count += 1
        # print(S[i][j])
        S[H-1][j] = str(count)

# 右辺
for i in H_list:
    if(S[i][W-1] == '.'):
        count = 0
        if(S[i-1][W-1] == '#'):
            count += 1
        if(S[i+1][W-1] == '#'):
            count += 1
        if(S[i-1][W-2] == '#'):
            count += 1
        if(S[i][W-2] == '#'):
            count += 1
        if(S[i+1][W-2] == '#'):
            count += 1
        # print(S[i][j])
        S[i][W-1] = str(count)

ans = []
for i in range(H):
    ans.append(''.join(S[i]))

# print(S)
# print(ans)

for i in range(H):
    print(f'{ans[i]}') 
