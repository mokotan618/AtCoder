
H, W, X, Y = map(int,input().split())

S_H = []

S_H.append(list("#"*(W+2)))
for i in range(H):
  S_temp1 = list(input())
  S_temp2 = ['#']
  S_temp2 += S_temp1
  S_temp2 += ['#']
  S_H.append(S_temp2)
S_H.append(list("#"*(W+2)))

# print(S_H)

count = -3

# 上に
for i in range(Y, 0, -1):
  if(S_H[i][X] == '#'):
    print([i,X])
    break
  count +=1

# 下に
for i in range(Y, H, 1):
  if(S_H[i][X] == '#'):
    print([i,X])
    break
  count +=1


# 右に
for i in range(X, W, 1):
  if(S_H[Y][i] == '#'):
    print([Y,i])
    break
  count +=1


# 左に
for i in range(X, 0, -1):
  if(S_H[Y][i] == '#'):
    print([Y,i])
    break
  count +=1

print(count)