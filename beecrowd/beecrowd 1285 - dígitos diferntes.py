mi,ma = input().split()
mi, ma = int(mi), int(ma)
dif =0
iguais= 0
lista = []
qtd = 0

while mi<=ma:
    lista.append(mi)
    mi+=1
    qtd+=1
print(lista)

for numero in lista:
    x = str(numero)
    print(x)



##cont = 0
##while cont<qtd:
##    x = lista[qtd]
##    x = str(x)


##for i in range(mi,ma+1):
##    list(i)
##    print(i)
##    i = str(i)
##    x = len(i)
##    cont = x
##    while cont>=0:
##        if i[cont]==i[cont-1]:
##            iguais +=1
##        else:
##            lista.append(i)
##            dif+=1
##        cont =-1
##print(dif)
    



##for i in range(mi,ma+1):
##    i = str(i)
##    x = len(i)
##    while cont>=0:
##        if i[x]==i[x-1] or i[x-1]==[x-2]:
##            iguais +=1
##        else:
##            lista.append(i)
##            dif+=1
##        cont
##print(dif)
    


['87', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '100', '101', '102', '103', '104']
##87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 102, 103, 104
##
##88, 99, 100, 101
