import random
N = int(input('Введите количество строк и столбцов (квадратная матрица) :'))
a = []
for i in range(N):
    b = []
    for j in range(N):
        b.append(int(random.random()*11))
        print("%3d" % b[j], end='')
    a.append(b)
    print()
