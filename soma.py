n, k = [int(x) for x in input().split()]

seq = [int(x) for x in input().split()]

# para cada conjunto de valor numa lista, somar e verificar se dá K
# se der, adicionar 1 ao contador

contador = []

while True:
    for i in range(len(seq)):
        soma = 0
        for j in range(i, len(seq)):
            soma += seq[j]
            if soma == k:
                contador.append(seq[i:j+1])
    break


print(len(contador))