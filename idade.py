# dona monica

'''
 a soma das idades dos seus três filhos é igual à idade dela

 a idade do filho mais velho

'''
dona_monica = int(input())

lista_idades = []

for i in range(2):
    lista_idades.append(int(input()))

lista_idades.append(dona_monica - sum(lista_idades))

filho_mais_velho = max(lista_idades)

print(filho_mais_velho)