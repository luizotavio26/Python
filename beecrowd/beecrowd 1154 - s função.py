idade = int(input())
i = 0
cont = 0

while idade >= 0:
    i+=idade
    cont+=1
    idade=int(input())
    
media = i/cont

print(f"{media:.2f}")
