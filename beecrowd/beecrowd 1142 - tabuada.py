N = int(input())
cont = 1

while N>0 and N<=10 and cont<=10:
    tabuada = N * cont
    print(f"{N} x {cont} = {tabuada}")
    cont+=1
