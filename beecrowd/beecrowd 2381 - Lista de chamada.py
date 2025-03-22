##Lista de chamada - beecrowd 2381

N, K = input().split()
N,K = int(N),int(K)
alunos = []

for i in range(N):
    alunos.append(input())

alunos.sort()
print(alunos[K-1])
