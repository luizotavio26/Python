INICIO = int(input())
FIM = int(input())

quant = FIM-INICIO
lista = quant*[0]
C = INICIO
cont = 0
n = 0

while cont<=quant:
    lista[cont]= C
    C+=1
    cont+=1
print(lista)

##while C<FIM:
##    if lista[cont]%4 == 0 and lista[cont]%100!=0:
##        cont+=1
##        print(lista[cont])
##    else:
##        n+=1
##
##print("bissextos:",cont)
