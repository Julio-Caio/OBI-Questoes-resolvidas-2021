'''
OBEJTIVO: ler uma string que contenha 3 caracteres para cada carta

U = Ouro
P = Pals
A = Ás
C = Copas

numeros de 1 a 13, onde dois caracteres da string são digitos numericos

SAÍDA:
Produzir uma saída com a quantidade de cartas que cada valete falta

Valetes: 13 cartas ao todo para cada
se houver carta repetida, indique mensagem "erro"
'''

# primeiro leia uma entrada com no minimo 3 caracteres e no máximo, 208 caracteres

# depois, leia a entrada e separe em uma lista de strings com 3 caracteres cada

# faça uma lista para cada valete

# faça um laço de repetição para cada naipe

# se a carta for um Espadas, adicione a lista de Espadas
# se a carta for um Copas, adicione a lista de Copas
# se a carta for um Paus, adicione a lista de Paus
# se a carta for um Ouro, adicione a lista de Ouro

# ao final determine através do len o comprimento, ou seja, a quantidade de elementos de cada naipe
# subtraia com 13 e informe o numero que falta

# se o numero for 0, o naipe está completo

# faça um laço de repeticao para cada carta repetida de cada naipe

# faça uma variavel contadora para caso haja repetidos

# se contador for >= 1, erro

U = []
P = []
A = []
C = []

cartas_rep_A = []
cartas_rep_P = []
cartas_rep_U = []
cartas_rep_C = []

baralho = input()

for i in range(1):
    if len(baralho) % 3 != 0 and len(baralho) > 3 or len(baralho) > 208:
        break

else:
    for i in range(0, len(baralho), 3):
        carta = baralho[i:i+3]

        if carta[2] == 'U':
            U.append(carta)

        elif carta[2] == 'P':
            P.append(carta)

        elif carta[2] == 'E':
            A.append(carta)

        elif carta[2] == 'C':
            C.append(carta)

for carta in A:
    if A.count(carta) > 1:
        cartas_rep_A.append(carta)

for carta in P:
    if P.count(carta) > 1:
        cartas_rep_P.append(carta)

for carta in U:
    if U.count(carta) > 1:
        cartas_rep_U.append(carta)
    
for carta in C:
    if C.count(carta) > 1:
        cartas_rep_C.append(carta)


if len(cartas_rep_C)> 1:
    print('erro')
else: 
    print(13 - len(C))

if len(cartas_rep_A)> 1:
    print('erro')
else:
     print(13 - len(A))

if len(cartas_rep_U)> 1:
            print('erro')
else:
    print(13 - len(U))

if len(cartas_rep_P)> 1:
            print('erro')
else:
    print(13 - len(P))