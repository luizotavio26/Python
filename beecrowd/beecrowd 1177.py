t = int(input())
cont = 0
lista = []
num = 0

while cont<1000:
        if num==t:
            num=0
        lista.append(num)
        num+=1
        cont+=1

cont = 0

for i in lista:
    print(f"N[{cont}] = {i}")
    cont+=1
