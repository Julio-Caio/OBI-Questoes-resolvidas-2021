N = int(input())
M = int(input())
S = int(input())

matriz = [[] for i in range(M)]

intervalo = []

soma_digitos = []

for i in range(N, M + 1):
    intervalo.append(str(i))

for i in range(len(intervalo)):
    for j in range(len(intervalo[i])):
        matriz[i].append(int(intervalo[i][j]))

    if sum(matriz[i]) == S:
        soma_digitos.append(int(intervalo[i]))

if len(soma_digitos) > 0:
    print(max(soma_digitos))
else:
    print(-1)
    
