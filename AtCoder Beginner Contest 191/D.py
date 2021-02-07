# import sys
# sys.exit()
# a = int(input())
# H, W = [int(s) for s in input().split()]
# txy_table = [[int(i) for i in input().split()] for num in range(N)]

X_1, Y_1, R = [float(s) for s in input().split()]

count = 0

X_2 = 0
Y_2 = 0

if(abs(X_1 - R) >= abs(X_1 + R)):
    X_2 = abs(X_1 - R)
else:
    X_2 = abs(X_1 + R)

if(abs(Y_1 - R) >= abs(Y_1 + R)):
    Y_2 = abs(Y_1 - R)
else:
    Y_2 = abs(Y_1 + R)

X_3 = 0
Y_3 = 0
while(X_3 <= X_2):
    X_3 += 1
while(Y_3 <= Y_2):
    Y_3 += 1

X_3 += 1
Y_3 += 1

for X in range(-X_3, X_3):
    for Y in range(-Y_3, Y_3):
        if((X - X_1)*(X - X_1) + (Y - Y_1)*(Y - Y_1) <= R*R):
            count += 1

print(count)