# https://atcoder.jp/contests/abc193/tasks/abc193_c

n = int(input())

num_list = [ i for i in range(n+1)]
num_list.pop(0)
ans_list = []

# ans_list.append(num_list.pop(0))
# ans_list.append(num_list.pop(0))
# print(num_list)
# print(ans_list)

for i in range(n-1):
    for j in range(n-1):
        if(i <= 1) or (j <= 1):
            pass
        else:
            beki = i**j 
            if((beki in num_list) == True):
                num_list.remove(beki)
                # print("a")
                
print(len(num_list))