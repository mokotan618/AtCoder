# import sys
# sys.exit()
# a = int(input())
# H, W = [int(s) for s in input().split()]
# txy_table = [[int(i) for i in input().split()] for num in range(N)]

N, X = [int(s) for s in input().split()]
A_N_list = [int(s) for s in input().split()]

A_new_list = []
for i in range(N):
    if(A_N_list[i] != X):
        A_new_list.append(A_N_list[i])
    

print(' '.join(map(str ,A_new_list)))