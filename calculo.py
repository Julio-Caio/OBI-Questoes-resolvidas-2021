## Fase 2 - Calculo Rápido - Nível 2 Programação

s = int(input())
a = input()
b = input()
count = 0

# Neste código, precisamos descobrir os números entre o intervalo de A e B, que possuem como soma de seus algarismos
# o valor de S

# Para isso, tivemos que montar um laço for com esse intervalo
# Logo após, para cada interação do primeiro laço, ou seja, para cada numero percorrido no intervalo
# tivemos que percorrer cada algarismo desse numero, adicionando os algarismos desse numero numa lista
# e somando os valores dessa lista, para ver se a soma dos algarismos é igual ao valor de S

# Desse modo, se a soma for igual a S, incrementamos no contador

valoresA_inteiros = []

for i in range(int(a), int(b) + 1):
    for j in str(i):
        valoresA_inteiros.append(int(j))

    if sum(valoresA_inteiros) == s:
        count += 1

    valoresA_inteiros = []

print('Contador:', count)

# Exemplos de entrada:
'''
3
10
30

Os valores que possuem a soma de seus algarismos neste caso, é 12, 21, 30
Ou seja, o contador deve dar 3

'''