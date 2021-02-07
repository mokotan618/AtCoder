# import sys
# sys.exit()
# a = int(input())
# H, W = [int(s) for s in input().split()]
# txy_table = [[int(i) for i in input().split()] for num in range(N)]

V, T, S, D = [int(s) for s in input().split()]

if (D < V*T) or (V*S < D):
    print("Yes")
else:
    print("No")