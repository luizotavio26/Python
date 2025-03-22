x = int(input())
y = int(input())
s = 0
if x > y:
    c = x
    x = y
    y = c
i = x + 1
while i < y:
    if i % 2 != 0:
        s += i
    i += 1
print(s)
