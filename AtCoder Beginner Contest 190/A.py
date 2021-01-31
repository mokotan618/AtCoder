A_n_list = [int(s) for s in input().split()]

if A_n_list[0] - A_n_list[1] > 0:
    print("Takahashi")
elif A_n_list[0] - A_n_list[1] < 0:
    print("Aoki")
elif A_n_list[2] == 1:
    print("Takahashi")
else:
    print("Aoki")