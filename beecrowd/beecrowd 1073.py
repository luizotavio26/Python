def quad(y):
    y=y**2
    return y

N = int(input())
y= 1

while N>=y:
    quad(y)
    y+=2
    print(y)
