n = int(input())
A_n_list = [int(s) for s in input().split()]

count = 0
ans = 0

while(1):
    for A_n in A_n_list:
        if A_n % 2 == 0:
            count += 1
    if count == n:
        i = 0
        for A_n in A_n_list:
            A_n_list[i] = A_n // 2
            i += 1
        # print(A_n_list)
        ans += 1
        count = 0
    else:
        break

print(ans)