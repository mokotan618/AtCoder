# https://atcoder.jp/contests/abc192/tasks/abc192_d

# x = list(input())
# m = int(input())

x = [2,2]

m = 10

ws = ''.join(map(str ,x))

X = int(ws)

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

x.sort(reverse=True)

dplus = int(x[0]) + 1
count = 0

print(Base_10_to_n(22, 3))

while(int(Base_10_to_n(X, dplus)) <= m):
    print("hoge")
    count += 1
    dplus += 1

# print(dplus)
# print(m)

print(count)