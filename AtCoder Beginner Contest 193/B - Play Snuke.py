# https://atcoder.jp/contests/abc193/tasks/abc193_b

n = int(input())

apx_list = [[int(i) for i in input().split()] for j in range(n)]

# print(n)
# print(apx_list)

count = -1
temp = 0
for i in range(n):
    if(apx_list[i][2]-1-((apx_list[i][0]*60-30)//60) > 0):
        temp = apx_list[i][1]
        if(count == -1):
            count = temp
        elif(count > temp):
            count = temp
        else:
            pass
        # count += apx_list[i][1]
        # print(count)
    else:
        pass

print(count)