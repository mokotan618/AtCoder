# https://atcoder.jp/contests/abs/tasks/arc065_a
# https://qiita.com/drken/items/fd4e5e3630d0f5859067
# これ見ちゃったよ…

import sys

S = input()

# 長さを取得して文字列Sを反転しようとしている
s_length = len(S)
s_reverse = ""
while(s_length > 0):
    s_reverse += S[s_length-1]
    s_length -= 1

D_m = "maerd" # D_m[0] = "m", D_m[4] = "d" 
D_r = "remaerd" # D_r[0] = "r", D_r[4] = "e"
E_e = "esare" # E_e[0] = "e", E_e[4] = "e"
E_r = "resare" # E_r[0] = "r", E_r[4] = "r"

# s_reverseが""になるまでif判定と文字列の削除を行う
while(s_reverse != ""):
    if(s_reverse[0] == "m") and (s_reverse[1] == "a") and (s_reverse[2] == "e") and (s_reverse[3] == "r") and (s_reverse[4] == "d"):
        s_reverse = s_reverse[5:]
    elif(s_reverse[0] == "r") and (s_reverse[1] == "e") and (s_reverse[2] == "m") and (s_reverse[3] == "a") and (s_reverse[4] == "e") and (s_reverse[5] == "r") and (s_reverse[6] == "d"):
        s_reverse = s_reverse[7:]
    elif(s_reverse[0] == "e") and (s_reverse[1] == "s") and (s_reverse[2] == "a") and (s_reverse[3] == "r") and (s_reverse[4] == "e"):
        s_reverse = s_reverse[5:]
    elif(s_reverse[0] == "r") and (s_reverse[1] == "e") and (s_reverse[2] == "s") and (s_reverse[3] == "a") and (s_reverse[4] == "r") and (s_reverse[5] == "e"):
        s_reverse = s_reverse[6:]
    else:
        print("NO")
        sys.exit()

print("YES")
# print(s_reverse)