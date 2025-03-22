n = int(input("casos?" ))
cont = 1
lista = []
soma = 0
while cont<=n:
    x = int(input("num?" ))
    for numeros in range(1,x):
        if x%numeros==0:
            lista.append(numeros)
            soma+=numeros
    if soma==x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
    print(lista)
    print(soma)
    lista = []
    soma = 0
    cont+=1

