def gera():
    cont = 0
    cont_2 = 0
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []
    l8 = []
    l9 = []
    l10 = []
    l11 = []
    l12 = []
    linhas = []

    while cont<12:
        num =float(input())
        l1.append(num)
        cont+=1
    linhas.append(l1)

    cont = 0
    while cont<12:
        num =float(input())
        l2.append(num)
        cont+=1
    linhas.append(l2)

    cont = 0
    while cont<12:
        num =float(input())
        l3.append(num)
        cont+=1
    linhas.append(l3)

    cont = 0
    while cont<12:
        num =float(input())
        l4.append(num)
        cont+=1
    linhas.append(l4)

    cont = 0
    while cont<12:
        num =float(input())
        l5.append(num)
        cont+=1
    linhas.append(l5)

    cont = 0
    while cont<12:
        num =float(input())
        l6.append(num)
        cont+=1
    linhas.append(l6)

    cont = 0
    while cont<12:
        num =float(input())
        l7.append(num)
        cont+=1
    linhas.append(l7)

    cont = 0
    while cont<12:
        num =float(input())
        l8.append(num)
        cont+=1
    linhas.append(l8)

    cont = 0
    while cont<12:
        num =float(input())
        l9.append(num)
        cont+=1
    linhas.append(l9)

    cont = 0
    while cont<12:
        num =float(input())
        l10.append(num)
        cont+=1
    linhas.append(l10)

    cont = 0
    while cont<12:
        num =float(input())
        l11.append(num)
        cont+=1
    linhas.append(l11)

    cont = 0
    while cont<12:
        num =float(input())
        l12.append(num)
        cont+=1
    linhas.append(l12)

    return linhas

L = int(input())
T = input()
x = gera()
soma = 0
media = 0
cont = 0
h = x[L]

if T =="S":
    while cont<12:
        num = h[cont]
        soma+=num
        cont+=1
    print(soma)
    
if T =="M":
    while cont<12:
        num = h[cont]
        soma+=num
        cont+=1
    media = soma/12
    print(media)
