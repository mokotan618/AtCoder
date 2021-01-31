N, S, D = [int(i) for i in input().split()]
table = [[int(i) for i in input().split()] for N in range(N)]

i = 0
count = 0

while i < N:
    if S > table[i][0] 0 and D - table[i][1] > 0 :
        count = 1
    i += 1

if count != 0:
    print("Yes")
else:
    print("No")