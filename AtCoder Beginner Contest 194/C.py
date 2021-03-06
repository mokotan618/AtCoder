
n = int(input())

aseq = [int(i) for i in input().split()]

# print(aseq)

ans = 0
j = 0

while (len(aseq) != 1):
    temp = aseq.pop(0)
    j += 1
    for i in range (n-j):
        ans += (aseq[i] - temp) ** 2

print(ans)
