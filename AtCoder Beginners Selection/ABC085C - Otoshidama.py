# https://atcoder.jp/contests/abs/tasks/abc085_c

# いい方法が思いつかなかったので
# とりあえずfor文の総当たりで後でif文で判定しようと思った

import sys

N_mai, Y_yen = [int(i) for i in input().split()]

for x in range(N_mai+1):
    for y in range(N_mai+1):
        # zはx,y,N_maiから決まる
        z = N_mai - x - y
        if( z < 0):
            break
        else:
            pass
        # 条件文は金額と枚数が等しいかを見ていて
        # 両方等しいときプリントしている
        if(1000*z == Y_yen-5000*y-10000*x):
            print(f'{x} {y} {z}')
            sys.exit()
        else:
            pass

print(f'{-1} {-1} {-1}')