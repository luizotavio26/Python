trabalhos = float(input())
prova = float(input())

media = (trabalhos + prova)/2

if media >=6:
    print("aprovado")
else:
    if trabalhos <2:
        print("reprovado")
    else:
        print("talvez com a sub")
