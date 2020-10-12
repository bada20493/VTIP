import random
N = int(input('Введите количество строк :'))
M = int(input('Введите количество столбцов :'))
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random.random()*11))
        print("%3d" % b[j], end='')
    a.append(b)
    print()
