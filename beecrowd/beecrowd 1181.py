linha = int(input())
T = input()

soma = 0
media = 0
cont = 0

while cont<=3: #qtd de linhas
    linhas = []
    linhas.append(linha)
    while cont<3: #preenchendo uma linha com 12 posições
        num = float(input())
        linha = []
        linha.append(num)
        cont+=1
print (linhas)




if T =="S":
    while cont<12:
        soma+=num
        cont+=1
    print(soma)

if T =="M":
    while cont<12:
        soma+=num
        cont+=1
    media = soma/11
    print(media)
