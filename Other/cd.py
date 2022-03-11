a = int(input())
b = int(input())
c = int(input())
for i in range(a-1):
    b1 = int(input())
    c1 = int(input())
    b = b * c1 + c * b1
    c = c * c1

max = max(b, c)
min = min(b, c)
while max % min != 0:
    ost = max % min
    if not ost:
        break
    max = min
    min = ost
print(b // ost, "/", c // ost)