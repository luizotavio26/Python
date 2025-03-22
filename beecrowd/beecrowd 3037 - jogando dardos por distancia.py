casos = int(input())
cont=1
pontos_j = 0
pontos_m = 0
ponto = 0

while cont<=casos:
    cont_2 = 0
    while cont_2<6:
        if cont_2<3:
            pont, dis = input().split()
            pont, dis = int(pont), int(dis)
            ponto = pont*dis
            pontos_j+=ponto
        ponto = 0
        if cont_2>=3:
            pont, dis = input().split()
            pont, dis = int(pont), int(dis)
            ponto = pont*dis
            pontos_m+=ponto
        cont_2+=1
    if pontos_m>pontos_j:
        print("MARIA")
    elif pontos_m==pontos_j:
        print("EMPATE")
    else:
        print("JOAO")
    pontos_m = 0
    pontos_j = 0
    ponto = 0
    cont+=1
  
