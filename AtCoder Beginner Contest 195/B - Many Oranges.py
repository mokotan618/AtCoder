# https://atcoder.jp/contests/abc195/tasks/abc195_b

A, B, W = map(int,input().split())

m_max = (W*1000)//A+1
# n_max = (W*1000)//B+1
count_list=[]

# print(m_max)

# for i in range(int(m_max)):
#     for j in range(int(n_max)):
#         if(A*i+B*j == W*1000):
#             count_list.append(i+j)
#         else:
#             pass

# print(count_list)

count = 0
for i in range(A, B):
    for j in range(m_max):
        if A*j == W*1000:
            count_list.append(j)

print(count_list)
