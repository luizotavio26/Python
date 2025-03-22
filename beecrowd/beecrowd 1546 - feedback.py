dias = int(input())
cont_dias = 0
cont_feed = 0

while cont_dias<dias:
    feedbacks = int(input())
    while cont_feed<feedbacks:
        tipo = int(input())
        if tipo == 1:
            print("Rolien")
        elif tipo == 2:
            print("Naej")
        elif tipo == 3:
            print("Elehcim")
        else:
            print("odranoel")
        cont_feed+=1
    cont_dias+=1
    cont_feed = 0

## x dias de trabalho
## quantos feedbacks por dia
## recepção de cada feedback
## devolução de cada funcionário
