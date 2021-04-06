
S = input()

SL = list(S)

SL.append(SL.pop(0))

print("".join(SL))