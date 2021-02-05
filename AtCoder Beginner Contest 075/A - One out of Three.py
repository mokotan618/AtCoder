# https://atcoder.jp/contests/abc075/tasks/abc075_a

ABC_list = [int(s) for s in input().split()]

if(ABC_list[0] ==ABC_list[1]):
    print(ABC_list[2])
elif(ABC_list[0] == ABC_list[2]):
    print(ABC_list[1])
else:
    print(ABC_list[0])