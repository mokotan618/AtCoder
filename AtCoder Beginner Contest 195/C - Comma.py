# https://atcoder.jp/contests/abc195/tasks/abc195_c

N = int(input())
N_temp = N
count = 0
count_list = []

while N_temp > 0:
    count_list.append(N_temp % 1000)
    N_temp //= 1000


# for i in range(N):
#     if(i < 10**3):
#         count += 0
#     elif(10**3 <= i < 10**6):
#         count += 1
#     elif(10**6 <= i < 10**9):
#         count += 2
#     elif(10**9 <= i < 10**12):
#         count += 3
#     elif(10**12 <= i < 10**15):
#         count += 4
#     else:
#         count += 5

print(count_list)


