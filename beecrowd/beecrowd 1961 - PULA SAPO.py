pulos, num = input().split()
pulos, num = int(pulos), int(num)
cont = 1
vitorias = 0
comparacao = 1


while cont<=num:
    alturas = int(input())
    if comparacao <= alturas:     # subindo
        diferenca = alturas - comparacao
        if diferenca <=pulos:
            vitorias+=1
    else:# comparacao > alturas:
        diferenca = comparacao - alturas
        if diferenca <= pulos:
            vitorias+=1
    comparacao = alturas
    cont+=1

if vitorias == num:
    print("YOU WIN")
else:
    print("GAME OVER")
