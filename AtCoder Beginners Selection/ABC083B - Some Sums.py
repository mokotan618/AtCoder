# https://atcoder.jp/contests/abs/tasks/abc081_b
N, A, B = [int(i) for i in input().split()]

ans_sum = 0

N_list_1 = [i for i in range(N+1)]
N_list_2 = [i for i in range(N+1)]
#print(N_list)

while(N_list_1 != []):
    N_i_1 = N_list_1.pop()
    N_i_2 = N_list_2.pop()

#各桁の和を求めている
    camp = 0
    while(N_i_1 > 0):
        camp += N_i_1 % 10
        N_i_1 //= 10

    if A <= camp and camp <= B:
        ans_sum += N_i_2

print(ans_sum)