A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0

for A in range(A+1):
    for B in range(B+1):
        for C in range(C+1):
            print(f'500*{A}+100*{B}+50*{C} = {X}')
            if 500*A+100*B+50*C == X:
                ans += 1 

print(ans)
