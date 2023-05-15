def remover_zeros(lista):

    numeros_sem_zero = []

    for i in range(len(lista)):

        if lista[i] == 0:
            numeros_sem_zero.pop()
        else:
            numeros_sem_zero.append(lista[i])

    soma = sum(numeros_sem_zero)
        
    return soma

lista = []

qtde = int(input())

for i in range(qtde):
    numeros = int(input())
    lista.append(numeros)

print(remover_zeros(lista))
