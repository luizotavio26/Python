N = []
cont = 0

while cont< 20:
    num = int(input())
    N.append(num)
    cont+=1

N.reverse()
cont = 0

for i in N:
    print(f"N[{cont}] = {i}")
    cont+=1
