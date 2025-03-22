def lista_notas(alunos):
    lista = alunos*[0]
    cont = 1
    pos = 0
    while cont<=alunos:
        lista[pos]= float(input())
        cont+=1
        pos +=1
    return lista

def nota_final(alunos):
    lista = alunos*[0]
    cont = 1
    pos = 0
    return lista

a = input()
alunos = int(a)

original = lista_notas(alunos)
sub = lista_notas(alunos)

cont = 1
pos = 0
alteradas = 0
final = nota_final(alunos)

while cont<=alunos:
    if original[pos]==10:
        final[pos] = 10
    else:
        if sub[pos]==10:
            alteradas+=1
            final[pos]=original[pos]+2
            if final[pos]>10:
                final[pos]=10
        else:
            final[pos]= original[pos]
    pos+=1
    cont+=1
print("NOTAS ALTERADAS:", alteradas)

cont = 1
pos = 0

while cont<=alunos:
    if sub[pos]==10 and original[pos]<10:
        print(f"*(00{cont}) original: {original[pos]:05.2f} | final: {final[pos]:05.2f}")
    else:
        print(f"-(00{cont}) original: {original[pos]:05.2f} | final: {final[pos]:05.2f}")
    cont+=1
    pos+=1
    
