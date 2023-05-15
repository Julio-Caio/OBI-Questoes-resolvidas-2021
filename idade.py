def idades_meio (idades):
    maior = max(idades)

    idades.remove(maior)

    if idades[0] > idades[1]:
        meio = idades[0]
    else:
        meio = idades[1]

    return meio

idades = []

for i in range(3):
    idade = int(input())
    idades.append(idade) 

print(idades_meio(idades))