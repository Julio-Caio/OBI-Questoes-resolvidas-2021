'''

níveis dos dois times formados sejam o mais próximo possível

nível de um time é a soma dos níveis dos jogadores do time


encontrar a menor diferença possível entre os níveis dos times

'''
times = []
soma1 = 0
soma2 = 0
list1 = []
list2 = []

for j in range(4):
    time = int(input())
    
    times.append(time)

for i in range(len(times)//2):
    list1.append(times[i])
max1 = max(list1)
min1 = min(list1)

for num in list1:
    if num in times:
        times.remove(num)
        
max2 = max(times)
min2 = min(times)

dif = abs((max1 + min2) - (max2 + min1))
print(dif)
