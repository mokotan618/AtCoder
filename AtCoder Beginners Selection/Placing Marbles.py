sss = input()
value = int(sss)
#print(value)

#value = 101
count = 0

while value > 0:
    if value % 2 == 1:
        count += 1
    value //= 10

print(count)