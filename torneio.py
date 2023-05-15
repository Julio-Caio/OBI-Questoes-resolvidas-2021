resultados_torneiosP = []
resultados_torneiosV = []
torneios = []

for i in range(6):
    resultado = input()
    torneios.append(resultado)


for result in torneios:
    if result == 'P' or result == 'V':
        if result == 'P':
            resultados_torneiosP.append(result)
        else:
            resultados_torneiosV.append(result)
    else:
        break

if 5 <= len(resultados_torneiosV) <= 6:
    print('1')
elif 3 <= len(resultados_torneiosV) <= 4:
    print('2')
elif 1 <= len(resultados_torneiosV) <= 2:
    print('3')
else:
    print('-1')